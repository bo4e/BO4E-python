import json

import pytest  # type:ignore[import]

from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.adresse import Adresse
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart
from bo4e.enum.landescode import Landescode


class TestGeschaeftspartner:
    @pytest.mark.datafiles("./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json")
    def test_serializable(self, datafiles):
        with open(datafiles / "test_data_adresse_only_required_fields.json", encoding="utf-8") as json_file:
            address_test_data = json.load(json_file)

        gp = Geschaeftspartner(
            anrede=Anrede.FRAU,
            name1="von Sinnen",
            name2="Helga",
            name3=None,
            gewerbekennzeichnung=True,
            hrnummer="HRB 254466",
            amtsgericht="Amtsgericht München",
            kontaktweg=[Kontaktart.E_MAIL],
            umsatzsteuer_id="DE267311963",
            glaeubiger_id="DE98ZZZ09999999999",
            e_mail_adresse="test@bo4e.de",
            website="bo4e.de",
            geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
            partneradresse=Adresse(
                postleitzahl=address_test_data["postleitzahl"],
                ort=address_test_data["ort"],
                strasse=address_test_data["strasse"],
                hausnummer=address_test_data["hausnummer"],
            ),
        )

        # test default value for bo_typ in Geschaeftspartner
        assert gp.bo_typ == BoTyp.GESCHAEFTSPARTNER

        schema = GeschaeftspartnerSchema()

        gp_json = schema.dumps(gp, ensure_ascii=False)

        assert "Helga" in gp_json

        gp_deserialized = schema.loads(gp_json)

        assert gp_deserialized.bo_typ == gp.bo_typ
        assert type(gp_deserialized.partneradresse) == Adresse

    def test_optional_attribute_partneradresse(self):
        """
        The BO4E standard does not yet define whether the partneradresse is mandatory or not.
        We will set this as an optional argument until the standard is clear about it.

        This test checks whether the Geschaeftspartner can also be initialized without a partneradresse.
        """

        gp = Geschaeftspartner(
            anrede=Anrede.FRAU,
            name1="von Sinnen",
            name2="Helga",
            name3=None,
            gewerbekennzeichnung=True,
            hrnummer="HRB 254466",
            amtsgericht="Amtsgericht München",
            kontaktweg=[Kontaktart.E_MAIL],
            umsatzsteuer_id="DE267311963",
            glaeubiger_id="DE98ZZZ09999999999",
            e_mail_adresse="test@bo4e.de",
            website="bo4e.de",
            geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
        )

        schema = GeschaeftspartnerSchema()
        gp_json = schema.dumps(gp, ensure_ascii=False)
        gp_deserialized = schema.loads(gp_json)

        assert gp_deserialized.partneradresse is None

    def test_list_validation_of_geschaeftspartnerrolle(self):
        """
        Tests that if the geschaeftspartnerrolle of Geschaeftspartner is not a list, an error is raised.

        The attribute geschaeftspartnerrolle of Geschaeftspartner must be a list type.
        Therefore the list validator checks the type of geschaeftspartnerrolle
        during the initialization of Geschaeftspartner.
        """

        with pytest.raises(TypeError) as excinfo:
            _ = Geschaeftspartner(
                anrede=Anrede.FRAU,
                name1="von Sinnen",
                name2="Helga",
                name3=None,
                gewerbekennzeichnung=True,
                hrnummer="HRB 254466",
                amtsgericht="Amtsgericht München",
                kontaktweg=[Kontaktart.E_MAIL],
                umsatzsteuer_id="DE267311963",
                glaeubiger_id="DE98ZZZ09999999999",
                e_mail_adresse="test@bo4e.de",
                website="bo4e.de",
                geschaeftspartnerrolle=Geschaeftspartnerrolle.DIENSTLEISTER,
                partneradresse=Adresse(
                    postleitzahl="01069",
                    ort="Dresden",
                    strasse="Goethestraße",
                    hausnummer="1",
                ),
            )

        assert "must be typing.List" in str(excinfo.value)

    def test_serialization_of_non_german_address(self):
        """
        Test that partneradresses with a Landescode!=DE (default) are (de)serialized correctly.
        """
        gp = Geschaeftspartner(
            anrede=Anrede.FRAU,
            name1="Kurz",
            name2="Sebastian",
            name3=None,
            gewerbekennzeichnung=True,
            hrnummer="HRB 254466",
            amtsgericht="Amtsgericht Ibiza",
            kontaktweg=[Kontaktart.E_MAIL],
            umsatzsteuer_id="AT12345",
            geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
            partneradresse=Adresse(
                postleitzahl="1014", ort="Wien 1", strasse="Ballhausplatz", hausnummer="2", landescode=Landescode.AT
            ),
        )
        schema = GeschaeftspartnerSchema()
        gp_json = schema.dumps(gp, ensure_ascii=False)
        gp_deserialized = schema.loads(gp_json)
        assert gp_deserialized.partneradresse.landescode == Landescode.AT
