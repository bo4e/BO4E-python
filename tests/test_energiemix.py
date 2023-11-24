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
    anteil=[
        Energieherkunft(
            erzeugungsart=Erzeugungsart.BIOGAS,
            anteil_prozent=Decimal(40),
        ),
    ],
)


class TestEnergiemix:
    @pytest.mark.parametrize(
        "energiemix, expected_json_dict",
        [
            pytest.param(
                example_energiemix,
                {
                    "energiemixnummer": 2,
                    "energieart": Sparte.STROM,
                    "bezeichnung": "foo",
                    "gueltigkeitsjahr": 2021,
                    "anteil": [{"erzeugungsart": Erzeugungsart.BIOGAS, "anteilProzent": Decimal("40"), "_id": None}],
                    "oekolabel": None,
                    "bemerkung": None,
                    "co2Emission": None,
                    "atommuell": None,
                    "website": None,
                    "oekozertifikate": None,
                    "istInOekoTopTen": None,
                    "_id": None,
                },
                id="only required attributes",
            ),
            pytest.param(
                Energiemix(
                    energiemixnummer=2,
                    energieart=Sparte.STROM,
                    bezeichnung="foo",
                    gueltigkeitsjahr=2021,
                    anteil=[
                        Energieherkunft(
                            erzeugungsart=Erzeugungsart.BIOGAS,
                            anteil_prozent=Decimal(40),
                        ),
                        Energieherkunft(
                            erzeugungsart=Erzeugungsart.GEOTHERMIE,
                            anteil_prozent=Decimal(60),
                        ),
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
                {
                    "energiemixnummer": 2,
                    "energieart": Sparte.STROM,
                    "bezeichnung": "foo",
                    "gueltigkeitsjahr": 2021,
                    "anteil": [
                        {"erzeugungsart": Erzeugungsart.BIOGAS, "anteilProzent": Decimal("40"), "_id": None},
                        {"erzeugungsart": Erzeugungsart.GEOTHERMIE, "anteilProzent": Decimal("60"), "_id": None},
                    ],
                    "oekolabel": ["GASGREEN", "GRUENER_STROM_GOLD"],
                    "bemerkung": "bar",
                    "co2Emission": Decimal("40"),
                    "atommuell": Decimal("5"),
                    "website": "foobar.de",
                    "oekozertifikate": ["FRAUNHOFER", "FREIBERG"],
                    "istInOekoTopTen": True,
                    "_id": None,
                },
                id="required and optional attributes",
            ),
        ],
    )
    def test_energiemix_serialization_roundtrip(
        self, energiemix: Energiemix, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Energiehermix with minimal attributes.
        """
        assert_serialization_roundtrip(energiemix, expected_json_dict)
