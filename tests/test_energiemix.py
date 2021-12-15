from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.energieherkunft import Energieherkunft
from bo4e.com.energiemix import Energiemix, EnergiemixSchema
from bo4e.enum.erzeugungsart import Erzeugungsart
from bo4e.enum.oekolabel import Oekolabel
from bo4e.enum.oekozertifikat import Oekozertifikat
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestEnergiemix:
    @pytest.mark.parametrize(
        "energiemix, expected_json_dict",
        [
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
                    ],
                ),
                {
                    "energiemixnummer": 2,
                    "energieart": "STROM",
                    "bezeichnung": "foo",
                    "gueltigkeitsjahr": 2021,
                    "anteil": [
                        {
                            "erzeugungsart": "BIOGAS",
                            "anteilProzent": "40",
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
                    "energieart": "STROM",
                    "bezeichnung": "foo",
                    "gueltigkeitsjahr": 2021,
                    "anteil": [
                        {
                            "erzeugungsart": "BIOGAS",
                            "anteilProzent": "40",
                        },
                        {
                            "erzeugungsart": "GEOTHERMIE",
                            "anteilProzent": "60",
                        },
                    ],
                    "oekolabel": ["GASGREEN", "GRUENER_STROM_GOLD"],
                    "bemerkung": "bar",
                    "co2Emission": "40",
                    "atommuell": "5",
                    "website": "foobar.de",
                    "oekozertifikate": ["FRAUNHOFER", "FREIBERG"],
                    "oekoTopTen": True,
                },
                id="required and optional attributes",
            ),
        ],
    )
    def test_energiemix_serialization_roundtrip(self, energiemix, expected_json_dict):
        """
        Test de-/serialisation of Energiehermix with minimal attributes.
        """
        assert_serialization_roundtrip(energiemix, EnergiemixSchema(), expected_json_dict)

    def test_energiemix_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Energiemix()

        assert "missing 5 required" in str(excinfo.value)

    def test_energiemix_anteil_required(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Energiemix(
                energiemixnummer=2,
                energieart=Sparte.STROM,
                bezeichnung="foo",
                gueltigkeitsjahr=2021,
                anteil=[],
            )

        assert "List anteil must not be empty." in str(excinfo.value)
