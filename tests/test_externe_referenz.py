from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.com.externereferenz import ExterneReferenz
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle


class TestExterneReferenz:
    def test_serialization(self) -> None:
        er = ExterneReferenz(ex_ref_name="HOCHFREQUENZ_HFSAP_100", ex_ref_wert="12345")

        er_json = er.json(by_alias=True, ensure_ascii=False)

        assert "exRefName" in er_json

        deserialized_er: ExterneReferenz = ExterneReferenz.parse_raw(er_json)
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

        gp_json = gp.json(by_alias=True, ensure_ascii=False)

        deserialized_gp: Geschaeftspartner = Geschaeftspartner.parse_raw(gp_json)
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

        gp_json = gp.json(by_alias=True, ensure_ascii=False)

        deserialized_gp: Geschaeftspartner = Geschaeftspartner.parse_raw(gp_json)

        assert deserialized_gp.externe_referenzen == []
