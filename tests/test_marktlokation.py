from bo4e.bo.marktlokation import Marktlokation
from bo4e.com.adresse import Adresse
from bo4e.enum.sparte import Sparte


class TestMaLo:
    def test_serializable(self):
        malo = Marktlokation(
            marktlokations_id="54321012345",
            sparte=Sparte.GAS,
            lokationsadresse=Adresse(
                postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"
            ),
        )
        assert malo.versionstruktur == 1, "versionstruktur was not automatically set"
        assert malo.bo_typ == "MARKTLOKATION", "boTyp was not automatically set"

        json_string = malo.to_json()

        assert (
            "boTyp" in json_string
        ), "No camel case serialization"  # camel case serialization
        assert (
            "marktlokationsId" in json_string
        ), "No camel case serialization"  # camel case serialization

        deserialized_malo: Marktlokation = Marktlokation.from_json(json_string)

        assert malo.marktlokations_id == deserialized_malo.marktlokations_id
        assert malo.marktlokations_id is not deserialized_malo.marktlokations_id
