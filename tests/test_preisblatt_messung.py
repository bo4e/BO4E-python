import pytest
from pydantic import ValidationError

from bo4e import (
    Bilanzierungsmethode,
    Dienstleistungstyp,
    Geraeteeigenschaften,
    Marktteilnehmer,
    Netzebene,
    PreisblattMessung,
    Preisposition,
    Preisstatus,
    Sparte,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreisblattMessung:
    @pytest.mark.parametrize(
        "preisblatt_messung",
        [
            pytest.param(
                PreisblattMessung(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[Preisposition()],
                    gueltigkeit=Zeitraum(),
                    herausgeber=Marktteilnehmer(),
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    messebene=Netzebene.MSP,
                    inklusive_dienstleistungen=[Dienstleistungstyp.AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB],
                    zaehler=Geraeteeigenschaften(),
                    inklusive_geraete=[Geraeteeigenschaften()],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_messung: PreisblattMessung) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_messung)
