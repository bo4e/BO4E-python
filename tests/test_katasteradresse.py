from bo4e.com.katasteradresse import Katasteradresse


class TestKatasteradresse:
    def test_serialization(self) -> None:
        ka = Katasteradresse(gemarkung_flur="hello", flurstueck="world")

        json_string = ka.model_dump_json(by_alias=True)

        assert "gemarkungFlur" in json_string, "No camel case serialization"

        deserialized_ka: Katasteradresse = Katasteradresse.model_validate_json(json_string)

        assert ka.gemarkung_flur == deserialized_ka.gemarkung_flur
