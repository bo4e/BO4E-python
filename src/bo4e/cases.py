"""
Small module to convert snake_case to CamelCase and vice versa.
"""
# pylint: disable=unused-argument, no-self-use

from marshmallow import post_dump, pre_load
from stringcase import camelcase, snakecase


class JavaScriptMixin:
    """
    This class is used so that we always use snake_case in the Python world and
    CamelCase in the JSON (Javascript world).
    Its methods are executed before loading or after dumping a JSON string respectively.
    """

    @pre_load
    def to_snakecase(self, data, **kwargs):
        """ convert to snake_case """
        return {snakecase(key): value for key, value in data.items()}

    @post_dump
    def to_camelcase(self, data, **kwargs):
        """ convert to CamelCase """
        return {camelcase(key): value for key, value in data.items()}
