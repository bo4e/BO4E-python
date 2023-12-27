import pytest

from bo4e import Adresse, Anrede, Geschaeftspartner, Geschaeftspartnerrolle, Kontakt, Landescode, Person
from tests.serialization_helper import assert_serialization_roundtrip


class TestGeschaeftspartner:
    @pytest.mark.parametrize(
        "geschaeftspartner",
        [
            pytest.param(
                Geschaeftspartner(
                    ansprechpartner=[Person(), Person()],
                    ist_gewerbe=True,
                    handelsregisternummer="HRB 254466",
                    amtsgericht="Amtsgericht München",
                    kontaktwege=[Kontakt()],
                    umsatzsteuer_id="DE267311963",
                    glaeubiger_id="DE98ZZZ09999999999",
                    website="bo4e.de",
                    geschaeftspartnerrollen=[Geschaeftspartnerrolle.DIENSTLEISTER],
                    partneradresse=Adresse(),
                ),
                id="all attributes at first level",
            ),
            pytest.param(
                Geschaeftspartner(
                    ansprechpartner=[Person(), Person()],
                    ist_gewerbe=True,
                    handelsregisternummer="HRB 254466",
                    amtsgericht="Amtsgericht Ibiza",
                    kontaktwege=[Kontakt()],
                    umsatzsteuer_id="AT12345",
                    geschaeftspartnerrollen=[Geschaeftspartnerrolle.DIENSTLEISTER],
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
