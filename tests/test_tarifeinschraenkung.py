from decimal import Decimal
from typing import Any, Dict

import pytest

from bo4e import (
    Geraet,
    Geraeteeigenschaften,
    Geraetemerkmal,
    Geraetetyp,
    Menge,
    Mengeneinheit,
    Tarifeinschraenkung,
    Voraussetzungen,
)
from tests.serialization_helper import assert_serialization_roundtrip

example_tarifeinschraenkung = Tarifeinschraenkung(
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
)


class TestTarifeinschraenkung:
    @pytest.mark.parametrize(
        "tarifeinschraenkung",
        [
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
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifeinschraenkung: Tarifeinschraenkung) -> None:
        """
        Test de-/serialisation of Tarifeinschraenkung
        """
        assert_serialization_roundtrip(tarifeinschraenkung)
