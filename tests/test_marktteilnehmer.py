import jsons

from bo4e.bo.marktteilnehmer import Marktteilehmer
from bo4e.com.adresse import Adresse
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.marktrolle import Marktrolle
from bo4e.enum.rollencodetyp import Rollencodetyp


class TestMarktteilnehmer:
    def test_serialization(self):
        mt = Marktteilehmer(
            # required attributes of Marktteilnehmer only
            marktrolle=Marktrolle.DIENSTLEISTER,
            rollencodenummer="271828",
            rollencodetyp=Rollencodetyp.BDEW,
            # required attributes inherited from Geschaeftspartner
            name1="Elon",
            gewerbekennzeichnung=True,
            geschaeftspartnerrolle=Geschaeftspartnerrolle.DIENSTLEISTER,
            partneradresse=Adresse(
                strasse="Milkyway",
                hausnummer="42",
                postleitzahl="16181",
                ort="Andromeda-Nebel",
            ),
        )

        assert mt.versionstruktur == 2, "versionstruktur was not automatically set"
        assert mt.bo_typ == "MARKTTEILNEHMER", "boTyp was not automatically set"

        json_string = mt.dumps(
            strip_nulls=True,
            key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE,
            jdkwargs={"ensure_ascii": False},
        )

        assert (
            "boTyp" in json_string
        ), "No camel case serialization"  # camel case serialization
        assert (
            "marktrolle" in json_string
        ), "No camel case serialization"  # camel case serialization

        deserialized_malo: Marktteilehmer = Marktteilehmer.loads(
            json_string, key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE
        )

        assert mt.marktrolle == deserialized_malo.marktrolle
        assert mt.marktrolle is not deserialized_malo.marktrolle
