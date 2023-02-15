from datetime import datetime, timezone
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.bo.buendelvertrag import Buendelvertrag
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.com.unterschrift import Unterschrift
from bo4e.com.vertragskonditionen import Vertragskonditionen
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart
from bo4e.enum.landescode import Landescode
from bo4e.enum.sparte import Sparte
from bo4e.enum.vertragsart import Vertragsart
from bo4e.enum.vertragsstatus import Vertragsstatus
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_vertrag import TestVertrag


class TestBuendelvertrag:
    _vertragspartner1 = Geschaeftspartner(
        anrede=Anrede.FRAU,
        name1="van der Waal",
        name2="Helga",
        name3=None,
        gewerbekennzeichnung=True,
        kontaktweg=[Kontaktart.SMS],
        umsatzsteuer_id="DE267311963",
        glaeubiger_id="DE98ZZZ09999999999",
        e_mail_adresse="helga.waal@bo4e.de",
        website="bo4e.de",
        geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
        partneradresse=Adresse(
            postleitzahl="33333",
            ort="Quadrat-Ichendorf",
            strasse="Kubikstraße",
            hausnummer="4",
        ),
    )
    _vertragspartner2 = Geschaeftspartner(
        name1="Eckart",
        name2="Björn",
        gewerbekennzeichnung=False,
        geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
        partneradresse=Adresse(
            postleitzahl="24211",
            ort="Preetz",
            strasse="Am Markt",
            hausnummer="67",
        ),
    )
    _vertragspartner1_dict: Dict[str, Any] = {
        "anrede": Anrede.FRAU,
        "name1": "van der Waal",
        "name2": "Helga",
        "name3": None,
        "gewerbekennzeichnung": True,
        "kontaktweg": [Kontaktart.SMS],
        "umsatzsteuerId": "DE267311963",
        "glaeubigerId": "DE98ZZZ09999999999",
        "eMailAdresse": "helga.waal@bo4e.de",
        "website": "bo4e.de",
        "geschaeftspartnerrolle": [Geschaeftspartnerrolle.DIENSTLEISTER],
        "partneradresse": {
            "postleitzahl": "33333",
            "ort": "Quadrat-Ichendorf",
            "strasse": "Kubikstraße",
            "hausnummer": "4",
            "postfach": None,
            "adresszusatz": None,
            "coErgaenzung": None,
            "landescode": Landescode.DE,  # type:ignore[attr-defined]
            "ortsteil": None,
        },
        "versionstruktur": "2",
        "boTyp": BoTyp.GESCHAEFTSPARTNER,
        "externeReferenzen": [],
        "hrnummer": None,
        "amtsgericht": None,
    }
    _vertragspartner2_dict: Dict[str, Any] = {
        "name1": "Eckart",
        "name2": "Björn",
        "gewerbekennzeichnung": False,
        "geschaeftspartnerrolle": [Geschaeftspartnerrolle.DIENSTLEISTER],
        "partneradresse": {
            "postleitzahl": "24211",
            "ort": "Preetz",
            "strasse": "Am Markt",
            "hausnummer": "67",
            "postfach": None,
            "adresszusatz": None,
            "coErgaenzung": None,
            "landescode": Landescode.DE,  # type:ignore[attr-defined]
            "ortsteil": None,
        },
        "versionstruktur": "2",
        "boTyp": BoTyp.GESCHAEFTSPARTNER,
        "externeReferenzen": [],
        "anrede": None,
        "name3": None,
        "hrnummer": None,
        "amtsgericht": None,
        "kontaktweg": [],
        "umsatzsteuerId": None,
        "glaeubigerId": None,
        "eMailAdresse": None,
        "website": None,
    }

    @pytest.mark.parametrize(
        "buendelvertrag, expected_dict",
        [
            pytest.param(
                Buendelvertrag(
                    vertragsnummer="1234567890",
                    vertragsart=Vertragsart.NETZNUTZUNGSVERTRAG,
                    vertragsstatus=Vertragsstatus.AKTIV,
                    sparte=Sparte.STROM,
                    vertragsbeginn=datetime(2021, 4, 30, 13, 45, tzinfo=timezone.utc),
                    vertragsende=datetime(2200, 4, 30, 13, 45, tzinfo=timezone.utc),
                    vertragspartner1=_vertragspartner1,
                    vertragspartner2=_vertragspartner2,
                ),
                {
                    "vertragsnummer": "1234567890",
                    "vertragsart": Vertragsart.NETZNUTZUNGSVERTRAG,
                    "vertragsstatus": Vertragsstatus.AKTIV,
                    "sparte": Sparte.STROM,
                    "vertragsbeginn": datetime(2021, 4, 30, 13, 45, tzinfo=timezone.utc),
                    "vertragsende": datetime(2200, 4, 30, 13, 45, tzinfo=timezone.utc),
                    "vertragspartner1": _vertragspartner1_dict,
                    "vertragspartner2": _vertragspartner2_dict,
                    "versionstruktur": "2",
                    "boTyp": BoTyp.BUENDELVERTRAG,
                    "externeReferenzen": [],
                    "einzelvertraege": [],
                    "vertragskonditionen": [],
                    "unterzeichnervp1": [],
                    "unterzeichnervp2": [],
                    "beschreibung": None,
                },
                id="minimal fields",
            ),
            pytest.param(
                Buendelvertrag(
                    vertragsnummer="1234567890",
                    vertragsart=Vertragsart.NETZNUTZUNGSVERTRAG,
                    vertragsstatus=Vertragsstatus.AKTIV,
                    sparte=Sparte.STROM,
                    vertragsbeginn=datetime(2021, 4, 30, 13, 45, tzinfo=timezone.utc),
                    vertragsende=datetime(2200, 4, 30, 13, 45, tzinfo=timezone.utc),
                    vertragspartner1=_vertragspartner1,
                    vertragspartner2=_vertragspartner2,
                    einzelvertraege=[TestVertrag().get_example_vertrag()],
                    vertragskonditionen=[Vertragskonditionen(beschreibung="Hello World")],
                    unterzeichnervp1=[Unterschrift(name="Helga van der Waal")],
                    unterzeichnervp2=[Unterschrift(name="Björn oder so"), Unterschrift(name="Zweiter Typ")],
                    beschreibung="Das ist ein Bündelvertrag mit allen optionalen Feldern ausgefüllt.",
                ),
                {
                    "versionstruktur": "2",
                    "boTyp": BoTyp.BUENDELVERTRAG,
                    "externeReferenzen": [],
                    "vertragsnummer": "1234567890",
                    "vertragsart": Vertragsart.NETZNUTZUNGSVERTRAG,
                    "vertragsstatus": Vertragsstatus.AKTIV,
                    "sparte": Sparte.STROM,
                    "vertragsbeginn": datetime(2021, 4, 30, 13, 45, tzinfo=timezone.utc),
                    "vertragsende": datetime(2200, 4, 30, 13, 45, tzinfo=timezone.utc),
                    "vertragspartner1": _vertragspartner1_dict,
                    "vertragspartner2": _vertragspartner2_dict,
                    "einzelvertraege": [TestVertrag().get_example_vertrag_expected_dict()],
                    "vertragskonditionen": [
                        {
                            "beschreibung": "Hello World",
                            "anzahlAbschlaege": None,
                            "vertragslaufzeit": None,
                            "kuendigungsfrist": None,
                            "vertragsverlaengerung": None,
                            "abschlagszyklus": None,
                        }
                    ],
                    "unterzeichnervp1": [{"name": "Helga van der Waal", "ort": None, "datum": None}],
                    "unterzeichnervp2": [
                        {"name": "Björn oder so", "ort": None, "datum": None},
                        {"name": "Zweiter Typ", "ort": None, "datum": None},
                    ],
                    "beschreibung": "Das ist ein Bündelvertrag mit allen optionalen Feldern ausgefüllt.",
                },
                id="maximal fields",
            ),
        ],
    )
    def test_serialization_roundtrip(self, buendelvertrag: Buendelvertrag, expected_dict: Dict[str, Any]) -> None:
        assert_serialization_roundtrip(buendelvertrag, expected_dict)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Buendelvertrag()  # type: ignore[call-arg]

        assert "8 validation errors" in str(excinfo.value)
