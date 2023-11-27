import pytest

from bo4e import (
    Bilanzierungsmethode,
    Dienstleistungstyp,
    Geraet,
    Marktteilnehmer,
    Netzebene,
    PreisblattHardware,
    Preisposition,
    Preisstatus,
    Sparte,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreisblattHardware:
    @pytest.mark.parametrize(
        "preisblatt_hardware",
        [
            pytest.param(
                PreisblattHardware(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[Preisposition()],
                    gueltigkeit=Zeitraum(),
                    herausgeber=Marktteilnehmer(),
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    messebene=Netzebene.MSP,
                    inklusive_dienstleistungen=[Dienstleistungstyp.AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB],
                    basisgeraet=Geraet(),
                    inklusive_geraete=[Geraet()],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_hardware: PreisblattHardware) -> None:
        """
        Test de-/serialisation Preisblatt-Hardware.
        """
        assert_serialization_roundtrip(preisblatt_hardware)
