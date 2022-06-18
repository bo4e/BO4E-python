"""
A module that simplifies assertions for json serialization
"""
from typing import TypeVar

from dictdiffer import diff

T = TypeVar("T")


def assert_serialization_roundtrip(serializable_object: T, expected_json_dict: dict = None) -> T:
    """
    Serializes the serializable_object using the provided schema,
    then asserts, that the result is equal to the expected_json_dict (if given),
    then deserializes the dictionary again and asserts the equality with the original serializable_object
    :returns the deserialized_object
    """
    json_string = serializable_object.json(by_alias=True, ensure_ascii=False)
    assert json_string is not None
    actual_json_dict = serializable_object.dict(by_alias=True)
    assert actual_json_dict is not None
    # TODO: serializable_object.dict()
    if expected_json_dict is not None:
        # this contains the difference between two dicts -> just for easier debugging
        diffDict = list(diff(expected_json_dict, actual_json_dict))

        assert all([(k in json_string) for k in expected_json_dict.keys()])
        assert actual_json_dict == expected_json_dict, f"actual_json_dict != expected_json_dict\n\tdiff = {diffDict}"
    deserialized_object = type(serializable_object).parse_raw(json_string)
    assert isinstance(deserialized_object, type(serializable_object))
    assert deserialized_object == serializable_object
    return deserialized_object
