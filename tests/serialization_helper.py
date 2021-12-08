"""
A module that simplifies assertions for json serialization
"""
import json
from typing import TypeVar

from marshmallow import Schema

T = TypeVar("T")


def assert_serialization_roundtrip(serializable_object: T, schema: Schema, expected_json_dict: dict) -> T:
    """
    Serializes the serializable_object using the provided schema,
    asserts, that the result is equal to the expected_json_dict
    then deserializes it again and asserts on equality with the original serializable_object
    :returns the deserialized_object
    """
    json_string = schema.dumps(serializable_object)
    assert json_string is not None
    actual_json_dict = json.loads(json_string)
    assert actual_json_dict == expected_json_dict
    deserialized_object = schema.loads(json_data=json_string)
    assert isinstance(deserialized_object, type(serializable_object))
    assert deserialized_object == serializable_object
    return deserialized_object
