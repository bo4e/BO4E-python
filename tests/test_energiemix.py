from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.energieherkunft import Energieherkunft
from bo4e.com.energiemix import Energiemix
from bo4e.enum.erzeugungsart import Erzeugungsart
from bo4e.enum.oekolabel import Oekolabel
from bo4e.enum.oekozertifikat import Oekozertifikat
from bo4e.enum.sparte import Sparte
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
                    "anteil": [
                        {
                            "erzeugungsart": Erzeugungsart.BIOGAS,
                            "anteilProzent": Decimal("40"),
                        }
                    ],
                    "oekolabel": [],
                    "bemerkung": None,
                    "co2Emission": None,
                    "atommuell": None,
                    "website": None,
                    "oekozertifikate": [],
                    "oekoTopTen": None,
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
                    oeko_top_ten=True,
                ),
                {
                    "energiemixnummer": 2,
                    "energieart": Sparte.STROM,
                    "bezeichnung": "foo",
                    "gueltigkeitsjahr": 2021,
                    "anteil": [
                        {
                            "erzeugungsart": Erzeugungsart.BIOGAS,
                            "anteilProzent": Decimal("40"),
                        },
                        {
                            "erzeugungsart": Erzeugungsart.GEOTHERMIE,
                            "anteilProzent": Decimal("60"),
                        },
                    ],
                    "oekolabel": ["GASGREEN", "GRUENER_STROM_GOLD"],
                    "bemerkung": "bar",
                    "co2Emission": Decimal("40"),
                    "atommuell": Decimal("5"),
                    "website": "foobar.de",
                    "oekozertifikate": ["FRAUNHOFER", "FREIBERG"],
                    "oekoTopTen": True,
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

    def test_energiemix_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Energiemix()  # type: ignore[call-arg]

        assert "5 validation errors" in str(excinfo.value)

    def test_energiemix_anteil_required(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Energiemix(
                energiemixnummer=2,
                energieart=Sparte.STROM,
                bezeichnung="foo",
                gueltigkeitsjahr=2021,
                anteil=[],
            )

        assert "1 validation error" in str(excinfo.value)
        assert "too_short" in str(excinfo.value)
