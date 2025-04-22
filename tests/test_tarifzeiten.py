from datetime import date

import pytest

from bo4e import Marktteilnehmer, Zeitraum
from bo4e.bo.tarifzeiten import Tarifzeiten
from bo4e.com.tarifzeit import Tarifzeit
from bo4e.com.tarifzeitenzeitscheibe import TarifzeitenZeitscheibe
from bo4e.enum.tarifstufen import Tarifstufen
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifzeiten:
    @pytest.mark.parametrize(
        "tarifzeiten",
        [
            pytest.param(
                Tarifzeiten(
                    marktteilnehmer=Marktteilnehmer(),
                    zeitscheiben=[TarifzeitenZeitscheibe(
                        gueltigkeit=Zeitraum(
                            startdatum=date(2025, 1, 1),
                            enddatum=date(2025, 1, 31),
                        ),
                        tarifzeiten=[Tarifzeit(
                            zeitraum=Zeitraum(
                                startdatum=date(2025, 1, 1),
                                enddatum=date(2025, 1, 31),
                            ),
                            tarifstufe=Tarifstufen("HT"),
                        )])]
                )
            )

        ]
    )
    def test_serialization_roundtrip(self, tarifzeiten: Tarifzeiten) -> None:
        """
        Test de-/serialisation of Tarifzeit.
        """
        assert_serialization_roundtrip(tarifzeiten)
