from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.adresse import Adresse
from bo4e.com.externereferenz import ExterneReferenz, ExterneReferenzSchema
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle


class TestExterneReferenz:
    def test_serialization(self):
        er = ExterneReferenz(ex_ref_name="HOCHFREQUENZ_HFSAP_100", ex_ref_wert="12345")

        schema = ExterneReferenzSchema()

        er_json = schema.dumps(er, ensure_ascii=False)

        assert "exRefName" in er_json

        deserialized_er: ExterneReferenz = schema.loads(er_json)
        assert isinstance(deserialized_er, ExterneReferenz)
        assert deserialized_er == er

    def test_list_of_externe_referenz(self):
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

        schema = GeschaeftspartnerSchema()

        gp_json = schema.dumps(gp, ensure_ascii=False)

        deserialized_gp: Geschaeftspartner = schema.loads(gp_json)
        assert len(deserialized_gp.externe_referenzen) == 2
        assert deserialized_gp.externe_referenzen[0].ex_ref_name == "SAP GP Nummer"

    def test_geschaeftspartner_with_no_externe_referenz(self):
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

        schema = GeschaeftspartnerSchema()

        gp_json = schema.dumps(gp, ensure_ascii=False)

        deserialized_gp: Geschaeftspartner = schema.loads(gp_json)

        assert deserialized_gp.externe_referenzen == []
