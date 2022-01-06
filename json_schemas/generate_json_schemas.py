"""
This script is run in the tox 'json_schemas' environment.
It creates json schema files as described in the README.md in the same directory.
"""

import json
import pathlib
from typing import List, Type

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema  # type:ignore[import]

from bo4e.bo.marktlokation import MarktlokationSchema

schema_types: List[Type[Schema]] = [MarktlokationSchema]
json_schema = JSONSchema()
for schema_type in schema_types:
    this_directory = pathlib.Path(__file__).parent.absolute()
    file_name = schema_type.__name__ + ".json"  # pylint:disable=invalid-name
    file_path = this_directory / file_name
    schema_instance = schema_type()
    json_schema_dict = json_schema.dump(schema_instance)
    with open(file_path, "w", encoding="utf-8") as json_schema_file:
        json.dump(json_schema_dict, json_schema_file, ensure_ascii=False, sort_keys=True, indent=4)
