import pytest
from pydantic import ValidationError

from bo4e import Bilanzierungsmethode, Kundengruppe, Netzebene, PreisblattNetznutzung, Preisstatus, Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_preisposition import example_preisposition
from tests.test_zeitraum import example_zeitraum


class TestPreisblatt:
    @pytest.mark.parametrize(
        "preisblatt_netznutzung",
        [
            pytest.param(
                PreisblattNetznutzung(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=example_marktteilnehmer,
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
