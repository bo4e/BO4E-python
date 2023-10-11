from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import (
    Ausschreibungsdetail,
    Ausschreibungslos,
    Menge,
    Preismodell,
    Rechnungslegung,
    Sparte,
    Vertragsform,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_ausschreibungsdetail import example_ausschreibungsdetail, example_ausschreibungsdetail_dict
from tests.test_menge import example_menge, example_menge_dict
from tests.test_zeitraum import example_zeitraum, example_zeitraum_dict

example_ausschreibungslos = Ausschreibungslos(
    losnummer="foo",
    bezeichnung="bar",
    bemerkung="asd",
    preismodell=Preismodell.FESTPREIS,
    energieart=Sparte.STROM,
    wunsch_rechnungslegung=Rechnungslegung.MONATSRECHN,
    wunsch_vertragsform=Vertragsform.DIREKT,
    betreut_durch="Max Mustermann",
    anzahl_lieferstellen=17,
    lieferstellen=[Ausschreibungsdetail()],
    gesamt_menge=Menge(),
    wunsch_mindestmenge=Menge(),
    wunsch_maximalmenge=Menge(),
    lieferzeitraum=Zeitraum(),
    wunsch_kuendingungsfrist=Zeitraum(),
    wunsch_zahlungsziel=Zeitraum(),
    wiederholungsintervall=Zeitraum(),
)


class TestAusschreibungslos:
    @pytest.mark.parametrize(
        "ausschreibungslos",
        [
            pytest.param(
                example_ausschreibungslos,
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, ausschreibungslos: Ausschreibungslos) -> None:
        """
        Test de-/serialisation of Ausschreibungslos
        """
        assert_serialization_roundtrip(ausschreibungslos)
