from datetime import time, timezone

import pytest

from bo4e import (
    Adresse,
    Anrede,
    Geschaeftspartner,
    Geschaeftspartnerrolle,
    Kontaktweg,
    Landescode,
    Organisationstyp,
    Person,
    Titel,
)
from bo4e.com.erreichbarkeit import Erreichbarkeit
from bo4e.com.zeitfenster import Zeitfenster
from tests.serialization_helper import assert_serialization_roundtrip


class TestGeschaeftspartner:
    @pytest.mark.parametrize(
        "geschaeftspartner",
        [
            pytest.param(
                Geschaeftspartner(
                    ansprechpartner=[Person(), Person()],
                    anrede=Anrede.EHELEUTE,
                    individuelle_anrede="Künstler",
                    titel=Titel.PROF_DR,
                    vorname="Hans",
                    nachname="Müller-Schmidt",
                    organisationstyp=Organisationstyp.UNTERNEHMEN,
                    handelsregisternummer="HRB 254466",
                    amtsgericht="Amtsgericht München",
                    kontaktwege=[Kontaktweg()],
                    umsatzsteuer_id="DE267311963",
                    glaeubiger_id="DE98ZZZ09999999999",
                    website="bo4e.de",
                    geschaeftspartnerrollen=[Geschaeftspartnerrolle.DIENSTLEISTER],
                    adresse=Adresse(),
                ),
                id="all attributes at first level",
            ),
            pytest.param(
                Geschaeftspartner(
                    ansprechpartner=[Person(), Person()],
                    anrede=Anrede.EHELEUTE,
                    individuelle_anrede="Künstler",
                    titel=Titel.PROF_DR,
                    vorname="Hans",
                    nachname="Müller-Schmidt",
                    organisationstyp=Organisationstyp.UNTERNEHMEN,
                    handelsregisternummer="HRB 254466",
                    amtsgericht="Amtsgericht Ibiza",
                    kontaktwege=[Kontaktweg()],
                    umsatzsteuer_id="AT12345",
                    geschaeftspartnerrollen=[Geschaeftspartnerrolle.DIENSTLEISTER],
                    adresse=Adresse(
                        postleitzahl="1014", ort="Wien 1", strasse="Ballhausplatz", hausnummer="2", landescode=Landescode.AT  # type: ignore[attr-defined]
                    ),
                    erreichbarkeit=Erreichbarkeit(
                        montag_erreichbarkeit=Zeitfenster(
                            startzeit=time(14, 00, tzinfo=timezone.utc), endzeit=time(17, 00, tzinfo=timezone.utc)
                        ),
                        mittwoch_erreichbarkeit=Zeitfenster(
                            startzeit=time(6, 00, tzinfo=timezone.utc), endzeit=time(12, 00, tzinfo=timezone.utc)
                        ),
                        freitag_erreichbarkeit=Zeitfenster(
                            startzeit=time(5, 00, tzinfo=timezone.utc), endzeit=time(22, 00, tzinfo=timezone.utc)
                        ),
                        mittagspause=Zeitfenster(
                            startzeit=time(12, 00, tzinfo=timezone.utc), endzeit=time(13, 00, tzinfo=timezone.utc)
                        ),
                    ),
                ),
                id="Landescode!=DE, DE is default",
            ),
        ],
    )
    def test_serialization_roundtrip(self, geschaeftspartner: Geschaeftspartner) -> None:
        """
        Test de-/serialisation of Geschaeftspartner.
        """

        assert_serialization_roundtrip(geschaeftspartner)
