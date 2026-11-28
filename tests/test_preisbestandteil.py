from decimal import Decimal

import pytest

from bo4e import Preisbestandteil, Preisblatt, PreisblattMessung, PreisblattNetznutzung, PreisblattKonzessionsabgabe
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreisbestandteil:
    @pytest.mark.parametrize(
        "preisbestandteil",
        [
            pytest.param(
                Preisbestandteil(
                    steuern_umlagen=[Preisblatt()],
                    messung=[PreisblattMessung()],
                    netznutzung=[PreisblattNetznutzung()],
                    konzessionsabgabe=[PreisblattKonzessionsabgabe()],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisbestandteil: Preisbestandteil) -> None:
        """
        Test de-/serialisation of Preisbestandteil
        """
        assert_serialization_roundtrip(preisbestandteil)
