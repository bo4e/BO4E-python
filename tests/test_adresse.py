from datetime import datetime, timezone

import pytest

from bo4e import (
    Adresse,
    Anrede,
    Geschaeftspartner,
    Geschaeftspartnerrolle,
    Kontaktweg,
    Organisationstyp,
    Person,
    Sparte,
    Titel,
    Unterschrift,
    Vertrag,
    Vertragsart,
    Vertragskonditionen,
    Vertragsstatus,
    Vertragsteil,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestVertrag:
    @pytest.mark.parametrize(
        "vertrag",
        [
            pytest.param(
                Vertrag(
                    vertragsnummer="1234567891011",
                    vertragsart=Vertragsart.BILANZIERUNGSVERTRAG,
                    vertragsstatus=Vertragsstatus.AKTIV,
                    sparte=Sparte.STROM,
                    vertragsbeginn=datetime(2021, 4, 30, 13, 45, tzinfo=timezone.utc),
                    vertragsende=datetime(2021, 6, 5, 16, 30, tzinfo=timezone.utc),
                    vertragspartner1=Geschaeftspartner(
                        ansprechpartner=[Person(), Person()],
                        anrede=Anrede.EHELEUTE,
                        individuelle_anrede="Künstler",
                        titel=Titel.PROF_DR,
                        vorname="Hans",
                        nachname="Müller-Schmidt",
                        organisationstyp=Organisationstyp.PRIVATPERSON,
                        kontaktwege=[Kontaktweg()],
                        umsatzsteuer_id="DE267311963",
                        glaeubiger_id="DE98ZZZ09999999999",
                        website="bo4e.de",
                        geschaeftspartnerrollen=[Geschaeftspartnerrolle.DIENSTLEISTER],
                        adresse=Adresse(
                            postleitzahl="24306",
                            ort="Plön",
                            strasse="Kirchstraße",
                            hausnummer="3",
                        ),
                    ),
                    vertragspartner2=Geschaeftspartner(
                        ansprechpartner=[Person(), Person()],
                        organisationstyp=Organisationstyp.UNTERNEHMEN,
                        organisationsname="Hochfrequenz",
                        geschaeftspartnerrollen=[Geschaeftspartnerrolle.DIENSTLEISTER],
                        adresse=Adresse(
                            postleitzahl="24211",
                            ort="Preetz",
                            strasse="Am Markt",
                            hausnummer="67",
                        ),
                    ),
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
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, vertrag: Vertrag) -> None:
        """
        Test de-/serialisation of Vertrag.
        """
        assert_serialization_roundtrip(vertrag)
