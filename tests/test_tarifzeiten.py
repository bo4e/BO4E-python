from datetime import date

import pytest

from bo4e import Marktteilnehmer
from bo4e.bo.tarifzeiten import Tarifzeiten
from bo4e.com.tarifzeitenzeitscheibe import TarifzeitenZeitscheibe
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifzeiten:
    @pytest.mark.parametrize(
        "tarifzeiten",
        [
            pytest.param(
                Tarifzeiten(
                    marktteilnehmer=Marktteilnehmer(),
                    zeitscheiben=[TarifzeitenZeitscheibe()],
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifzeiten: Tarifzeiten) -> None:
        """
        Test de-/serialisation of Tarifzeit.
        """
        assert_serialization_roundtrip(tarifzeiten)
