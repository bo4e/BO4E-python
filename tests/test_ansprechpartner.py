import pytest

from bo4e import Adresse, Anrede, Ansprechpartner, Geschaeftspartner, Rufnummer, Titel, Zustaendigkeit
from tests.serialization_helper import assert_serialization_roundtrip


class TestAnsprechpartner:
    @pytest.mark.parametrize(
        "ansprechpartner",
        [
            pytest.param(
                Ansprechpartner(
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
                ),
                id="all attributes at first level",  # = min + menge and betrag
            ),
        ],
    )
    def test_serialization_roundtrip(self, ansprechpartner: Ansprechpartner) -> None:
        """
        Test Test de-/serialisation roundtrip of Ansprechpartner
        """
        assert_serialization_roundtrip(ansprechpartner)
