import pytest
import json
import jsons

from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.enum.anrede import Anrede
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart


class TestGeschaeftspartner:
    @pytest.mark.datafiles(
        "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json"
    )
    def test_serializable(self, datafiles):

        with open(
            datafiles / "test_data_adresse_only_required_fields.json", encoding="utf-8"
        ) as json_file:
            adress_test_data = json.load(json_file)

        gp = Geschaeftspartner(
            anrede=Anrede.FRAU,
            name1="Helga",
            name2="von",
            name3="Sinnen",
            gewerbekennzeichnung=True,
            hrnummer="HRB 254466",
            amtsgericht="Amtsgericht München",
            kontaktweg=Kontaktart.E_MAIL,
            umsatzsteuerId="DE267311963",
            glaeubigerId="DE98ZZZ09999999999",
            eMailAdresse="test@bo4e.de",
            website="bo4e.de",
            geschaeftspartnerrolle=Geschaeftspartnerrolle.DIENSTLEISTER,
            partneradresse=Adresse(
                postleitzahl=adress_test_data["postleitzahl"],
                ort=adress_test_data["ort"],
                strasse=adress_test_data["strasse"],
                hausnummer=adress_test_data["hausnummer"],
            ),
        )

        # test default value for bo_typ in Geschaeftspartner
        assert gp.bo_typ == "GESCHAEFTSPARTNER"

        gp_json = gp.dumps(
            strip_nulls=True,
            key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE,
            jdkwargs={"ensure_ascii": False},
        )

        assert "Helga" in gp_json
