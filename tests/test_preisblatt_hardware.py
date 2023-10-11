import pytest
from pydantic import ValidationError

from bo4e import (
    Bilanzierungsmethode,
    Dienstleistungstyp,
    Geraeteeigenschaften,
    Netzebene,
    PreisblattHardware,
    Preisstatus,
    Sparte,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_preisposition import example_preisposition
from tests.test_zeitraum import example_zeitraum


class TestPreisblattHardware:
    @pytest.mark.parametrize(
        "preisblatt_hardware",
        [
            pytest.param(
                PreisblattHardware(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=example_marktteilnehmer,
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    messebene=Netzebene.MSP,
                    inklusive_dienstleistungen=[Dienstleistungstyp.AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB],
                    basisgeraet=Geraeteeigenschaften(),  # TODO warum sind hier keine Gerate?
                    inklusive_geraete=[Geraeteeigenschaften()],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_hardware: PreisblattHardware) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_hardware)
