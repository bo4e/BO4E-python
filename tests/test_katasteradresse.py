import jsons

from bo4e.com.katasteradresse import Katasteradresse


class TestKatasteradresse:
    def test_serialization(self):
        ka = Katasteradresse(gemarkung_flur="hello", flurstueck="world")

        json_string = ka.dumps(
            strip_nulls=True,
            key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE,
            jdkwargs={"ensure_ascii": False},
        )

        assert "gemarkungFlur" in json_string, "No camel case serialization"

        deserialized_ka: Katasteradresse = Katasteradresse.loads(
            json_string, key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE
        )

        assert ka.gemarkung_flur == deserialized_ka.gemarkung_flur
