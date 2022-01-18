import pytest  # type:ignore[import]

from bo4e.com.ausschreibungslos import Ausschreibungslos, AusschreibungslosSchema
from bo4e.enum.preismodell import Preismodell
from bo4e.enum.rechnungslegung import Rechnungslegung
from bo4e.enum.sparte import Sparte
from bo4e.enum.vertragsform import Vertragsform
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_ausschreibungsdetail import (  # type:ignore[import]
    example_ausschreibungsdetail,
    example_ausschreibungsdetail_dict,
)
from tests.test_menge import example_menge, example_menge_dict  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum, example_zeitraum_dict  # type:ignore[import]


class TestAusschreibungslos:
    @pytest.mark.parametrize(
        "ausschreibungslos, expected_json_dict",
        [
            pytest.param(
                Ausschreibungslos(
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
                ),
                {
                    "lieferzeitraum": example_zeitraum_dict,
                    "preismodell": "FESTPREIS",
                    "energieart": "STROM",
                    "wiederholungsintervall": example_zeitraum_dict,
                    "bemerkung": "asd",
                    "bezeichnung": "bar",
                    "losnummer": "foo",
                    "anzahlLieferstellen": 17,
                    "lieferstellen": [example_ausschreibungsdetail_dict],
                    "wunschKuendingungsfrist": example_zeitraum_dict,
                    "wunschZahlungsziel": example_zeitraum_dict,
                    "gesamtMenge": example_menge_dict,
                    "wunschVertragsform": "DIREKT",
                    "wunschMaximalmenge": example_menge_dict,
                    "wunschRechnungslegung": "MONATSRECHN",
                    "wunschMindestmenge": example_menge_dict,
                    "betreutDurch": "Max Mustermann",
                },
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, ausschreibungslos, expected_json_dict):
        """
        Test de-/serialisation of Ausschreibungslos
        """
        assert_serialization_roundtrip(ausschreibungslos, AusschreibungslosSchema(), expected_json_dict)

    def test_ausschreibungslos_lieferstellen_required(self):
        with pytest.raises(ValueError) as excinfo:
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

        assert "List lieferstellen must not be empty." in str(excinfo.value)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Ausschreibungslos()
        assert "missing 10 required" in str(excinfo.value)
