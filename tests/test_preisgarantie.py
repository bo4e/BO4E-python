import pytest

from bo4e import Preisgarantie, Preisgarantietyp, Zeitspanne
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreisgarantie:
    @pytest.mark.parametrize(
        "preisgarantie",
        [
            pytest.param(
                Preisgarantie(preisgarantietyp=Preisgarantietyp.NUR_ENERGIEPREIS, zeitliche_gueltigkeit=Zeitspanne()),
            )
        ],
    )
    def test_preisgarantie_required_attributes(self, preisgarantie: Preisgarantie) -> None:
        """
        Test de-/serialisation of Preisgarantie with minimal attributes.
        """
        assert_serialization_roundtrip(preisgarantie)
