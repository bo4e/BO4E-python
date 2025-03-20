import pytest

from bo4e.com.lastprofil import Lastprofil
from bo4e.com.tagesparameter import Tagesparameter
from bo4e.enum.profilart import Profilart
from bo4e.enum.profilverfahren import Profilverfahren
from tests.serialization_helper import assert_serialization_roundtrip


class TestLastprofil:
    @pytest.mark.parametrize(
        "lastprofil",
        [
            pytest.param(
                Lastprofil(
                    bezeichnung="foo",
                    profilschar="foo2",
                    verfahren=Profilverfahren.SYNTHETISCH,
                    ist_einspeisung=True,
                    tagesparameter=Tagesparameter(
                        klimazone="7624q",
                        temperaturmessstelle="1234x",
                        dienstanbieter="ZT1",
                        herausgeber="BDEW",
                    ),
                    profilart=Profilart.ART_LASTPROFIL,
                    herausgeber="BDEW",
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, lastprofil: Lastprofil) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(lastprofil)
