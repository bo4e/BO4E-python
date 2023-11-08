import pytest
from pydantic import ValidationError

from bo4e import Marktteilnehmer, Preisblatt, Preisposition, Preisstatus, Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_zeitraum import example_zeitraum


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
                    gueltigkeit=example_zeitraum,
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
