import pytest

from bo4e import Anrede, Geschaeftspartner, Geschaeftspartnerrolle, Kontakt, Organisationstyp, Person, Titel
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
                    kontaktwege=[Kontakt()],
                    umsatzsteuer_id="DE267311963",
                    glaeubiger_id="DE98ZZZ09999999999",
                    website="bo4e.de",
                    geschaeftspartnerrollen=[Geschaeftspartnerrolle.DIENSTLEISTER],
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
                    kontaktwege=[Kontakt()],
                    umsatzsteuer_id="AT12345",
                    geschaeftspartnerrollen=[Geschaeftspartnerrolle.DIENSTLEISTER],
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
