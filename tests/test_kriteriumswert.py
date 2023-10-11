from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import KriteriumWert, Tarifregionskriterium
from tests.serialization_helper import assert_serialization_roundtrip


class TestKriteriumWert:
    @pytest.mark.parametrize(
        "kriteriumwert, expected_json_dict",
        [
            pytest.param(
                KriteriumWert(
                    kriterium=Tarifregionskriterium.ORT,
                    wert="Grünwald",
                ),
                {"kriterium": Tarifregionskriterium.ORT, "wert": "Grünwald", "_id": None},
            ),
        ],
    )
    def test_kriteriumwert_serialization_roundtrip(
        self, kriteriumwert: KriteriumWert, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of KriteriumWert with minimal attributes.
        """
        assert_serialization_roundtrip(kriteriumwert, expected_json_dict)
