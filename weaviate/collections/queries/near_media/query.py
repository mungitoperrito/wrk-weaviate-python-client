from io import BufferedReader
from pathlib import Path
from typing import Generic, Optional, Union

from weaviate import syncify
from weaviate.collections.classes.filters import (
    _Filters,
)
from weaviate.collections.classes.grpc import (
    GroupBy,
    METADATA,
    NearMediaType,
    Rerank,
    TargetVectorJoinType,
)
from weaviate.collections.classes.internal import (
    _GroupBy,
    ReturnProperties,
    ReturnReferences,
    _QueryOptions,
    QuerySearchReturnType,
)
from weaviate.collections.classes.types import Properties, TProperties, References, TReferences
from weaviate.collections.queries.base import _Base
from weaviate.types import NUMBER, INCLUDE_VECTOR


class _NearMediaQueryAsync(Generic[Properties, References], _Base[Properties, References]):
    async def near_media(
        self,
        media: Union[str, Path, BufferedReader],
        media_type: NearMediaType,
        *,
        certainty: Optional[NUMBER] = None,
        distance: Optional[NUMBER] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        auto_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        group_by: Optional[GroupBy] = None,
        rerank: Optional[Rerank] = None,
        target_vector: Optional[TargetVectorJoinType] = None,
        include_vector: INCLUDE_VECTOR = False,
        return_metadata: Optional[METADATA] = None,
        return_properties: Optional[ReturnProperties[TProperties]] = None,
        return_references: Optional[ReturnReferences[TReferences]] = None,
    ) -> QuerySearchReturnType[Properties, References, TProperties, TReferences]:
        """Search for objects by audio in this collection using an audio-capable vectorization module and vector-based similarity search.

        See the [docs](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/multi2vec-bind) for a more detailed explanation.

        NOTE:
            You must have a multi-media-capable vectorization module installed in order to use this method, e.g. `multi2vec-bind`.

        Arguments:
            `media`
                The media file to search on, REQUIRED. This can be a base64 encoded string of the binary, a path to the file, or a file-like object.
            `media_type`
                The type of the provided media file, REQUIRED.
            `certainty`
                The minimum similarity score to return. If not specified, the default certainty specified by the server is used.
            `distance`
                The maximum distance to search. If not specified, the default distance specified by the server is used.
            `limit`
                The maximum number of results to return. If not specified, the default limit specified by the server is returned.
            `offset`
                The offset to start from. If not specified, the retrieval begins from the first object in the server.
            `auto_limit`
                The maximum number of [autocut](https://weaviate.io/developers/weaviate/api/graphql/additional-operators#autocut) results to return. If not specified, no limit is applied.
            `filters`
                The filters to apply to the search.
            `group_by`
                How the results should be grouped by a specific property.
            `rerank`
                How the results should be reranked. NOTE: A `rerank-*` module must be enabled for this functionality to work.
            `target_vector`
                The name of the vector space to search in for named vector configurations. Required if multiple spaces are configured.
            `include_vector`
                Whether to include the vector in the results. If not specified, this is set to False.
            `return_metadata`
                The metadata to return for each object, defaults to `None`.
            `return_properties`
                The properties to return for each object.
            `return_references`
                The references to return for each object.

        NOTE:
            - If `return_properties` is not provided then all properties are returned except for blob properties.
            - If `return_metadata` is not provided then no metadata is provided. Use MetadataQuery.full() to retrieve all metadata.
            - If `return_references` is not provided then no references are provided.

        Returns:
            A `QueryReturn` or `GroupByReturn` object that includes the searched objects.
            If `group_by` is provided then a `GroupByReturn` object is returned, otherwise a `QueryReturn` object is returned.

        Raises:
            `weaviate.exceptions.WeaviateQueryError`:
                If the request to the Weaviate server fails.
        """
        res = await self._query.near_media(
            media=self._parse_media(media),
            type_=media_type.value,
            certainty=certainty,
            distance=distance,
            limit=limit,
            offset=offset,
            autocut=auto_limit,
            filters=filters,
            group_by=_GroupBy.from_input(group_by),
            rerank=rerank,
            target_vector=target_vector,
            return_metadata=self._parse_return_metadata(return_metadata, include_vector),
            return_properties=self._parse_return_properties(return_properties),
            return_references=self._parse_return_references(return_references),
        )
        return self._result_to_query_or_groupby_return(
            res,
            _QueryOptions.from_input(
                return_metadata,
                return_properties,
                include_vector,
                self._references,
                return_references,
                rerank,
            ),
            return_properties,
            return_references,
        )


@syncify.convert
class _NearMediaQuery(
    Generic[Properties, References], _NearMediaQueryAsync[Properties, References]
):
    pass
