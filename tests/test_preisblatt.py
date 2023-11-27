import pytest

from bo4e import Marktteilnehmer, Preisblatt, Preisposition, Preisstatus, Sparte, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreisblatt:
    @pytest.mark.parametrize(
        "preisblatt",
        [
            pytest.param(
                Preisblatt(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[Preisposition()],
                    gueltigkeit=Zeitraum(),
                    herausgeber=Marktteilnehmer(),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt: Preisblatt) -> None:
        """
        Test de-/serialisation of Preisblatt.
        """
        assert_serialization_roundtrip(preisblatt)
