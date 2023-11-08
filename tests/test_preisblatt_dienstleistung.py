import pytest
from pydantic import ValidationError

from bo4e import (
    Bilanzierungsmethode,
    Dienstleistungstyp,
    Geraeteeigenschaften,
    Marktteilnehmer,
    PreisblattDienstleistung,
    Preisposition,
    Preisstatus,
    Sparte,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_zeitraum import example_zeitraum


class TestPreisblattDienstleistung:
    @pytest.mark.parametrize(
        "preisblatt_dienstleistung",
        [
            pytest.param(
                PreisblattDienstleistung(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[Preisposition()],
                    gueltigkeit=example_zeitraum,
                    herausgeber=Marktteilnehmer(),
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    basisdienstleistung=Dienstleistungstyp.ABLESUNG_MONATLICH,
                    inklusive_dienstleistungen=[Dienstleistungstyp.AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB],
                    geraetedetails=Geraeteeigenschaften(),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_dienstleistung: PreisblattDienstleistung) -> None:
        """
        Test de-/serialisation Preisblatt-Dienstleistung.
        """
        assert_serialization_roundtrip(preisblatt_dienstleistung)
