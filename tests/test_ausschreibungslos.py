from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.ausschreibungslos import Ausschreibungslos
from bo4e.enum.preismodell import Preismodell
from bo4e.enum.rechnungslegung import Rechnungslegung
from bo4e.enum.sparte import Sparte
from bo4e.enum.vertragsform import Vertragsform
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
        "ausschreibungslos, expected_json_dict",
        [
            pytest.param(
                example_ausschreibungslos,
                {
                    "lieferzeitraum": example_zeitraum_dict,
                    "preismodell": Preismodell.FESTPREIS,
                    "energieart": Sparte.STROM,
                    "wiederholungsintervall": example_zeitraum_dict,
                    "bemerkung": "asd",
                    "bezeichnung": "bar",
                    "losnummer": "foo",
                    "anzahlLieferstellen": 17,
                    "lieferstellen": [example_ausschreibungsdetail_dict],
                    "wunschKuendingungsfrist": example_zeitraum_dict,
                    "wunschZahlungsziel": example_zeitraum_dict,
                    "gesamtMenge": example_menge_dict,
                    "wunschVertragsform": Vertragsform.DIREKT,
                    "wunschMaximalmenge": example_menge_dict,
                    "wunschRechnungslegung": Rechnungslegung.MONATSRECHN,
                    "wunschMindestmenge": example_menge_dict,
                    "betreutDurch": "Max Mustermann",
                },
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, ausschreibungslos: Ausschreibungslos, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Ausschreibungslos
        """
        assert_serialization_roundtrip(ausschreibungslos, expected_json_dict)

    def test_ausschreibungslos_lieferstellen_required(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Ausschreibungslos(
                losnummer="foo",
                bezeichnung="bar",
                bemerkung="asd",
                preismodell=Preismodell.FESTPREIS,
                energieart=Sparte.STROM,
                wunsch_rechnungslegung=Rechnungslegung.MONATSRECHN,
                wunsch_vertragsform=Vertragsform.DIREKT,
                betreut_durch="Max Mustermann",
                anzahl_lieferstellen=17,
                lieferzeitraum=example_zeitraum,
                ## ^^ above is just clutter
                lieferstellen=[],  # the important line
            )

        assert "1 validation error" in str(excinfo.value)
        assert "too_short" in str(excinfo.value)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Ausschreibungslos()  # type: ignore[call-arg]
        assert "10 validation errors" in str(excinfo.value)
