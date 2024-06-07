import pytest

from bo4e import (
    Gueltigkeitstyp,
    KriteriumWert,
    Preisgarantietyp,
    RegionaleGueltigkeit,
    RegionalePreisgarantie,
    Tarifregionskriterium,
    Zeitspanne,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestRegionalePreisgarantie:
    @pytest.mark.parametrize(
        "regionale_preisgarantie",
        [
            pytest.param(
                RegionalePreisgarantie(
                    preisgarantietyp=Preisgarantietyp.NUR_ENERGIEPREIS,
                    zeitliche_gueltigkeit=Zeitspanne(),
                    regionale_gueltigkeit=RegionaleGueltigkeit(
                        gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
                        kriteriums_werte=[KriteriumWert(kriterium=Tarifregionskriterium.POSTLEITZAHL, wert="01069")],
                    ),
                ),
            ),
        ],
    )
    def test_regionale_preisgarantie_serialization_roundtrip(
        self, regionale_preisgarantie: RegionalePreisgarantie
    ) -> None:
        """
        Test de-/serialisation of RegionalePreisgarantie with minimal attributes.
        """
        assert_serialization_roundtrip(regionale_preisgarantie)
