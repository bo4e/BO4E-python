from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.geraet import Geraet
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften
from bo4e.com.menge import Menge  # type:ignore[import]
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung, TarifeinschraenkungSchema
from bo4e.enum.geraetemerkmal import Geraetemerkmal
from bo4e.enum.geraetetyp import Geraetetyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.voraussetzungen import Voraussetzungen
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestTarifeinschraenkung:
    @pytest.mark.parametrize(
        "tarifeinschraenkung, expected_json_dict",
        [
            pytest.param(
                Tarifeinschraenkung(),
                {
                    "zusatzprodukte": None,
                    "voraussetzungen": None,
                    "einschraenkungzaehler": None,
                    "einschraenkungleistung": None,
                },
                id="minimal attributes",
            ),
            pytest.param(
                Tarifeinschraenkung(
                    zusatzprodukte=["foo", "bar"],
                    voraussetzungen=[Voraussetzungen.ALTVERTRAG, Voraussetzungen.DIREKTVERTRIEB],
                    einschraenkungzaehler=[
                        Geraet(
                            geraetenummer="0815",
                            geraeteeigenschaften=Geraeteeigenschaften(
                                geraetemerkmal=Geraetemerkmal.GAS_G1000,
                                geraetetyp=Geraetetyp.MULTIPLEXANLAGE,
                            ),
                        ),
                        Geraet(geraetenummer="197foo"),
                    ],
                    einschraenkungleistung=[
                        Menge(wert=Decimal(12.5), einheit=Mengeneinheit.MWH),
                        Menge(wert=Decimal(30), einheit=Mengeneinheit.KWH),
                    ],
                ),
                {
                    "zusatzprodukte": ["foo", "bar"],
                    "voraussetzungen": ["ALTVERTRAG", "DIREKTVERTRIEB"],
                    "einschraenkungzaehler": [
                        {
                            "geraetenummer": "0815",
                            "geraeteeigenschaften": {"geraetemerkmal": "GAS_G1000", "geraetetyp": "MULTIPLEXANLAGE"},
                        },
                        {
                            "geraetenummer": "197foo",
                            "geraeteeigenschaften": None,
                        },
                    ],
                    "einschraenkungleistung": [
                        {
                            "wert": "12.5",
                            "einheit": "MWH",
                        },
                        {
                            "wert": "30",
                            "einheit": "KWH",
                        },
                    ],
                },
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifeinschraenkung: Tarifeinschraenkung, expected_json_dict: dict):
        """
        Test de-/serialisation of Tarifeinschraenkung
        """
        assert_serialization_roundtrip(tarifeinschraenkung, TarifeinschraenkungSchema(), expected_json_dict)
