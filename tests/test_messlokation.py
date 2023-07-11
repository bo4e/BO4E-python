import json
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.bo.messlokation import Messlokation
from bo4e.bo.zaehler import Zaehler
from bo4e.com.adresse import Adresse
from bo4e.com.dienstleistung import Dienstleistung
from bo4e.com.externereferenz import ExterneReferenz
from bo4e.com.geokoordinaten import Geokoordinaten
from bo4e.com.hardware import Hardware
from bo4e.com.katasteradresse import Katasteradresse
from bo4e.com.zaehlwerk import Zaehlwerk
from bo4e.enum.botyp import BoTyp
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.geraetetyp import Geraetetyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.zaehlerauspraegung import Zaehlerauspraegung
from bo4e.enum.zaehlertyp import Zaehlertyp


class TestMeLo:
    def test_serialisation_only_required_attributes(self) -> None:
        """
        Test serialisation of Messlokation only with required attributes
        """
        melo = Messlokation(
            messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
            sparte=Sparte.STROM,
        )
        assert melo.versionstruktur == "2", "versionstruktur was not automatically set"
        assert melo.bo_typ is BoTyp.MESSLOKATION, "boTyp was not automatically set"

        json_string = melo.model_dump_json(by_alias=True)
        json_dict = json.loads(json_string)

        assert "boTyp" in json_dict, "No camel case serialization"
        assert "messlokationsId" in json_dict, "No camel case serialization"

        deserialized_melo: Messlokation = Messlokation.model_validate_json(json_string)

        # check that `deserialized_malo.marktlokations_id` and `malo.marktlokations_id` have the same value
        # but are **not** the same object.
        assert deserialized_melo.messlokations_id == melo.messlokations_id
        assert deserialized_melo.messlokations_id is not melo.messlokations_id
        assert deserialized_melo.bo_typ is BoTyp.MESSLOKATION

    def test_serialization_required_and_optional_attributes(self) -> None:
        """
        Test serialisation of Messlokation with required attributes and optional attributes
        """

        melo = Messlokation(
            # required attributes
            messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
            sparte=Sparte.STROM,
            # optional attributes
            netzebene_messung=Netzebene.MSP,
            messgebietnr="664073",
            geraete=[
                Hardware(geraetetyp=Geraetetyp.INTELLIGENTES_MESSYSTEM, bezeichnung="intelligentes Messsystem"),
                Hardware(geraetetyp=Geraetetyp.MODEM, bezeichnung="56k Modem"),
            ],
            messdienstleistung=[
                Dienstleistung(
                    dienstleistungstyp=Dienstleistungstyp.AUSLESUNG_TAEGLICH_FERNAUSLESUNG,
                    bezeichnung="fernauslesung_taeglich",
                ),
                Dienstleistung(
                    dienstleistungstyp=Dienstleistungstyp.ENTSPERRUNG,
                    bezeichnung="entsperrung",
                ),
            ],
            messlokationszaehler=[
                Zaehler(
                    zaehlernummer="000111222",
                    sparte=Sparte.STROM,
                    zaehlerauspraegung=Zaehlerauspraegung.EINRICHTUNGSZAEHLER,
                    zaehlwerke=[
                        Zaehlwerk(
                            zaehlwerk_id="98765",
                            einheit=Mengeneinheit.KW,
                            richtung=Energierichtung.EINSP,
                            bezeichnung="my zaehlwerk",
                            obis_kennzahl="1-0:1.8.1",
                            wandlerfaktor=Decimal(0.95),
                        )
                    ],
                    zaehlertyp=Zaehlertyp.DREHSTROMZAEHLER,
                    tarifart=Tarifart.ZWEITARIF,
                    zaehlerkonstante=Decimal(0.9),
                    eichung_bis=datetime(2022, 1, 1, 0, 0, 0),
                    externe_referenzen=[ExterneReferenz(ex_ref_name="zaehler im anderen system", ex_ref_wert="7890")],
                    letzte_eichung=datetime(2019, 6, 30, 0, 0, 0),
                )
            ],
            grundzustaendiger_msb_codenr="9910125000002",
            messadresse=Adresse(postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"),
        )
        assert melo.versionstruktur == "2", "versionstruktur was not automatically set"
        assert melo.bo_typ == BoTyp.MESSLOKATION, "boTyp was not automatically set"

        json_string = melo.model_dump_json(by_alias=True)
        json_dict = json.loads(json_string)

        assert "boTyp" in json_dict, "No camel case serialization"
        assert "messlokationsId" in json_dict, "No camel case serialization"

        deserialized_melo: Messlokation = Messlokation.model_validate_json(json_string)

        assert deserialized_melo.messlokations_id == melo.messlokations_id
        assert deserialized_melo.messlokations_id is not melo.messlokations_id
        assert deserialized_melo.bo_typ is BoTyp.MESSLOKATION

    def test_missing_required_fields(self) -> None:
        """
        Test that the required attributes are checked in the deserialization.
        Therefore the required attribute `messlokations_id` is removed in the test data.
        """
        invalid_json_string = """
            {
                "boTyp": "MESSLOKATION",
                "messlokationszaehler": null,
                "katasterinformation": null,
                "messgebietnr": "664073",
                "messadresse":
                    {
                        "strasse": "Jahnalle",
                        "hausnummer": "1",
                        "postfach": null,
                        "postleitzahl": "04177",
                        "landescode": "DE",
                        "coErgaenzung": null,
                        "adresszusatz": null,
                        "ort": "Leipzig"
                    },
                "sparte": "STROM",
                "netzebeneMessung": "MSP",
                "grundzustaendigerMsbCodenr": null,
                "geraete": null,
                "externeReferenzen": [],
                "messdienstleistung": null,
                "geoadresse": null,
                "versionstruktur": "2",
                "grundzustaendigerMsbimCodenr": null
                }
                """

        with pytest.raises(ValidationError) as excinfo:
            Messlokation.model_validate_json(invalid_json_string)

        assert "messlokationsId" in str(excinfo.value)

    def test_address_validation(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Messlokation(
                messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
                sparte=Sparte.STROM,
                netzebene_messung=Netzebene.MSP,
                messadresse=Adresse(postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"),
                geoadresse=Geokoordinaten(
                    breitengrad=Decimal(52.52149200439453),
                    laengengrad=Decimal(13.404866218566895),
                ),
                katasterinformation=Katasteradresse(gemarkung_flur="hello", flurstueck="world"),
            )

        assert "More than one address information is given." in str(excinfo.value)

    def test_grundzustaendiger_x_codenr_validation(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Messlokation(
                messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
                sparte=Sparte.STROM,
                netzebene_messung=Netzebene.MSP,
                grundzustaendiger_msb_codenr="9904768000008",
                grundzustaendiger_msbim_codenr="test",
            )

        assert "More than one codenr is given." in str(excinfo.value)

    @pytest.mark.parametrize(
        "melo_id, is_valid",
        [
            ("DE00056266802AO6G56M11SN51G21M24S", True),
            ("FR00056266802AO6G56M11SN51G21M24S", True),
            ("XX00056266802AO6G56M11SN51G21M24S", False),
            ("0000056266802AO6G56M11SN51G21M24S", False),
            ("asdasd", False),
            ("   ", False),
            ("  asdasdasd ", False),
            ("keine melo id", False),
            (None, False),
            ("", False),
        ],
    )
    def test_id_validation(self, melo_id: str, is_valid: bool) -> None:
        def _instantiate_melo(melo_id: str) -> None:
            _ = Messlokation(
                messlokations_id=melo_id,
                sparte=Sparte.STROM,
                netzebene_messung=Netzebene.MSP,
            )

        if not is_valid:
            with pytest.raises(ValidationError):
                _instantiate_melo(melo_id)
        else:
            _instantiate_melo(melo_id)

    def test_extension_data(self) -> None:
        """
        tests the behaviour of the json extension data (`extra="allow"`)
        """
        melo = Messlokation(
            messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
            sparte=Sparte.STROM,
        )
        melo_json: Dict[str, Any] = melo.model_dump()
        melo_json["additional_key"] = "additional_value"
        deserialized_melo: Messlokation = Messlokation.model_validate(melo_json)
        assert isinstance(deserialized_melo, Messlokation)
        assert deserialized_melo.additional_key == "additional_value"  # type:ignore[attr-defined]
