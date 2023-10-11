from datetime import datetime, timezone
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import (
    Gueltigkeitstyp,
    KriteriumWert,
    Preisgarantietyp,
    RegionaleGueltigkeit,
    RegionalePreisgarantie,
    Tarifregionskriterium,
    Zeitraum,
)
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
                        "kriteriumsWerte": [
                            {"kriterium": Tarifregionskriterium.POSTLEITZAHL, "wert": "01069", "_id": None}
                        ],
                        "_id": None,
                    },
                    "zeitlicheGueltigkeit": {
                        "startdatum": None,
                        "einheit": None,
                        "enddatum": None,
                        "dauer": None,
                        "endzeitpunkt": datetime(2021, 7, 30, 0, 0, tzinfo=timezone.utc),
                        "startzeitpunkt": datetime(2011, 2, 5, 16, 43, tzinfo=timezone.utc),
                        "_id": None,
                    },
                    "_id": None,
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
