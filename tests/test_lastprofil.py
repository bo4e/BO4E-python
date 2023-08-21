from typing import Dict, Any

import pytest
from pydantic import ValidationError

from bo4e.com.lastprofil import Lastprofil
from bo4e.com.tagesparameter import Tagesparameter
from bo4e.enum.profilart import Profilart
from bo4e.enum.profilverfahren import Profilverfahren
from tests.serialization_helper import assert_serialization_roundtrip

#: maximal example
example_lastprofil = Lastprofil(
    bezeichnung="foo",
    profilschar="foo2",
    verfahren=Profilverfahren.SYNTHETISCH,
    einspeisung=True,
    tagesparameter=Tagesparameter(
        klimazone="7624q",
        temperaturmessstelle="1234x",
        dienstanbieter="ZT1",
        herausgeber="BDEW",
    ),
    profilart=Profilart.ART_LASTPROFIL,
    herausgeber="BDEW",
)


class TestLastprofil:
    @pytest.mark.parametrize(
        "lastprofil, expected_json_dict",
        [
            pytest.param(
                example_lastprofil,
                {
                    "bezeichnung": "foo",
                    "profilschar": "foo2",
                    "verfahren": Profilverfahren.SYNTHETISCH,
                    "einspeisung": True,
                    "tagesparameter": {
                        "klimazone": "7624q",
                        "temperaturmessstelle": "1234x",
                        "dienstanbieter": "ZT1",
                        "herausgeber": "BDEW",
                    },
                    "profilart": Profilart.ART_LASTPROFIL,
                    "herausgeber": "BDEW",
                },
                id="max param test",
            ),
            pytest.param(
                Lastprofil(),
                {
                    "bezeichnung": None,
                    "profilschar": None,
                    "verfahren": None,
                    "einspeisung": None,
                    "tagesparameter": None,
                    "profilart": None,
                    "herausgeber": None,
                },
                id="min param test",
            ),
        ],
    )
    def test_serialization_roundtrip(self, lastprofil: Lastprofil, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Lastprofil with minimal attributes.
        """
        assert_serialization_roundtrip(lastprofil, expected_json_dict)

    @pytest.mark.parametrize(
        "profil_art",
        [
            pytest.param(
                Profilart.ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL,
                id="profilart tagesparm.abh.",
            ),
        ],
    )
    def test_failing_validation_tagesparameter_given_for_tagesparam_lastprofil(self, profil_art: Profilart) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Lastprofil(
                profilart=profil_art,
            )

        assert "Lastprofil depends on Tagesparameter. Tagesparameter not given." in str(excinfo.value)
