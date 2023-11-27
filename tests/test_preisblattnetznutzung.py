import pytest

from bo4e import (
    Bilanzierungsmethode,
    Kundengruppe,
    Marktteilnehmer,
    Netzebene,
    PreisblattNetznutzung,
    Preisposition,
    Preisstatus,
    Sparte,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreisblatt:
    @pytest.mark.parametrize(
        "preisblatt_netznutzung",
        [
            pytest.param(
                PreisblattNetznutzung(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[Preisposition()],
                    gueltigkeit=Zeitraum(),
                    herausgeber=Marktteilnehmer(),
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    netzebene=Netzebene.MSP,
                    kundengruppe=Kundengruppe.SLP_G_GKO,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_netznutzung: PreisblattNetznutzung) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_netznutzung)
