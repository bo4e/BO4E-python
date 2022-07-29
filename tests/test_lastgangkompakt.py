from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.bo.lastgang import LastgangKompakt
from bo4e.com.zeitintervall import Zeitintervall
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from bo4e.enum.zeiteinheit import Zeiteinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_tagesvektor import example_tagesvektor, example_tagesvektor_json


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
                    "sparte": Sparte.STROM,
                    "lokationstyp": Lokationstyp.MELO,
                    "messgroesse": Mengeneinheit.KWH,
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
    def test_serialization_roundtrip(
        self, lastgang_kompakt: LastgangKompakt, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of LastgangKompakt.
        """
        assert_serialization_roundtrip(lastgang_kompakt, expected_json_dict)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = LastgangKompakt()  # type: ignore[call-arg]

        assert "6 validation errors" in str(excinfo.value)
