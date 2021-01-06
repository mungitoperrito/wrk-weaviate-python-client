import sys
import json
from typing import List, Optional
from weaviate.connect import REST_METHOD_POST, Connection
from weaviate.exceptions import UnexpectedStatusCodeException, RequestsConnectionError
from .filter import WhereFilter

class AggregateBuilder:
    """
    AggregateBuilder class used to aggregate weaviate objects.
    """

    def __init__(self, class_name: str, connection: Connection):
        """
        Initialize a AggregateBuilder class instance.

        Parameters
        ----------
        class_name : str
            Class name of the objects to be aggregated.
        connection : weaviate.connect.Connection
            Connection object to an active and running weaviate instance.
        """

        self._class_name = class_name
        self._connection = connection
        self._with_meta_count = False
        self._fields: List[str] = []
        self._where: Optional[WhereFilter] = None
        self._group_by_properties: Optional[List[str]] = None
        self._uses_filter = False

    def with_meta_count(self) -> 'AggregateBuilder':
        """
        Set Meta Count to True.

        Returns
        -------
        weaviate.gql.aggregate.AggregateBuilder
            Updated AggregateBuilder.
        """

        self._with_meta_count = True
        return self

    def with_fields(self, field: str) -> 'AggregateBuilder':
        """
        Include a field in the aggregate query.

        Parameters
        ----------
        field : str
            Field to include in the aggregate query.
            e.g. '<property_name> { count }'

        Returns
        -------
        weaviate.gql.aggregate.AggregateBuilder
            Updated AggregateBuilder.
        """

        self._fields.append(field)
        return self

    def with_where(self, filter: dict) -> 'AggregateBuilder':
        """
        Set 'where' filter.

        Parameters
        ----------
        filter : dict
            The where filter to include in the aggregate query.

        Returns
        -------
        weaviate.gql.aggregate.AggregateBuilder
            Updated AggregateBuilder.
        """

        self._where = WhereFilter(filter)
        self._uses_filter = True
        return self

    def with_group_by_filter(self, properties: List[str]) -> 'AggregateBuilder':
        """
        Add a group by filter to the query. Might requires the user to set
        an additional group by clause using `with_fields(..)`.

        Parameters
        ----------
        properties : list of str
            list of properties that are included in the group by filter.
            Generates a filter like: 'groupBy: ["property1", "property2"]'
            from a list ["property1", "property2"]

        Returns
        -------
        weaviate.gql.aggregate.AggregateBuilder
            Updated AggregateBuilder.
        """

        self._group_by_properties = properties
        self._uses_filter = True
        return self

    def build(self) -> str:
        """
        Build the query and return the string.

        Returns
        -------
        str
            The GraphQL query as a string.
        """

        # Path
        query = f"{{Aggregate{{{self._class_name}"

        # Filter
        if self._uses_filter:
            query += "("
        if self._where is not None:
            query += f"where: {str(self._where)} "
        if self._group_by_properties is not None:
            query += f"groupBy: {json.dumps(self._group_by_properties)}"
        if self._uses_filter:
            query += ")"

        # Body
        query += "{"
        if self._with_meta_count:
            query += "meta{count}"
        for field in self._fields:
            query += field

        # close
        query += "}}}"
        return query

    def do(self) -> dict:
        """
        Builds and runs the query.

        Returns
        -------
        dict
            The response of the query.

        Raises
        ------
        requests.exceptions.ConnectionError
            If the network connection to weaviate fails.
        weaviate.UnexpectedStatusCodeException
            If weaviate reports a none OK status.
        """

        query = self.build()

        try:
            response = self._connection.run_rest("/graphql", REST_METHOD_POST, {"query": query})
        except RequestsConnectionError as conn_err:
            message = str(conn_err) + ' Connection error, query was not successful.'
            raise type(conn_err)(message).with_traceback(sys.exc_info()[2])
        if response.status_code == 200:
            return response.json()  # success
        raise UnexpectedStatusCodeException("Query was not successful", response)
