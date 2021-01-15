from bo4e.com.katasteradresse import Katasteradresse, KatasteradresseSchema


class TestKatasteradresse:
    def test_serialization(self):
        ka = Katasteradresse(gemarkung_flur="hello", flurstueck="world")

        schema = KatasteradresseSchema()

        json_string = schema.dumps(ka, ensure_ascii=False)

        assert "gemarkungFlur" in json_string, "No camel case serialization"

        deserialized_ka: Katasteradresse = schema.loads(json_string)

        assert ka.gemarkung_flur == deserialized_ka.gemarkung_flur
