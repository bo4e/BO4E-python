from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import LastgangKompakt, Lokationstyp, Mengeneinheit, Sparte, Zeiteinheit, Zeitintervall
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
                    "zeitintervall": {"zeiteinheit": "VIERTEL_STUNDE", "wert": 1, "_id": None},
                    "tagesvektoren": [example_tagesvektor_json],
                    "externeReferenzen": None,
                    "lokationsId": "DE0000011111222223333344444555556",
                    "_typ": "LASTGANG_KOMPAKT",
                    "obisKennzahl": "1-0:1.8.1",
                    "_id": None,
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
