import weaviate
import requests
import json


def test_gql_injection() -> None:
    client = weaviate.Client(url="http://localhost:8080")
    client.schema.delete_class("Question")
    client.schema.delete_class("Hacked")
    class_obj = {
        "class": "Question",
        "vectorizer": "text2vec-contextionary",
        "properties": [
            {"name": "answer", "dataType": ["string"], "tokenization": "field"},
            {"name": "question", "dataType": ["string"]},
            {"name": "category", "dataType": ["string"]},
        ],
    }

    class_obj2 = {
        "class": "Hacked",
        "vectorizer": "text2vec-contextionary",
        "properties": [
            {"name": "answer", "dataType": ["string"]},
            {"name": "question", "dataType": ["string"]},
            {"name": "category", "dataType": ["string"]},
        ],
    }
    client.schema.create_class(class_obj)
    client.schema.create_class(class_obj2)

    resp = requests.get(
        "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json"
    )
    data = json.loads(resp.text)

    client.batch.configure(batch_size=100)
    with client.batch as batch:
        for _, d in enumerate(data):
            properties = {
                "answer": d["Answer"],
                "question": d["Question"],
                "category": d["Category"],
            }
            batch.add_data_object(data_object=properties, class_name="Question")
            batch.add_data_object(data_object=properties, class_name="Hacked")

    injection_payload = client.query.get("Hacked", ["answer"]).build()
    injection_template = 'Liver\\\\"}}){{answer}}}}{payload}#'
    query = client.query.get("Question", ["question", "answer", "category"]).with_where(
        {
            "path": ["answer"],
            "operator": "NotEqual",
            "valueText": injection_template.format(payload=injection_payload[1:]),
        }
    )
    res = query.do()
    assert "Hacked" not in res["data"]["Get"]
