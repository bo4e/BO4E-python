import pytest  # type:ignore[import]

from bo4e.bo.lastgang import LastgangKompakt, LastgangKompaktSchema
from bo4e.com.zeitintervall import Zeitintervall
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from bo4e.enum.zeiteinheit import Zeiteinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_tagesvektor import example_tagesvektor, example_tagesvektor_json  # type:ignore[import]


class TestLastgangKompakt:
    @pytest.mark.parametrize(
        "lastgang_kompakt, expected_json_dict",
        [
            pytest.param(
                LastgangKompakt(
                    version="1.1",
                    sparte=Sparte.STROM,
                    lokations_id="DE0000011111222223333344444555556",
                    obis_kennzahl="1-0:1.8.1",
                    lokationstyp=Lokationstyp.MELO,
                    messgroesse=Mengeneinheit.KWH,
                    zeitintervall=Zeitintervall(
                        wert=1,
                        zeiteinheit=Zeiteinheit.VIERTEL_STUNDE,
                    ),
                    tagesvektoren=[example_tagesvektor],
                ),
                {
                    "version": "1.1",
                    "sparte": "STROM",
                    "lokationstyp": "MELO",
                    "messgroesse": "KWH",
                    "zeitintervall": {"zeiteinheit": "VIERTEL_STUNDE", "wert": 1},
                    "tagesvektoren": [example_tagesvektor_json],
                    "versionstruktur": "2",
                    "externeReferenzen": [],
                    "lokationsId": "DE0000011111222223333344444555556",
                    "boTyp": "LASTGANG_KOMPAKT",
                    "obisKennzahl": "1-0:1.8.1",
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, lastgang_kompakt: LastgangKompakt, expected_json_dict: dict):
        """
        Test de-/serialisation of LastgangKompakt.
        """
        assert_serialization_roundtrip(lastgang_kompakt, LastgangKompaktSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = LastgangKompakt()

        assert "missing 6 required" in str(excinfo.value)
