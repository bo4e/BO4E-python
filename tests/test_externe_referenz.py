import jsons

from bo4e.com.externereferenz import ExterneReferenz


class TestExterneReferenz:
    def test_serialization(self):
        er = ExterneReferenz(ex_ref_name="Hello", ex_ref_wert="World")

        er_json = er.dumps(
            strip_nulls=True,
            key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE,
            jdkwargs={"ensure_ascii": False},
        )

        assert "exRefName" in er_json

        deserialized_er: ExterneReferenz = ExterneReferenz.loads(
            er_json, key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE
        )
        assert isinstance(deserialized_er, ExterneReferenz)
        assert deserialized_er == er
