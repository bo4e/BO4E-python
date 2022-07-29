import json

from bo4e.bo.marktteilnehmer import Marktteilnehmer
from bo4e.com.adresse import Adresse
from bo4e.enum.botyp import BoTyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.marktrolle import Marktrolle
from bo4e.enum.rollencodetyp import Rollencodetyp
from bo4e.enum.sparte import Sparte

example_marktteilnehmer = Marktteilnehmer(
    # required attributes of Marktteilnehmer only
    marktrolle=Marktrolle.DL,
    rollencodenummer="9903916000000",
    rollencodetyp=Rollencodetyp.BDEW,
    sparte=Sparte.STROM,
    # required attributes inherited from Geschaeftspartner
    name1="Netze BW GmbH",
    gewerbekennzeichnung=True,
    geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
    partneradresse=Adresse(
        strasse="Schelmenwasenstraße",
        hausnummer="15",
        postleitzahl="70567",
        ort="Stuttgart",
    ),
)


class TestMarktteilnehmer:
    def test_serialization(self) -> None:
        mt = example_marktteilnehmer

        assert mt.versionstruktur == "2", "versionstruktur was not automatically set"
        assert mt.bo_typ == BoTyp.MARKTTEILNEHMER, "boTyp was not automatically set"

        json_string = mt.json(by_alias=True, ensure_ascii=False)
        json_dict = json.loads(json_string)

        # Test camelcase
        assert "boTyp" in json_dict
        assert "marktrolle" in json_dict

        deserialized_mt: Marktteilnehmer = Marktteilnehmer.parse_raw(json_string)

        assert mt.marktrolle is deserialized_mt.marktrolle
        # Test snakecase
        assert deserialized_mt.bo_typ is BoTyp.MARKTTEILNEHMER
