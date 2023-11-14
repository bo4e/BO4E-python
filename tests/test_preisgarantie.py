from datetime import datetime, timezone

import pytest

from bo4e import Preisgarantie, Preisgarantietyp, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreisgarantie:
    @pytest.mark.parametrize(
        "preisgarantie",
        [
            pytest.param(
                Preisgarantie(
                    preisgarantietyp=Preisgarantietyp.NUR_ENERGIEPREIS,
                    zeitliche_gueltigkeit=Zeitraum(
                        startdatum=datetime(2020, 1, 1, tzinfo=timezone.utc),
                        enddatum=datetime(2020, 4, 1, tzinfo=timezone.utc),
                    ),
                ),
            ),
        ],
    )
    def test_preisgarantie_required_attributes(self, preisgarantie: Preisgarantie) -> None:
        """
        Test de-/serialisation of Preisgarantie with minimal attributes.
        """
        assert_serialization_roundtrip(preisgarantie)
