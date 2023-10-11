from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Ausschreibungslos, Preismodell, Rechnungslegung, Sparte, Vertragsform
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
    lieferstellen=[example_ausschreibungsdetail],
    gesamt_menge=example_menge,
    wunsch_mindestmenge=example_menge,
    wunsch_maximalmenge=example_menge,
    lieferzeitraum=example_zeitraum,
    wunsch_kuendingungsfrist=example_zeitraum,
    wunsch_zahlungsziel=example_zeitraum,
    wiederholungsintervall=example_zeitraum,
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
