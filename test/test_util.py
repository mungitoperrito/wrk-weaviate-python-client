import unittest
from unittest.mock import patch, Mock
from weaviate.util import * 
from weaviate.util import  _get_dict_from_object, _is_sub_schema

schema_set = {
    "classes": [
        {
            "class": "Ollie",
            "properties": [{"name": "height"}]
        },
        {
            "class": "Shuvit",
            "properties": [{"name": "direction"}]
        },
        {
            "class": "Board",
            "properties": [{"name": "brand"},
                            {"name": "art"},
                            {"name": "size"}]
        },
        {
            "class": "Truck",
            "properties": [{"name": "name"},
                            {"name": "height"}]
        }
    ],
}

schema_set_extended_prop = {
    "classes": [
        {
            "class": "Ollie",
            "properties": [{"name": "height", "name": "weight"}]
        },
        {
            "class": "Shuvit",
            "properties": [{"name": "direction"}]
        },
        {
            "class": "Board",
            "properties": [{"name": "brand"},
                            {"name": "art"},
                            {"name": "size"}]
        },
        {
            "class": "Truck",
            "properties": [{"name": "name"},
                            {"name": "height"}]
        }
    ],
}

schema_sub_set = {
    "classes": [
        {
            "class": "Ollie",
            "properties": [{"name": "height"}]
        },
        {
            "class": "Board",
            "properties": [{"name": "brand"},
                            {"name": "art"},
                            {"name": "size"}]
        }
    ],
}

disjoint_set = {
    "classes": [
        {
            "class": "Manual",
            "properties": [{"name": "nose"}]
        },
        {
            "class": "Bearings",
            "properties": [{"name": "brand"}]
        }
    ],
}

partial_set = {
    "classes": [
        {
            "class": "Board",
            "properties": [{"name": "brand"},
                            {"name": "art"},
                            {"name": "size"}]
        },
        {
            "class": "Truck",
            "properties": [{"name": "name"},
                            {"name": "height"}]
        },
        {
            "class": "Bearings",
            "properties": [{"name": "brand"}]
        },
        {
            "class": "Ollie",
            "properties": [{"name": "height"}]
        },
        {
            "class": "Shuvit",
            "properties": [{"name": "direction"}]
        },
        {
            "class": "Manual",
            "properties": [{"name": "nose"}]
        }
    ],
}

schema_company = {
  "classes": [
    {
      "class": "Company",
      "description": "A business that acts in the market",
      "properties": [
        {
          "name": "name",
          "description": "The name under which the company is known",
          "dataType": ["text"]
        },
        {
          "name": "legalBody",
          "description": "The legal body under which the company maintains its business",
          "dataType": ["text"]
        },
        {
          "name": "hasEmployee",
          "description": "The employees of the company",
          "dataType": ["Employee"]
        }
      ]
    },
    {
      "class": "Employee",
      "description": "An employee of the company",
      "properties": [
        {
          "name": "name",
          "description": "The name of the employee",
          "dataType": ["text"]
        },
        {
          "name": "job",
          "description": "the job description of the employee",
          "dataType": ["text"]
        },
        {
          "name": "yearsInTheCompany",
          "description": "The number of years this employee has worked in the company",
          "dataType": ["int"]
        }
      ]
    }
  ]
}


