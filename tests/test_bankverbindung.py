import pytest

from bo4e import Bankverbindung
from tests.serialization_helper import assert_serialization_roundtrip


class TestBankverbindung:
    @pytest.mark.parametrize(
        "bankverbindung",
        [
            pytest.param(
                Bankverbindung(
                    iban="DE07123412341234123412",
                    kontoinhaber="Jürgen W.",
                    bankkennung="DEUTDEFF",
                    bankname="Deutsche Bank",
                ),
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, bankverbindung: Bankverbindung) -> None:
        """
        Test de-/serialisation of Ausschreibungslos
        """
        assert_serialization_roundtrip(bankverbindung)
