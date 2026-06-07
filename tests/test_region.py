import pytest

from bo4e import Operator, Region, Regionskriterium, Regionsoperation
from tests.serialization_helper import assert_serialization_roundtrip


class TestRegion:
    @pytest.mark.parametrize(
        "region",
        [
            pytest.param(
                Region(
                    bezeichnung="Bikini Bottom",
                    beschreibung="Heimatort der Krabbencrew",
                    regionsoperationen=[
                        Regionsoperation(
                            regionsoperator=Operator.ADDITION,
                            prioritaet=0,
                            bezeichnung="Bikini Bottom",
                            regionskriterium=Regionskriterium.ORT,
                        ),
                    ],
                ),
                id="single regionsoperation",
            ),
            pytest.param(
                Region(
                    bezeichnung="NRW ohne Düsseldorf",
                    regionsoperationen=[
                        Regionsoperation(
                            regionsoperator=Operator.ADDITION,
                            prioritaet=0,
                            bezeichnung="NRW",
                            regionskriterium=Regionskriterium.BUNDESLAND_NAME,
                        ),
                        Regionsoperation(
                            regionsoperator=Operator.SUBTRAKTION,
                            prioritaet=1,
                            bezeichnung="Düsseldorf",
                            regionskriterium=Regionskriterium.ORT,
                        ),
                    ],
                ),
                id="combined regionsoperationen",
            ),
        ],
    )
    def test_serialization_roundtrip(self, region: Region) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(region)
