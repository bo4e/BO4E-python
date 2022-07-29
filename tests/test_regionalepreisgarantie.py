from datetime import datetime, timezone
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit
from bo4e.com.regionalepreisgarantie import RegionalePreisgarantie
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.preisgarantietyp import Preisgarantietyp
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium
from tests.serialization_helper import assert_serialization_roundtrip

example_regionale_preisgarantie = RegionalePreisgarantie(
    preisgarantietyp=Preisgarantietyp.NUR_ENERGIEPREIS,
    zeitliche_gueltigkeit=Zeitraum(
        startzeitpunkt=datetime(2011, 2, 5, 16, 43, tzinfo=timezone.utc),
        endzeitpunkt=datetime(2021, 7, 30, tzinfo=timezone.utc),
    ),
    regionale_gueltigkeit=RegionaleGueltigkeit(
        gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
        kriteriums_werte=[KriteriumWert(kriterium=Tarifregionskriterium.POSTLEITZAHL, wert="01069")],
    ),
)


class TestRegionalePreisgarantie:
    @pytest.mark.parametrize(
        "regionale_preisgarantie, expected_json_dict",
        [
            pytest.param(
                example_regionale_preisgarantie,
                {
                    "beschreibung": None,
                    "preisgarantietyp": "NUR_ENERGIEPREIS",
                    "regionaleGueltigkeit": {
                        "gueltigkeitstyp": "NUR_IN",
                        "kriteriumsWerte": [{"kriterium": Tarifregionskriterium.POSTLEITZAHL, "wert": "01069"}],
                    },
                    "zeitlicheGueltigkeit": {
                        "startdatum": None,
                        "einheit": None,
                        "enddatum": None,
                        "dauer": None,
                        "endzeitpunkt": datetime(2021, 7, 30, 0, 0, tzinfo=timezone.utc),
                        "startzeitpunkt": datetime(2011, 2, 5, 16, 43, tzinfo=timezone.utc),
                    },
                },
                id="only required attributes",
            ),
        ],
    )
    def test_regionale_preisgarantie_serialization_roundtrip(
        self, regionale_preisgarantie: RegionalePreisgarantie, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of RegionalePreisgarantie with minimal attributes.
        """
        assert_serialization_roundtrip(regionale_preisgarantie, expected_json_dict)

    def test_regionalepreisgarantie_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = RegionalePreisgarantie()  # type: ignore[call-arg]

        assert "3 validation errors" in str(excinfo.value)
