from stringcase import camelcase, snakecase
from marshmallow import pre_load, post_dump


class JavaScriptMixin:
    @pre_load
    def to_snakecase(self, data, **kwargs):
        return {snakecase(key): value for key, value in data.items()}

    @post_dump
    def to_camelcase(self, data, **kwargs):
        return {camelcase(key): value for key, value in data.items()}