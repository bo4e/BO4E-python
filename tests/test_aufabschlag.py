from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import AufAbschlag, AufAbschlagstyp, AufAbschlagsziel, Preisstaffel, Waehrungseinheit, Zeitraum
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
        "aufabschlag",
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
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, aufabschlag: AufAbschlag) -> None:
        """
        Test de-/serialisation of AufAbschlag with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlag)
