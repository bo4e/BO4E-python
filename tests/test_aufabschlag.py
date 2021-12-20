from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.aufabschlag import AufAbschlag, AufAbschlagSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.preisstaffel import Preisstaffel, PreisstaffelSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_sigmoidparameter import example_sigmoidparameter  # type:ignore[import]


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
                    "aufAbschlagstyp": "ABSOLUT",
                    "aufAbschlagsziel": "GESAMTPREIS",
                    "einheit": "EUR",
                    "website": "foo.bar",
                    "gueltigkeitszeitraum": {
                        "startdatum": "2020-01-01T00:00:00+00:00",
                        "endzeitpunkt": None,
                        "einheit": None,
                        "enddatum": "2020-04-01T00:00:00+00:00",
                        "startzeitpunkt": None,
                        "dauer": None,
                    },
                    "staffeln": [
                        {
                            "einheitspreis": "40",
                            "sigmoidparameter": {"a": "1", "b": "2", "c": "3", "d": "4"},
                            "staffelgrenzeVon": "12.5",
                            "staffelgrenzeBis": "25",
                        },
                        {
                            "einheitspreis": "15",
                            "sigmoidparameter": None,
                            "staffelgrenzeVon": "2.5",
                            "staffelgrenzeBis": "40.5",
                        },
                    ],
                },
                id="maximal attributes",
            ),
            pytest.param(
                AufAbschlag(
                    bezeichnung="foo",
                    staffeln=[
                        Preisstaffel(
                            einheitspreis=Decimal(15.0),
                            staffelgrenze_von=Decimal(2.5),
                            staffelgrenze_bis=Decimal(40.5),
                        ),
                    ],
                ),
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
                            "einheitspreis": "15",
                            "sigmoidparameter": None,
                            "staffelgrenzeVon": "2.5",
                            "staffelgrenzeBis": "40.5",
                        },
                    ],
                },
                id="minimal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, aufabschlag, expected_json_dict):
        """
        Test de-/serialisation of AufAbschlag with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlag, AufAbschlagSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = AufAbschlag()

        assert "missing 2 required" in str(excinfo.value)

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
    def test_failing_validation_einheit_only_for_abschlagstyp_absolut(self, auf_abschlagstyp):
        with pytest.raises(ValueError) as excinfo:
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
