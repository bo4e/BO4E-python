from datetime import datetime, timezone

import pytest  # type:ignore[import]

from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit
from bo4e.com.regionalepreisgarantie import RegionalePreisgarantie, RegionalePreisgarantieSchema
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.preisgarantietyp import Preisgarantietyp
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestRegionalePreisgarantie:
    @pytest.mark.parametrize(
        "regionale_preisgarantie, expected_json_dict",
        [
            pytest.param(
                RegionalePreisgarantie(
                    preisgarantietyp=Preisgarantietyp.NUR_ENERGIEPREIS,
                    zeitliche_gueltigkeit=Zeitraum(
                        startzeitpunkt=datetime(2011, 2, 5, 16, 43, tzinfo=timezone.utc),
                        endzeitpunkt=datetime(2021, 7, 30, tzinfo=timezone.utc),
                    ),
                    regionale_gueltigkeit=RegionaleGueltigkeit(
                        gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
                        kriteriums_werte=[KriteriumWert(kriterium=Tarifregionskriterium.POSTLEITZAHL, wert="01069")],
                    ),
                ),
                {
                    "beschreibung": None,
                    "preisgarantietyp": "NUR_ENERGIEPREIS",
                    "regionaleGueltigkeit": {
                        "gueltigkeitstyp": "NUR_IN",
                        "kriteriumsWerte": [{"kriterium": "POSTLEITZAHL", "wert": "01069"}],
                    },
                    "zeitlicheGueltigkeit": {
                        "startdatum": None,
                        "einheit": None,
                        "enddatum": None,
                        "dauer": None,
                        "endzeitpunkt": "2021-07-30T00:00:00+00:00",
                        "startzeitpunkt": "2011-02-05T16:43:00+00:00",
                    },
                },
                id="only required attributes",
            ),
        ],
    )
    def test_regionale_preisgarantie_serialization_roundtrip(self, regionale_preisgarantie, expected_json_dict):
        """
        Test de-/serialisation of RegionalePreisgarantie with minimal attributes.
        """
        assert_serialization_roundtrip(regionale_preisgarantie, RegionalePreisgarantieSchema(), expected_json_dict)

    def test_regionalepreisgarantie_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = RegionalePreisgarantie()

        assert "missing 3 required" in str(excinfo.value)
