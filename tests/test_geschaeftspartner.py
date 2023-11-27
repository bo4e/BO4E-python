import pytest

from bo4e import Adresse, Anrede, Geschaeftspartner, Geschaeftspartnerrolle, Kontaktart, Landescode
from tests.serialization_helper import assert_serialization_roundtrip


class TestGeschaeftspartner:
    @pytest.mark.parametrize(
        "geschaeftspartner",
        [
            pytest.param(
                Geschaeftspartner(
                    anrede=Anrede.FRAU,
                    name1="von Sinnen",
                    name2="Helga",
                    name3=None,
                    ist_gewerbe=True,
                    hrnummer="HRB 254466",
                    amtsgericht="Amtsgericht München",
                    kontaktweg=[Kontaktart.E_MAIL],
                    umsatzsteuer_id="DE267311963",
                    glaeubiger_id="DE98ZZZ09999999999",
                    e_mail_adresse="test@bo4e.de",
                    website="bo4e.de",
                    geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
                    partneradresse=Adresse(),
                ),
                id="all attributes at first level",
            ),
            pytest.param(
                Geschaeftspartner(
                    anrede=Anrede.FRAU,
                    name1="Kurz",
                    name2="Sebastian",
                    name3=None,
                    ist_gewerbe=True,
                    hrnummer="HRB 254466",
                    amtsgericht="Amtsgericht Ibiza",
                    kontaktweg=[Kontaktart.E_MAIL],
                    umsatzsteuer_id="AT12345",
                    geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
                    partneradresse=Adresse(
                        postleitzahl="1014", ort="Wien 1", strasse="Ballhausplatz", hausnummer="2", landescode=Landescode.AT  # type: ignore[attr-defined]
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
