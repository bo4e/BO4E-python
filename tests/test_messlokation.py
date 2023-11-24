import json
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import (
    Adresse,
    Dienstleistung,
    Dienstleistungstyp,
    Energierichtung,
    ExterneReferenz,
    Geraet,
    Geraeteklasse,
    Geraetetyp,
    Mengeneinheit,
    Messlokation,
    Netzebene,
    Registeranzahl,
    Sparte,
    Typ,
    Zaehler,
    Zaehlerauspraegung,
    Zaehlertyp,
    Zaehlwerk,
)


class TestMeLo:
    def test_serialisation_only_required_attributes(self) -> None:
        """
        Test serialisation of Messlokation only with required attributes
        """
        melo = Messlokation(
            messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
            sparte=Sparte.STROM,
        )
        assert melo.version is not None, "versionstruktur was not automatically set"
        assert melo.typ is Typ.MESSLOKATION, "_typ was not automatically set"

        json_string = melo.model_dump_json(by_alias=True)
        json_dict = json.loads(json_string)

        assert "_typ" in json_dict, "No camel case serialization"
        assert "messlokationsId" in json_dict, "No camel case serialization"

        deserialized_melo: Messlokation = Messlokation.model_validate_json(json_string)

        # check that `deserialized_malo.marktlokations_id` and `malo.marktlokations_id` have the same value
        # but are **not** the same object.
        assert deserialized_melo.messlokations_id == melo.messlokations_id
        assert deserialized_melo.messlokations_id is not melo.messlokations_id
        assert deserialized_melo.typ is Typ.MESSLOKATION

    def test_serialization_required_and_optional_attributes(self) -> None:
        """
        Test serialisation of Messlokation with required attributes and optional attributes
        """

        melo = Messlokation(
            messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
            sparte=Sparte.STROM,
            netzebene_messung=Netzebene.MSP,
            messgebietnr="664073",
            geraete=[
                Geraet(
                    geraetetyp=Geraetetyp.INTELLIGENTES_MESSYSTEM,
                    bezeichnung="intelligentes Messsystem",
                    geraetenummer="123",
                ),
                Geraet(
                    geraeteklasse=Geraeteklasse.WANDLER,
                    geraetetyp=Geraetetyp.BLOCKSTROMWANDLER,
                    bezeichnung="56k Modem",
                    geraetenummer="456",
                ),
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
                    registeranzahl=Registeranzahl.ZWEITARIF,
                    zaehlerkonstante=Decimal(0.9),
                    eichung_bis=datetime(2022, 1, 1, 0, 0, 0),
                    externe_referenzen=[ExterneReferenz(ex_ref_name="zaehler im anderen system", ex_ref_wert="7890")],
                    letzte_eichung=datetime(2019, 6, 30, 0, 0, 0),
                )
            ],
            grundzustaendiger_msb_codenr="9910125000002",
            messadresse=Adresse(postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"),
        )
        assert melo.version is not None, "versionstruktur was not automatically set"
        assert melo.typ == Typ.MESSLOKATION, "_typ was not automatically set"

        json_string = melo.model_dump_json(by_alias=True)
        json_dict = json.loads(json_string)

        assert "_typ" in json_dict, "No camel case serialization"
        assert "messlokationsId" in json_dict, "No camel case serialization"

        deserialized_melo: Messlokation = Messlokation.model_validate_json(json_string)

        assert deserialized_melo.messlokations_id == melo.messlokations_id
        assert deserialized_melo.messlokations_id is not melo.messlokations_id
        assert deserialized_melo.typ is Typ.MESSLOKATION

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
