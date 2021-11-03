"""
Functions and classes related to case conversions in schemata.
"""
import re
from typing import Pattern

from marshmallow import Schema, post_dump, pre_load


def snake_to_lower_camel_case(string: str) -> str:
    """
    Converts the string s from snake_case to lowerCamelCase
    :param string: foo_bar
    :return: fooBar
    """
    # copied from https://marshmallow.readthedocs.io/en/stable/examples.html?highlight=case#inflection-camel-casing-keys
    parts = iter(string.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


_lower_camel_word_boundary_pattern: Pattern = re.compile("[^A-Z][A-Z]")


def lower_camel_to_snake_case(string: str) -> str:
    """
    Converts the string s from lowerCamelCase to snake_case
    :param string: fooBar
    :return: foo_bar
    """
    result = string
    for lower_upper in _lower_camel_word_boundary_pattern.findall(string):
        result = result.replace(lower_upper, lower_upper[0] + "_" + lower_upper[1])
    return result.lower()


_upper_camel_word_boundary_pattern: Pattern = re.compile("[A-Z][^A-Z]")


def upper_camel_to_snake_case(string: str) -> str:
    """
    Converts the string s from UpperCamel to snake_case
    :param string: FooBar
    :return: foo_bar
    """
    result = string
    for upper_lower in _upper_camel_word_boundary_pattern.findall(string):
        result = result.replace(upper_lower, upper_lower[0].lower() + "_" + upper_lower[1])
    return result


def to_snake_case(string: str) -> str:
    """
    Converts any string that is either lowerCamel or UpperCamel to snake_case
    :param string: fooBar or FooBar
    :return: foo_bar
    """
    result = lower_camel_to_snake_case(string)
    result = upper_camel_to_snake_case(result)
    return result


class CaseConverterSchema(Schema):
    """
    Schema that uses snake case for its internal representation and lowerCamelCase for external representation unless
    explicitly specified otherwise by using the data_key attribute.
    """

    def on_bind_field(self, field_name, field_obj):
        """
        if a data_key is not explicitly specified, then use the field name as lowerCamelCase
        :param field_name:
        :param field_obj:
        :return:
        """
        field_obj.data_key = field_obj.data_key or to_snake_case(field_name)

    @pre_load
    # pylint:disable=unused-argument
    def convert_keys_to_snake_case(self, data, many, **kwargs):
        """
        Converts all the keys of data to snake_case.
        :param data:
        :param many:
        :param kwargs:
        :return:
        """
        for external_key in list(data.keys()):
            internal_key = to_snake_case(external_key)
            if internal_key != external_key and internal_key in self.fields:
                data[internal_key] = data.pop(external_key)
        return data

    @post_dump(pass_many=True)
    def convert_keys_to_lower_camel(self, data, many, **kwargs):
        """
        Converts all the internal keys to lowerCamel keys
        :param data:
        :param many:
        :param kwargs:
        :return:
        """
        if many:
            return [self.convert_keys_to_lower_camel(d, many=False, **kwargs) for d in data]
        for internal_key in list(data.keys()):
            if internal_key in self.fields:
                external_key = snake_to_lower_camel_case(internal_key)
                if external_key != internal_key:
                    data[external_key] = data.pop(internal_key)
        return data
