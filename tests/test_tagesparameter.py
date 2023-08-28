from typing import Any, Dict

import pytest

from bo4e.com.tagesparameter import Tagesparameter
from tests.serialization_helper import assert_serialization_roundtrip

# full example
example_tagesparameter = Tagesparameter(
    klimazone="7624q",
    temperaturmessstelle="1234x",
    dienstanbieter="ZT1",
    herausgeber="BDEW",
)


class TestTagesparameter:
    #
    @pytest.mark.parametrize(
        "tagesparameter, expected_json_dict",
        [
            pytest.param(
                example_tagesparameter,
                {
                    "klimazone": "7624q",
                    "temperaturmessstelle": "1234x",
                    "dienstanbieter": "ZT1",
                    "herausgeber": "BDEW",
                },
                id="full example",
            ),
            pytest.param(
                Tagesparameter(),
                {
                    "klimazone": None,
                    "temperaturmessstelle": None,
                    "dienstanbieter": None,
                    "herausgeber": None,
                },
                id="min example",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tagesparameter: Tagesparameter, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Tagesparameter with maximal/minimal attributes.
        """
        assert_serialization_roundtrip(tagesparameter, expected_json_dict)
