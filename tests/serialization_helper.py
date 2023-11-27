"""
A module that simplifies assertions for json serialization
"""
from typing import Any, Dict, Optional, TypeVar

from dictdiffer import diff  # type:ignore[import-not-found]
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def assert_serialization_roundtrip(serializable_object: T, expected_json_dict: Optional[Dict[str, Any]] = None) -> T:
    """
    Serializes the serializable_object using the provided schema,
    then asserts, that the result is equal to the expected_json_dict (if given),
    then deserializes the dictionary again and asserts the equality with the original serializable_object
    :returns the deserialized_object
    """
    json_string = serializable_object.model_dump_json(by_alias=True)
    assert json_string is not None
    actual_json_dict = serializable_object.model_dump(by_alias=True)
    assert actual_json_dict is not None

    def _remove_version_recursive_iter(value: dict[str, Any] | list[Any]) -> None:
        if isinstance(value, dict):
            value.pop("_version", None)
            for v in value.values():
                _remove_version_recursive_iter(v)
        elif isinstance(value, list):
            for v in value:
                _remove_version_recursive_iter(v)

    _remove_version_recursive_iter(actual_json_dict)
    # TODO: serializable_object.dict()
    if expected_json_dict is not None:
        assert all([(k in json_string) for k in expected_json_dict.keys()])
        assert actual_json_dict == expected_json_dict, (
            f"actual_json_dict != expected_json_dict\n\t" f"diff = {list(diff(expected_json_dict, actual_json_dict))}"
        )
        # this (diff(...)) contains the difference between two dicts -> just for easier debugging

    deserialized_object = type(serializable_object).model_validate_json(json_string)
    assert isinstance(deserialized_object, type(serializable_object))
    assert deserialized_object == serializable_object
    return deserialized_object