class TestUtil(unittest.TestCase):

    def test_is_weaviate_object_url(self):
        """
        Test the `is_weaviate_object_url` function.
        """

        # valid formats
        self.assertTrue(
            is_weaviate_object_url("weaviate://localhost/28f3f61b-b524-45e0-9bbe-2c1550bf73d2"))
        self.assertTrue(
            is_weaviate_object_url("weaviate://some-domain.com/28f3f61b-b524-45e0-9bbe-2c1550bf73d2"))

        # invalid formats
        ## wrong argument data type
        self.assertFalse(
            is_weaviate_object_url(["weaviate://localhost/28f3f61b-b524-45e0-9bbe-2c1550bf73d2"]))
        ## wrong prefix, i.e. does not start with 'weaviate://' 
        self.assertFalse(
            is_weaviate_object_url("http://some-domain.com/28f3f61b-b524-45e0-9bbe-2c1550bf73d2"))
        ## wrong path, additional '/thing'
        self.assertFalse(
            is_weaviate_object_url("weaviate://localhost/things/f61b-b524-45e0-9bbe-2c1550bf73d2"))
        ## worng domain format
        self.assertFalse(
            is_weaviate_object_url("weaviate://some-INVALID-domain/28f3f61b-b524-45e0-9bbe-2c1550bf73d2"))
        # wrong UUID format
        self.assertFalse(
            is_weaviate_object_url("weaviate://localhost/UUID"))

    def test_is_object_url(self):
        """
        Test the `is_object_url` function.
        """

        # valid formats
        self.assertTrue(
            is_object_url("http://localhost:8080/v1/objects/1c9cd584-88fe-5010-83d0-017cb3fcb446"))
        self.assertTrue(
            is_object_url("http://ramalamadingdong/v1/objects/1c9cd584-88fe-5010-83d0-017cb3fcb446"))

        # invalid formats
        ## wrong path, should be at least 3 subpaths to the object UUID
        self.assertFalse(
            is_object_url("objects/1c9cd584-88fe-5010-83d0-017cb3fcb446"))
        ## wrong '/v2', shoudl be '/v1'  
        self.assertFalse(
            is_object_url("http://localhost:8080/v2/objects/1c9cd584-88fe-5010-83d0-017cb3fcb446"))
        ## wrong UUID format
        self.assertFalse(
            is_object_url("http://ramalamadingdong/v1/objects/1c9cd584-88fe-5010-83d0"))
        ## wrong objects path, instead of '/passions' should have been '/objects/
        self.assertFalse(
            is_object_url("http://localhost:8080/v1/passions/1c9cd584-88fe-5010-83d0-017cb3fcb446"))

    def test_get_valid_uuid(self):
        """
        Test the `get_valid_uuid` function.
        """

        # valid calls
        result = get_valid_uuid("weaviate://localhost/28f3f61b-b524-45e0-9bbe-2c1550bf73d2")
        self.assertEqual(result, "28f3f61b-b524-45e0-9bbe-2c1550bf73d2")

        result = get_valid_uuid("weaviate://otherhost.com/28f3f61b-b524-45e0-9bbe-2c1550bf73d2")
        self.assertEqual(result, "28f3f61b-b524-45e0-9bbe-2c1550bf73d2")

        result = get_valid_uuid("http://localhost:8080/v1/objects/1c9cd584-88fe-5010-83d0-017cb3fcb446")
        self.assertEqual(result, "1c9cd584-88fe-5010-83d0-017cb3fcb446")

        result = get_valid_uuid("http://otherhost_2:8080/v1/objects/1c9cd584-88fe-5010-83d0-017cb3fcb446")
        self.assertEqual(result, "1c9cd584-88fe-5010-83d0-017cb3fcb446")

        result = get_valid_uuid("1c9cd584-88fe-5010-83d0-017cb3fcb446")
        self.assertEqual(result, "1c9cd584-88fe-5010-83d0-017cb3fcb446")

        # invalid formats (return None)
        ## neither an object URL nor a weaviate object URL 
        result = get_valid_uuid("http://localhost:8080/v1/1c9cd584-88fe-5010-83d0-017cb3fcb")
        self.assertIsNone(result)

        # wrong UUID format
        result = get_valid_uuid("http://localhost:8080/v1/objects/some-UUID")
        self.assertIsNone(result)

        ## wrong '/v2', shoudl be '/v1' 
        result = get_valid_uuid("http://localhost:8080/v2/objects/1c9cd584-88fe-5010-83d0-017cb3fcb")
        self.assertIsNone(result)
        ## wrong URL
        result = get_valid_uuid("weaviate://INVALID_URL//1c9cd584-88fe-5010-83d0-017cb3fcb")
        self.assertIsNone(result)

        ## wrong UUID data type
        with self.assertRaises(TypeError):
            get_valid_uuid(12353465373573753)

    def test_get_uuid_from_weaviate_url(self):
        """
        Test the `get_uuid_from_weaviate_url` function.
        """

        uuid = "28f3f61b-b524-45e0-9bbe-2c1550bf73d2"
        self.assertEqual(get_uuid_from_weaviate_url(f"weaviate://localhost/{uuid}"), uuid)
        self.assertEqual(get_uuid_from_weaviate_url(f"weaviate://otherhost/{uuid}"), uuid)

    def test_get_domain_from_weaviate_url(self):
        """
        Test the `get_domain_from_weaviate_url` function.
        """

        uuid = "28f3f61b-b524-45e0-9bbe-2c1550bf73d2"
        self.assertEqual(get_domain_from_weaviate_url(f"weaviate://localhost/{uuid}"), "localhost")
        self.assertEqual(get_domain_from_weaviate_url(f"weaviate://otherhost/{uuid}"), "otherhost")

    def test__is_sub_schema(self):
        """
        Test the `_is_sub_schema` function.
        """

        self.assertTrue(_is_sub_schema(schema_set, schema_set))
        self.assertTrue(_is_sub_schema(schema_sub_set, schema_set))
        self.assertTrue(_is_sub_schema({}, schema_set))

        self.assertFalse(_is_sub_schema(disjoint_set, schema_set))
        self.assertFalse(_is_sub_schema(partial_set, schema_set))
        self.assertFalse(_is_sub_schema(schema_set_extended_prop, schema_set))

    def test_generate_local_beacon(self):
        """
        Test the `generate_local_beacon` function.
        """

        # wrong data type
        with self.assertRaises(TypeError):
            generate_local_beacon(None)
        # wrong value
        with self.assertRaises(ValueError):
            generate_local_beacon("Leeroy Jenkins")

        beacon = generate_local_beacon("fcf33178-1b5d-5174-b2e7-04a2129dd35a")
        self.assertTrue("beacon" in beacon)
        self.assertEqual(beacon["beacon"], "weaviate://localhost/fcf33178-1b5d-5174-b2e7-04a2129dd35a")

        beacon = generate_local_beacon("fcf33178-1b5d-5174-b2e7-04a2129dd35b")
        self.assertTrue("beacon" in beacon)
        self.assertEqual(beacon["beacon"], "weaviate://localhost/fcf33178-1b5d-5174-b2e7-04a2129dd35b")

    def test__get_dict_from_object(self):
        """
        Test the `_get_dict_from_object` function.
        """

        # test wrong type None
        with self.assertRaises(TypeError):
            _get_dict_from_object(None)
        # wrong data type
        with self.assertRaises(TypeError):
            _get_dict_from_object([{"key": 1234}])
        # wrong value
        with self.assertRaises(ValueError):
            _get_dict_from_object("not_a_path_or_url")
        # wrong URL or non existing one or failure of requests.get
        with patch('weaviate.util.requests') as mock_obj:
            result_mock = Mock()
            result_mock.status_code = 404
            mock_obj.get.return_value = result_mock
            with self.assertRaises(ValueError):
                _get_dict_from_object("http://www.url.com")
            mock_obj.get.assert_called()

        # valid calls
        self.assertEqual(_get_dict_from_object({"key": "val"}), {"key": "val"})
        # read from file
        path = '/'.join(__file__.split('/')[:-1])
        self.assertEqual(_get_dict_from_object(f'{path}/schema/schema_company.json'), schema_company)
        # read from URL
        path = "https://raw.githubusercontent.com/semi-technologies/weaviate-python-client/weaviate_v1/test/schema/schema_company.json"
        self.assertEqual(_get_dict_from_object(path), schema_company)
