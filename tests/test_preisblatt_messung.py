import pytest

from bo4e import Bilanzierungsmethode, Dienstleistungstyp, Netzebene, PreisblattMessung, Preisstatus, Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_geraet import example_geraet
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_preisposition import example_preisposition
from tests.test_zaehler import example_zaehler
from tests.test_zeitraum import example_zeitraum


class TestPreisblattMessung:
    @pytest.mark.parametrize(
        "preisblatt_messung",
        [
            pytest.param(
                PreisblattMessung(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=example_marktteilnehmer,
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    messebene=Netzebene.MSP,
                    inklusive_dienstleistungen=[Dienstleistungstyp.AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB],
                    zaehler=example_zaehler,
                    inklusive_geraete=[example_geraet],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_messung: PreisblattMessung) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_messung)
