import pytest

from bo4e import Anrede, Kontakt, Person, Titel, Zustaendigkeit
from tests.serialization_helper import assert_serialization_roundtrip


class TestPerson:
    @pytest.mark.parametrize(
        "person",
        [
            pytest.param(
                Person(
                    anrede=Anrede.HERR,
                    titel=Titel.PROF_DR,
                    vorname="Hans",
                    nachname="Müller-Schmidt",
                    kontaktwege=[Kontakt(), Kontakt()],
                    kommentar="does this thing work?",
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
