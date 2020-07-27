import unittest
import weaviate
from test.testing_util import add_run_rest_to_mock
from weaviate.connect import REST_METHOD_DELETE
from weaviate import UnexpectedStatusCodeException
import sys
if sys.version_info[0] == 2:
    from mock import MagicMock as Mock
else:
    from unittest.mock import Mock

class TestDelete(unittest.TestCase):

    def test_delete_thing_input(self):
        w = weaviate.Client("http://localhost:8080")
        try:
            w.delete(4)
            self.fail("UUID has the wrong type")
        except TypeError:
            pass

        try:
            w.delete("Hallo Wereld")
            self.fail("UUID has the wrong value")
        except ValueError:
            pass

    def test_delete_thing(self):
        w = weaviate.Client("http://localhost:8080")

        # 1. Succesfully delete something
        connection_mock = Mock()
        w._connection = add_run_rest_to_mock(connection_mock, status_code=204)

        thing = "b36268d4-a6b5-5274-985f-45f13ce0c642"
        w.delete(thing)

        connection_mock.run_rest.assert_called_with("/things/"+thing, REST_METHOD_DELETE)

        # 2. Delete something that does not exist
        connection_mock = Mock()
        w._connection = add_run_rest_to_mock(connection_mock, status_code=404)

        thing = "b36268d4-a6b5-5274-985f-45f13ce0c642"
        try:
            w.delete(thing)
            self.fail("Unexpected status code")
        except UnexpectedStatusCodeException:
            pass

        connection_mock.run_rest.assert_called_with("/things/" + thing, REST_METHOD_DELETE)

    def test_delete_reference_from_thing_input(self, ):
        w = weaviate.Client("http://localhost:8080")

        uuid_1 = "b36268d4-a6b5-5274-985f-45f13ce0c642"
        uuid_2 = "a36268d4-a6b5-5274-985f-45f13ce0c642"

        try:
            w.delete_reference(1, "myProperty", uuid_2)
            self.fail("UUID has the wrong type")
        except TypeError:
            pass
        try:
            w.delete_reference(uuid_1, "myProperty", 2)
            self.fail("UUID has the wrong type")
        except TypeError:
            pass
        try:
            w.delete_reference(uuid_1, 3, uuid_2)
            self.fail("Property name has the wrong type")
        except TypeError:
            pass
        try:
            w.delete_reference("str", "myProperty", uuid_2)
            self.fail("UUID has the wrong value")
        except ValueError:
            pass
        try:
            w.delete_reference(uuid_1, "myProperty", "str")
            self.fail("UUID has the wrong value")
        except ValueError:
            pass
        try:
            w.delete_reference(uuid_1, "myProperty", uuid_2, to_weaviate=4)
            self.fail("to_weaviate has the wrong type")
        except TypeError:
            pass

    def test_delete_reference_from_thing(self):
        w = weaviate.Client("http://localhost:8080")

        # 1. Succesfully delete something
        connection_mock = Mock()
        w._connection = add_run_rest_to_mock(connection_mock, status_code=204)

        thing = "b36268d4-a6b5-5274-985f-45f13ce0c642"
        to_thing = "a36268d4-a6b5-5274-985f-45f13ce0c642"
        w.delete_reference(thing, "myProperty", to_thing)

        body = {
            "beacon": "weaviate://localhost/things/"+to_thing
        }

        connection_mock.run_rest.assert_called_with("/things/"+thing+"/references/myProperty", REST_METHOD_DELETE, body)

    def test_get_thinng(self):
        w = weaviate.Client("http://localhost:8080")

        thing = {
            "name": "test"
        }
        connection_mock = Mock()
        w._connection = add_run_rest_to_mock(connection_mock, return_json=thing, status_code=200)

        result = w.get("73802305-c0da-427e-b21c-d6779a22f35f")
        self.assertIn("name", result)
