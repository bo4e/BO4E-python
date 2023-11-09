from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Adresse, Ausschreibungsdetail, Landescode, Menge, Netzebene, Zaehlertyp, Zeiteinheit, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip

example_ausschreibungsdetail = Ausschreibungsdetail(
    marktlokations_id="56789012345",
    netzebene_lieferung=Netzebene.MSP,
    netzebene_messung=Netzebene.NSP,
    marktlokationsadresse=Adresse(),
    lieferzeitraum=Zeitraum(),
    rechnungsadresse=Adresse(),
)
example_ausschreibungsdetail_dict = {
    "zaehlernummer": None,
    "zaehlertechnik": None,
    "kunde": None,
    "marktlokationsbezeichnung": None,
    "lieferzeitraum": {
        "dauer": Decimal("5"),
        "startdatum": None,
        "endzeitpunkt": None,
        "enddatum": None,
        "einheit": Zeiteinheit.TAG,
        "startzeitpunkt": None,
        "_id": None,
    },
    "marktlokationsadresse": {
        "landescode": Landescode.DE,  # type: ignore[attr-defined]
        "hausnummer": "27A",
        "strasse": "Nördliche Münchner Straße",
        "postleitzahl": "82031",
        "ort": "Grünwald",
        "adresszusatz": None,
        "postfach": None,
        "coErgaenzung": None,
        "ortsteil": None,
        "_id": None,
    },
    "rechnungsadresse": {
        "landescode": Landescode.DE,  # type: ignore[attr-defined]
        "hausnummer": "27A",
        "strasse": "Nördliche Münchner Straße",
        "postleitzahl": "82031",
        "ort": "Grünwald",
        "adresszusatz": None,
        "postfach": None,
        "coErgaenzung": None,
        "ortsteil": None,
        "_id": None,
    },
    "netzbetreiber": None,
    "netzebeneLieferung": Netzebene.MSP,
    "prognoseArbeitLieferzeitraum": None,
    "netzebeneMessung": Netzebene.NSP,
    "prognoseLeistung": None,
    "istLastgangVorhanden": None,
    "prognoseJahresarbeit": None,
    "marktlokationsId": "56789012345",
    "_id": None,
}


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
