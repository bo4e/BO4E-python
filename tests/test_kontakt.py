import pytest

from bo4e import Kontaktart, Kontaktweg
from tests.serialization_helper import assert_serialization_roundtrip


class TestKontakt:
    @pytest.mark.parametrize(
        "kontakt",
        [
            pytest.param(
                Kontaktweg(
                    kontaktart=Kontaktart.E_MAIL,
                    beschreibung="irgendeine Spezifikation",
                    kontaktwert="test@bo4e.de",
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, kontakt: Kontaktweg) -> None:
        """
        Test de-/serialisation of Kontakt.
        """

        assert_serialization_roundtrip(kontakt)
