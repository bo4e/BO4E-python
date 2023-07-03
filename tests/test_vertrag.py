from datetime import datetime, timezone
from typing import Any, Dict, List

import pytest
from pydantic import ValidationError

from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.bo.vertrag import Vertrag
from bo4e.com.adresse import Adresse
from bo4e.com.unterschrift import Unterschrift
from bo4e.com.vertragskonditionen import Vertragskonditionen
from bo4e.com.vertragsteil import Vertragsteil
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart
from bo4e.enum.landescode import Landescode
from bo4e.enum.sparte import Sparte
from bo4e.enum.vertragsart import Vertragsart
from bo4e.enum.vertragsstatus import Vertragsstatus


class TestVertrag:
    _vertragsnummer = "1234567891011"
    _vertragsart = Vertragsart.BILANZIERUNGSVERTRAG
    _vertragsstatus = Vertragsstatus.AKTIV
    _sparte = Sparte.STROM
    _vertragsbeginn = datetime(2021, 4, 30, 13, 45, tzinfo=timezone.utc)
    _vertragsende = datetime(2021, 6, 5, 16, 30, tzinfo=timezone.utc)
    _vertragspartner1 = Geschaeftspartner(
        anrede=Anrede.FRAU,
        name1="von Sinnen",
        name2="Helga",
        name3=None,
        gewerbekennzeichnung=True,
        kontaktweg=[Kontaktart.E_MAIL],
        umsatzsteuer_id="DE267311963",
        glaeubiger_id="DE98ZZZ09999999999",
        e_mail_adresse="test@bo4e.de",
        website="bo4e.de",
        geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
        partneradresse=Adresse(
            postleitzahl="24306",
            ort="Plön",
            strasse="Kirchstraße",
            hausnummer="3",
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
    _vertragsteile = [
        Vertragsteil(
            vertragsteilbeginn=datetime(2021, 4, 30, tzinfo=timezone.utc),
            vertragsteilende=datetime(2021, 6, 5, tzinfo=timezone.utc),
        )
    ]
    _vertragspartner1_dict: Dict[str, Any] = {
        "versionstruktur": "2",
        "boTyp": BoTyp.GESCHAEFTSPARTNER,
        "externeReferenzen": [],
        "name1": "von Sinnen",
        "gewerbekennzeichnung": True,
        "geschaeftspartnerrolle": [Geschaeftspartnerrolle.DIENSTLEISTER],
        "anrede": "FRAU",
        "name2": "Helga",
        "name3": None,
        "hrnummer": None,
        "amtsgericht": None,
        "kontaktweg": [Kontaktart.E_MAIL],
        "umsatzsteuerId": "DE267311963",
        "glaeubigerId": "DE98ZZZ09999999999",
        "eMailAdresse": "test@bo4e.de",
        "website": "bo4e.de",
        "partneradresse": {
            "postleitzahl": "24306",
            "ort": "Plön",
            "strasse": "Kirchstraße",
            "hausnummer": "3",
            "postfach": None,
            "adresszusatz": None,
            "coErgaenzung": None,
            "landescode": Landescode.DE,  # type:ignore[attr-defined]
            "ortsteil": None,
        },
    }
    _vertragspartner2_dict: Dict[str, Any] = {
        "versionstruktur": "2",
        "boTyp": BoTyp.GESCHAEFTSPARTNER,
        "externeReferenzen": [],
        "name1": "Eckart",
        "gewerbekennzeichnung": False,
        "geschaeftspartnerrolle": [Geschaeftspartnerrolle.DIENSTLEISTER],
        "anrede": None,
        "name2": "Björn",
        "name3": None,
        "hrnummer": None,
        "amtsgericht": None,
        "kontaktweg": [],
        "umsatzsteuerId": None,
        "glaeubigerId": None,
        "eMailAdresse": None,
        "website": None,
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
    }
    _vertragsteile_dict: List[Dict[str, Any]] = [
        {
            "vertragsteilbeginn": datetime(2021, 4, 30, tzinfo=timezone.utc),
            "vertragsteilende": datetime(2021, 6, 5, tzinfo=timezone.utc),
            "lokation": None,
            "vertraglichFixierteMenge": None,
            "minimaleAbnahmemenge": None,
            "maximaleAbnahmemenge": None,
        }
    ]

    def get_example_vertrag(self) -> Vertrag:
        return Vertrag(
            vertragsnummer=self._vertragsnummer,
            vertragsart=self._vertragsart,
            vertragsstatus=self._vertragsstatus,
            sparte=self._sparte,
            vertragsbeginn=self._vertragsbeginn,
            vertragsende=self._vertragsende,
            vertragspartner1=self._vertragspartner1,
            vertragspartner2=self._vertragspartner2,
            vertragsteile=self._vertragsteile,
        )

    def get_example_vertrag_expected_dict(self) -> Dict[str, Any]:
        return {
            "vertragsnummer": self._vertragsnummer,
            "vertragsart": self._vertragsart,
            "vertragsstatus": self._vertragsstatus,
            "sparte": self._sparte,
            "vertragsbeginn": self._vertragsbeginn,
            "vertragsende": self._vertragsende,
            "vertragspartner1": self._vertragspartner1_dict,
            "vertragspartner2": self._vertragspartner2_dict,
            "vertragsteile": self._vertragsteile_dict,
            "versionstruktur": "2",
            "boTyp": BoTyp.VERTRAG,
            "externeReferenzen": [],
            "beschreibung": None,
            "vertragskonditionen": None,
            "unterzeichnervp1": None,
            "unterzeichnervp2": None,
        }

    def test_serialisation_only_required_attributes(self) -> None:
        """
        Test de-/serialisation of Vertrag with minimal attributes.
        """
        vertrag = self.get_example_vertrag()

        json_string = vertrag.model_dump_json(by_alias=True)

        assert vertrag.bo_typ is BoTyp.VERTRAG, "boTyp was not automatically set"
        assert self._vertragsnummer in json_string
        assert "BILANZIERUNGSVERTRAG" in json_string
        assert "AKTIV" in json_string
        assert "STROM" in json_string
        assert "2021-04-30T13:45:00Z" in json_string
        assert "2021-06-05T16:30:00Z" in json_string
        assert "von Sinnen" in json_string
        assert "Preetz" in json_string
        assert "2021-06-05T00:00:00Z" in json_string

        vertrag_deserialized = Vertrag.model_validate_json(json_string)

        assert vertrag_deserialized.vertragsnummer == self._vertragsnummer
        assert vertrag_deserialized.vertragsart == self._vertragsart
        assert vertrag_deserialized.vertragsstatus == self._vertragsstatus
        assert vertrag_deserialized.sparte == self._sparte
        assert vertrag_deserialized.vertragsbeginn == self._vertragsbeginn
        assert vertrag_deserialized.vertragsende == self._vertragsende
        assert vertrag_deserialized.vertragspartner1 == self._vertragspartner1
        assert vertrag_deserialized.vertragspartner2 == self._vertragspartner2
        assert vertrag_deserialized.vertragsteile == self._vertragsteile

    def test_serialisation_required_and_optional_attributes(self) -> None:
        """
        Test de-/serialisation of Vertrag with maximal attributes.
        """

        vertrag = Vertrag(
            vertragsnummer=self._vertragsnummer,
            vertragsart=self._vertragsart,
            vertragsstatus=self._vertragsstatus,
            sparte=self._sparte,
            vertragsbeginn=self._vertragsbeginn,
            vertragsende=self._vertragsende,
            vertragspartner1=self._vertragspartner1,
            vertragspartner2=self._vertragspartner2,
            vertragsteile=[
                Vertragsteil(
                    vertragsteilbeginn=datetime(2021, 4, 30, tzinfo=timezone.utc),
                    vertragsteilende=datetime(2021, 6, 5, tzinfo=timezone.utc),
                ),
                Vertragsteil(
                    vertragsteilbeginn=datetime(2001, 1, 23, tzinfo=timezone.utc),
                    vertragsteilende=datetime(2002, 12, 3, tzinfo=timezone.utc),
                ),
            ],
            beschreibung="Hello Vertrag",
            vertragskonditionen=Vertragskonditionen(beschreibung="Beschreibung"),
            unterzeichnervp1=[Unterschrift(name="Foo")],
            unterzeichnervp2=[Unterschrift(name="Bar"), Unterschrift(name="Dr.No")],
        )

        json_string = vertrag.model_dump_json(by_alias=True)

        assert vertrag.bo_typ is BoTyp.VERTRAG, "boTyp was not automatically set"
        assert self._vertragsnummer in json_string
        assert "BILANZIERUNGSVERTRAG" in json_string
        assert "AKTIV" in json_string
        assert "STROM" in json_string
        assert "2021-04-30T13:45:00Z" in json_string
        assert "2021-06-05T16:30:00Z" in json_string
        assert "von Sinnen" in json_string
        assert "Preetz" in json_string
        assert "2021-06-05T00:00:00Z" in json_string
        assert "2002-12-03T00:00:00Z" in json_string
        assert "Hello Vertrag" in json_string
        assert "Beschreibung" in json_string
        assert "Foo" in json_string
        assert "Bar" in json_string
        assert "Dr.No" in json_string

        vertrag_deserialized = Vertrag.model_validate_json(json_string)

        assert vertrag_deserialized.vertragsnummer == self._vertragsnummer
        assert vertrag_deserialized.vertragsart == self._vertragsart
        assert vertrag_deserialized.vertragsstatus == self._vertragsstatus
        assert vertrag_deserialized.sparte == self._sparte
        assert vertrag_deserialized.vertragsbeginn == self._vertragsbeginn
        assert vertrag_deserialized.vertragsende == self._vertragsende
        assert vertrag_deserialized.vertragspartner1 == self._vertragspartner1
        assert vertrag_deserialized.vertragspartner2 == self._vertragspartner2
        assert vertrag_deserialized.vertragsteile == [
            Vertragsteil(
                vertragsteilbeginn=datetime(2021, 4, 30, tzinfo=timezone.utc),
                vertragsteilende=datetime(2021, 6, 5, tzinfo=timezone.utc),
            ),
            Vertragsteil(
                vertragsteilbeginn=datetime(2001, 1, 23, tzinfo=timezone.utc),
                vertragsteilende=datetime(2002, 12, 3, tzinfo=timezone.utc),
            ),
        ]
        assert vertrag_deserialized.beschreibung == "Hello Vertrag"
        assert vertrag_deserialized.vertragskonditionen == Vertragskonditionen(beschreibung="Beschreibung")
        assert vertrag_deserialized.unterzeichnervp1 == [Unterschrift(name="Foo")]
        assert vertrag_deserialized.unterzeichnervp2 == [Unterschrift(name="Bar"), Unterschrift(name="Dr.No")]

    def test_missing_required_attributes(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Vertrag()  # type: ignore[call-arg]

        assert "9 validation errors" in str(excinfo.value)

    def test_serialization_fails_for_empty_vertragsteile(self) -> None:
        """
        Test serialisation of Zaehler fails if there are no vertragsteile.
        """
        with pytest.raises(ValidationError) as excinfo:
            _ = Vertrag(
                vertragsnummer=self._vertragsnummer,
                vertragsart=self._vertragsart,
                vertragsstatus=self._vertragsstatus,
                sparte=self._sparte,
                vertragsbeginn=self._vertragsbeginn,
                vertragsende=self._vertragsende,
                vertragspartner1=self._vertragspartner1,
                vertragspartner2=self._vertragspartner2,
                vertragsteile=[],
            )

        assert "1 validation error" in str(excinfo.value)
        assert "too_short" in str(excinfo.value)
