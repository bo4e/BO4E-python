from typing import Any, Dict

from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.com.externereferenz import ExterneReferenz
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle


class TestExterneReferenz:
    def test_serialization(self) -> None:
        er = ExterneReferenz(ex_ref_name="HOCHFREQUENZ_HFSAP_100", ex_ref_wert="12345")

        er_json = er.model_dump_json(by_alias=True)

        assert "exRefName" in er_json

        deserialized_er: ExterneReferenz = ExterneReferenz.model_validate_json(er_json)
        assert isinstance(deserialized_er, ExterneReferenz)
        assert deserialized_er == er

    def test_list_of_externe_referenz(self) -> None:
        gp = Geschaeftspartner(
            externe_referenzen=[
                ExterneReferenz(ex_ref_name="SAP GP Nummer", ex_ref_wert="0123456789"),
                ExterneReferenz(ex_ref_name="Schufa-ID", ex_ref_wert="aksdlakoeuhn"),
            ],
            # just some dummy data to make the GP valid
            name1="Duck",
            name2="Donald",
            gewerbekennzeichnung=False,
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
        assert len(deserialized_gp.externe_referenzen) == 2  # type: ignore[arg-type]
        assert deserialized_gp.externe_referenzen[0].ex_ref_name == "SAP GP Nummer"  # type: ignore[index]

    def test_geschaeftspartner_with_no_externe_referenz(self) -> None:
        gp = Geschaeftspartner(
            # just some dummy data to make the GP valid
            name1="Duck",
            name2="Donald",
            gewerbekennzeichnung=False,
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

        assert deserialized_gp.externe_referenzen == []

    def test_extension_data(self) -> None:
        """
        tests the behaviour of the json extension data (`extra="allow"`)
        """
        er = ExterneReferenz(ex_ref_name="foo.bar", ex_ref_wert="12345")
        er_json: Dict[str, Any] = er.model_dump()
        er_json["additional_key"] = "additional_value"
        deserialized_er: ExterneReferenz = ExterneReferenz.model_validate(er_json)
        assert isinstance(deserialized_er, ExterneReferenz)
        assert deserialized_er.additional_key == "additional_value"  # type:ignore[attr-defined]
