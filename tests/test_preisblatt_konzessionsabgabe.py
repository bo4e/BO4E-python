import pytest
from pydantic import ValidationError

from bo4e import KundengruppeKA, Marktteilnehmer, PreisblattKonzessionsabgabe, Preisstatus, Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_preisposition import example_preisposition
from tests.test_zeitraum import example_zeitraum


class TestPreisblatt:
    @pytest.mark.parametrize(
        "preisblatt_ka",
        [
            pytest.param(
                PreisblattKonzessionsabgabe(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=Marktteilnehmer(),
                    kundengruppe_k_a=KundengruppeKA.G_SONDERKUNDE,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_ka: PreisblattKonzessionsabgabe) -> None:
        """
        Test de-/serialisation Preisblatt-Konzessionsabgabe.
        """
        assert_serialization_roundtrip(preisblatt_ka)
