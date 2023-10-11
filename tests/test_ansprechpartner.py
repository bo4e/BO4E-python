from bo4e import (
    Adresse,
    Anrede,
    Ansprechpartner,
    Geschaeftspartner,
    Geschaeftspartnerrolle,
    Kontaktart,
    Rufnummer,
    Rufnummernart,
    Themengebiet,
    Titel,
    Typ,
    Zustaendigkeit,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestAnsprechpartner:
    def test_serialization_roundtrip(self) -> None:
        """
        Test Test de-/serialisation roundtrip of Ansprechpartner
        """
        ansprechpartner = Ansprechpartner(
            nachname="Müller-Schmidt",
            geschaeftspartner=Geschaeftspartner(),
            anrede=Anrede.EHELEUTE,
            individuelle_anrede="Künstler",
            titel=Titel.PROF_DR,
            vorname="Hans",
            e_mail_adresse="hans.müller@getrei.de",
            kommentar="does this thing work?",
            adresse=Adresse(),
            rufnummer=Rufnummer(),
            zustaendigkeit=Zustaendigkeit(),
        )

        assert_serialization_roundtrip(ansprechpartner)
