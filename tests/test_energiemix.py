from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Energieherkunft, Energiemix, Erzeugungsart, Oekolabel, Oekozertifikat, Sparte
from tests.serialization_helper import assert_serialization_roundtrip

example_energiemix = Energiemix(
    energiemixnummer=2,
    energieart=Sparte.STROM,
    bezeichnung="foo",
    gueltigkeitsjahr=2021,
    anteil=[Energieherkunft()],
)


class TestEnergiemix:
    @pytest.mark.parametrize(
        "energiemix",
        [
            pytest.param(
                Energiemix(
                    energiemixnummer=2,
                    energieart=Sparte.STROM,
                    bezeichnung="foo",
                    gueltigkeitsjahr=2021,
                    anteil=[
                        Energieherkunft(),
                        Energieherkunft(),
                    ],
                    oekolabel=[
                        Oekolabel.GASGREEN,
                        Oekolabel.GRUENER_STROM_GOLD,
                    ],
                    bemerkung="bar",
                    co2_emission=Decimal(40),
                    atommuell=Decimal(5),
                    website="foobar.de",
                    oekozertifikate=[Oekozertifikat.FRAUNHOFER, Oekozertifikat.FREIBERG],
                    ist_in_oeko_top_ten=True,
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_energiemix_serialization_roundtrip(self, energiemix: Energiemix) -> None:
        """
        Test de-/serialisation of Energiehermix with minimal attributes.
        """
        assert_serialization_roundtrip(energiemix)
