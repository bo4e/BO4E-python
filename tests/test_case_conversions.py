from typing import Dict, Optional

import attr
import pytest  # type:ignore[import]
from marshmallow import fields, post_load

from bo4e.schemata.caseconverterschema import CaseConverterSchema, snake_to_lower_camel_case, to_snake_case


@attr.s(auto_attribs=True)
class MyClass:
    some_string: str
    an_integer: int
    something: Optional[dict]


class MySchema(CaseConverterSchema):
    some_string = fields.Str(required=True, allow_none=False)
    an_integer = fields.Integer(required=True, allow_none=False)
    something = fields.Dict(required=False, allow_none=True)

    @post_load
    def to_my_class(self, data, **kwargs) -> MyClass:
        return MyClass(**data)


class MySchemaWithDataKeys(CaseConverterSchema):
    """
    The data_key attribute always allows to override the default behaviour.
    """

    some_string = fields.Str(required=True, allow_none=False, data_key="stringy key")
    an_integer = fields.Integer(required=True, allow_none=False, data_key="intiBinty")
    something = fields.Dict(required=False, allow_none=True, data_key="Some_Thing")

    class Meta:
        model = MyClass

    @post_load
    def to_my_class(self, data, **kwargs) -> MyClass:
        return MyClass(**data)


class TestCaseConversion:
    """
    Test class to test the snake/UpperCamel/lowerCamel conversions
    """

    @pytest.mark.parametrize(
        "original, expected",
        [
            pytest.param("foo", "foo"),
            pytest.param("foo_bar", "foo_bar"),
            pytest.param("fooBar", "foo_bar"),
            pytest.param("FooBar", "foo_bar"),
            pytest.param("Foo", "foo"),
            pytest.param("bo4e", "bo4e"),
            pytest.param("Bo4e", "bo4e"),
        ],
    )
    def test_to_snake(self, original: str, expected: str):
        """
        Tests the to_snake_case function
        :param original: input string
        :param expected: expected result
        :return:
        """
        actual = to_snake_case(original)
        assert actual == expected

    @pytest.mark.parametrize(
        "original, expected",
        [
            pytest.param("foo", "foo"),
            pytest.param("foo_bar", "fooBar"),
        ],
    )
    def test_to_lower_camel(self, original: str, expected: str):
        """
        Tests the to_lower_camel function
        :param original: input string
        :param expected: expected result
        :return:
        """
        actual = snake_to_lower_camel_case(original)
        assert actual == expected

    @pytest.mark.parametrize(
        "json_dict, expected",
        [
            pytest.param(
                {"some_string": "asd", "an_integer": 17, "something": None},
                MyClass(something=None, some_string="asd", an_integer=17),
            ),
            pytest.param(
                {"someString": "asd", "anInteger": 17, "something": None},
                MyClass(something=None, some_string="asd", an_integer=17),
            ),
            pytest.param(
                {"SomeString": "asd", "AnInteger": 17, "Something": None},
                MyClass(something=None, some_string="asd", an_integer=17),
            ),
        ],
    )
    def test_field_binding_on_load(self, json_dict: Dict[str, object], expected: MyClass):
        """
        Tests that the binding using the LowerCamelCaseSchema works
        :return:
        """
        schema = MySchema()
        actual: MyClass = schema.load(json_dict)
        assert actual == expected

    @pytest.mark.parametrize(
        "json_dict, expected",
        [
            pytest.param(
                {"stringy key": "asd", "intiBinty": 17, "Some_Thing": None},
                MyClass(something=None, some_string="asd", an_integer=17),
            )
        ],
    )
    def test_field_binding_on_load_with_data_keys(self, json_dict: Dict[str, object], expected: MyClass):
        """
        Tests that the binding using the LowerCamelCaseSchema works and the data_key parameter is taken into account.
        :return:
        """
        schema = MySchemaWithDataKeys()
        actual: MyClass = schema.load(json_dict)
        assert actual == expected

    @pytest.mark.parametrize(
        "instance, expected_dump",
        [
            pytest.param(
                MyClass(something=None, some_string="asd", an_integer=17),
                {"someString": "asd", "anInteger": 17, "something": None},
            ),
        ],
    )
    def test_key_conversion_on_dump(self, instance: MyClass, expected_dump: Dict[str, object]):
        """
        Tests that the dump using the LowerCamelCaseSchema works
        :return:
        """
        schema = MySchema()
        actual_dump: MyClass = schema.dump(instance)
        assert actual_dump == expected_dump

    @pytest.mark.parametrize(
        "instance, expected_dump",
        [
            pytest.param(
                MyClass(something=None, some_string="asd", an_integer=17),
                {"stringy key": "asd", "intiBinty": 17, "Some_Thing": None},
            ),
        ],
    )
    def test_key_conversion_on_dump_with_data_keys(self, instance: MyClass, expected_dump: Dict[str, object]):
        """
        Tests that the dump using the LowerCamelCaseSchema works and the data_key argument is taken into account.
        :return:
        """
        schema = MySchemaWithDataKeys()
        actual_dump: MyClass = schema.dump(instance)
        assert actual_dump == expected_dump
