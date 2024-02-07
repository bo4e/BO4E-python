import pytest

from bo4e import Adresse, Kontaktart, Kontaktweg
from tests.serialization_helper import assert_serialization_roundtrip


class TestKontakt:
    @pytest.mark.parametrize(
        "kontakt",
        [
            pytest.param(
                Kontaktweg(
                    kontaktart=Kontaktart.E_MAIL,
                    e_mail_adresse="test@bo4e.de",
                    adresse=Adresse(),
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
