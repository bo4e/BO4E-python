from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.aufabschlag import AufAbschlag
from bo4e.com.preisstaffel import Preisstaffel
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_sigmoidparameter import example_sigmoidparameter

example_aufabschlag = AufAbschlag(
    bezeichnung="foo",
    staffeln=[
        Preisstaffel(
            einheitspreis=Decimal(15.0),
            staffelgrenze_von=Decimal(2.5),
            staffelgrenze_bis=Decimal(40.5),
        ),
    ],
)


class TestAufAbschlag:
    @pytest.mark.parametrize(
        "aufabschlag, expected_json_dict",
        [
            pytest.param(
                AufAbschlag(
                    bezeichnung="foo",
                    beschreibung="bar",
                    auf_abschlagstyp=AufAbschlagstyp.ABSOLUT,
                    auf_abschlagsziel=AufAbschlagsziel.GESAMTPREIS,
                    einheit=Waehrungseinheit.EUR,
                    website="foo.bar",
                    gueltigkeitszeitraum=Zeitraum(
                        startdatum=datetime(2020, 1, 1, tzinfo=timezone.utc),
                        enddatum=datetime(2020, 4, 1, tzinfo=timezone.utc),
                    ),
                    staffeln=[
                        Preisstaffel(
                            einheitspreis=Decimal(40.0),
                            staffelgrenze_von=Decimal(12.5),
                            staffelgrenze_bis=Decimal(25.0),
                            sigmoidparameter=example_sigmoidparameter,
                        ),
                        Preisstaffel(
                            einheitspreis=Decimal(15.0),
                            staffelgrenze_von=Decimal(2.5),
                            staffelgrenze_bis=Decimal(40.5),
                        ),
                    ],
                ),
                {
                    "bezeichnung": "foo",
                    "beschreibung": "bar",
                    "aufAbschlagstyp": AufAbschlagstyp.ABSOLUT,
                    "aufAbschlagsziel": AufAbschlagsziel.GESAMTPREIS,
                    "einheit": Waehrungseinheit.EUR,
                    "website": "foo.bar",
                    "gueltigkeitszeitraum": {
                        "startdatum": datetime(2020, 1, 1, 0, 0, tzinfo=timezone.utc),
                        "endzeitpunkt": None,
                        "einheit": None,
                        "enddatum": datetime(2020, 4, 1, 0, 0, tzinfo=timezone.utc),
                        "startzeitpunkt": None,
                        "dauer": None,
                    },
                    "staffeln": [
                        {
                            "einheitspreis": Decimal("40"),
                            "sigmoidparameter": {
                                "A": Decimal("1"),
                                "B": Decimal("2"),
                                "C": Decimal("3"),
                                "D": Decimal("4"),
                            },
                            "staffelgrenzeVon": Decimal("12.5"),
                            "staffelgrenzeBis": Decimal("25"),
                        },
                        {
                            "einheitspreis": Decimal("15"),
                            "sigmoidparameter": None,
                            "staffelgrenzeVon": Decimal("2.5"),
                            "staffelgrenzeBis": Decimal("40.5"),
                        },
                    ],
                },
                id="maximal attributes",
            ),
            pytest.param(
                example_aufabschlag,
                {
                    "bezeichnung": "foo",
                    "beschreibung": None,
                    "aufAbschlagstyp": None,
                    "aufAbschlagsziel": None,
                    "einheit": None,
                    "website": None,
                    "gueltigkeitszeitraum": None,
                    "staffeln": [
                        {
                            "einheitspreis": Decimal("15"),
                            "sigmoidparameter": None,
                            "staffelgrenzeVon": Decimal("2.5"),
                            "staffelgrenzeBis": Decimal("40.5"),
                        },
                    ],
                },
                id="minimal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, aufabschlag: AufAbschlag, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of AufAbschlag with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlag, expected_json_dict)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = AufAbschlag()  # type: ignore[call-arg]

        assert "2 validation errors" in str(excinfo.value)

    @pytest.mark.parametrize(
        "auf_abschlagstyp",
        [
            pytest.param(
                AufAbschlagstyp.RELATIV,
                id="auf_abschlagstyp not absolute",
            ),
            pytest.param(
                None,
                id="auf_abschlagstyp not there",
            ),
        ],
    )
    def test_failing_validation_einheit_only_for_abschlagstyp_absolut(self, auf_abschlagstyp: AufAbschlagstyp) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = AufAbschlag(
                bezeichnung="foo",
                staffeln=[
                    Preisstaffel(
                        einheitspreis=Decimal(15.0),
                        staffelgrenze_von=Decimal(2.5),
                        staffelgrenze_bis=Decimal(40.5),
                    ),
                ],
                einheit=Waehrungseinheit.EUR,
                auf_abschlagstyp=auf_abschlagstyp,
            )

        assert "Only state einheit if auf_abschlagstyp is absolute." in str(excinfo.value)
