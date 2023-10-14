from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import LastgangKompakt, Lokationstyp, Mengeneinheit, Sparte, Tagesvektor, Zeiteinheit, Zeitintervall
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_tagesvektor import example_tagesvektor


class TestLastgangKompakt:
    @pytest.mark.parametrize(
        "lastgang_kompakt",
        [
            pytest.param(
                LastgangKompakt(
                    version="1.1",
                    sparte=Sparte.STROM,
                    lokations_id="DE0000011111222223333344444555556",
                    obis_kennzahl="1-0:1.8.1",
                    lokationstyp=Lokationstyp.MELO,
                    messgroesse=Mengeneinheit.KWH,
                    zeitintervall=Zeitintervall(),
                    tagesvektoren=[Tagesvektor()],
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, lastgang_kompakt: LastgangKompakt) -> None:
        """
        Test de-/serialisation of LastgangKompakt.
        """
        assert_serialization_roundtrip(lastgang_kompakt)
