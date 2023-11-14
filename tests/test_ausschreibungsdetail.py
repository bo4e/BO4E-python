import pytest

from bo4e import Adresse, Ausschreibungsdetail, Menge, Netzebene, Zaehlertyp, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestAusschreibungsdetail:
    @pytest.mark.parametrize(
        "ausschreibungsdetail",
        [
            pytest.param(
                Ausschreibungsdetail(
                    marktlokations_id="56789012345",
                    netzebene_lieferung=Netzebene.MSP,
                    netzebene_messung=Netzebene.NSP,
                    marktlokationsadresse=Adresse(),
                    lieferzeitraum=Zeitraum(),
                    netzbetreiber="Stromnetz Hamburg GmbH",
                    kunde="Dei Mudder ihr Kunde",
                    zaehlernummer="1YSK4234092304",
                    marktlokationsbezeichnung="Zentraler Einkauf, Hamburg",
                    zaehlertechnik=Zaehlertyp.LEISTUNGSZAEHLER,
                    ist_lastgang_vorhanden=True,
                    prognose_jahresarbeit=Menge(),
                    prognose_arbeit_lieferzeitraum=Menge(),
                    prognose_leistung=Menge(),
                    rechnungsadresse=Adresse(),
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, ausschreibungsdetail: Ausschreibungsdetail) -> None:
        """
        Test de-/serialisation of Ausschreibungsdetail
        """
        assert_serialization_roundtrip(ausschreibungsdetail)
