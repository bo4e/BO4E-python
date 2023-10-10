from typing import Any, Dict

from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.zusatzattribut import ZusatzAttribut


class TestZusatzAttribut:
    def test_serialization(self) -> None:
        za = ZusatzAttribut(name="HOCHFREQUENZ_HFSAP_100", wert="12345")

        za_json = za.model_dump_json(by_alias=True)

        assert "name" in za_json

        deserialized_er: ZusatzAttribut = ZusatzAttribut.model_validate_json(za_json)
        assert isinstance(deserialized_er, ZusatzAttribut)
        assert deserialized_er == za

    def test_list_of_zusatz_attribut(self) -> None:
        gp = Geschaeftspartner(
            zusatz_attribute=[
                ZusatzAttribut(name="SAP GP Nummer", wert="0123456789"),
                ZusatzAttribut(name="Schufa-ID", wert="aksdlakoeuhn"),
            ],
            # just some dummy data to make the GP valid
            name1="Duck",
            name2="Donald",
            ist_gewerbe=False,
            geschaeftspartnerrolle=[Geschaeftspartnerrolle.KUNDE],
            partneradresse=Adresse(
                strasse="Am Geldspeicher",
                hausnummer="17",
                postleitzahl="88101",
                ort="Entenhausen",
            ),
        )

        gp_json = gp.model_dump_json(by_alias=True)

        deserialized_gp: Geschaeftspartner = Geschaeftspartner.model_validate_json(gp_json)
        assert len(deserialized_gp.zusatz_attribute) == 2
        assert deserialized_gp.zusatz_attribute[0].name == "SAP GP Nummer"

    def test_geschaeftspartner_with_no_externe_referenz(self) -> None:
        gp = Geschaeftspartner(
            # just some dummy data to make the GP valid
            name1="Duck",
            name2="Donald",
            ist_gewerbe=False,
            geschaeftspartnerrolle=[Geschaeftspartnerrolle.KUNDE],
            partneradresse=Adresse(
                strasse="Am Geldspeicher",
                hausnummer="17",
                postleitzahl="88101",
                ort="Entenhausen",
            ),
        )

        gp_json = gp.model_dump_json(by_alias=True)

        deserialized_gp: Geschaeftspartner = Geschaeftspartner.model_validate_json(gp_json)

        assert deserialized_gp.zusatz_attribute is None
