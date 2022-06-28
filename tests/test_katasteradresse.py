from bo4e.com.katasteradresse import Katasteradresse


class TestKatasteradresse:
    def test_serialization(self) -> None:
        ka = Katasteradresse(gemarkung_flur="hello", flurstueck="world")

        json_string = ka.json(by_alias=True, ensure_ascii=False)

        assert "gemarkungFlur" in json_string, "No camel case serialization"

        deserialized_ka: Katasteradresse = Katasteradresse.parse_raw(json_string)

        assert ka.gemarkung_flur == deserialized_ka.gemarkung_flur
