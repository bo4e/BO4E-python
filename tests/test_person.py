import pytest

from bo4e import Adresse, Anrede, Kontaktweg, Person, Titel, Zustaendigkeit
from tests.serialization_helper import assert_serialization_roundtrip


class TestPerson:
    @pytest.mark.parametrize(
        "person",
        [
            pytest.param(
                Person(
                    anrede=Anrede.EHELEUTE,
                    individuelle_anrede="Künstler",
                    titel=Titel.PROF_DR,
                    vorname="Hans",
                    nachname="Müller-Schmidt",
                    kontaktwege=[Kontaktweg(), Kontaktweg()],
                    kommentar="does this thing work?",
                    adresse=Adresse(),
                    zustaendigkeiten=[Zustaendigkeit()],
                ),
                id="all attributes at first level",  # = min + menge and betrag
            ),
        ],
    )
    def test_serialization_roundtrip(self, person: Person) -> None:
        """
        Test Test de-/serialisation roundtrip of Person
        """
        assert_serialization_roundtrip(person)
