from stringcase import camelcase, snakecase
from marshmallow import pre_load, post_dump


class JavaScriptMixin:
    """
    This class is used so that we always use snake_case in the Python world and CamelCase in the JSON (Javascript world).
    Its methods are executed before loading or after dumping a JSON string respectively.
    """

    @pre_load
    def to_snakecase(self, data, **kwargs):
        return {snakecase(key): value for key, value in data.items()}

    @post_dump
    def to_camelcase(self, data, **kwargs):
        return {camelcase(key): value for key, value in data.items()}
