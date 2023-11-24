from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Ausschreibungsdetail, Landescode, Menge, Mengeneinheit, Netzebene, Zaehlertyp, Zeiteinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_adresse import example_adresse
from tests.test_zeitraum import example_zeitraum

example_ausschreibungsdetail = Ausschreibungsdetail(
    marktlokations_id="56789012345",
    netzebene_lieferung=Netzebene.MSP,
    netzebene_messung=Netzebene.NSP,
    marktlokationsadresse=example_adresse,
    lieferzeitraum=example_zeitraum,
    rechnungsadresse=example_adresse,
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
        "ausschreibungsdetail, expected_json_dict",
        [
            pytest.param(
                Ausschreibungsdetail(
                    marktlokations_id="56789012345",
                    netzebene_lieferung=Netzebene.MSP,
                    netzebene_messung=Netzebene.NSP,
                    marktlokationsadresse=example_adresse,
                    lieferzeitraum=example_zeitraum,
                    netzbetreiber="Stromnetz Hamburg GmbH",
                    kunde="Dei Mudder ihr Kunde",
                    zaehlernummer="1YSK4234092304",
                    marktlokationsbezeichnung="Zentraler Einkauf, Hamburg",
                    zaehlertechnik=Zaehlertyp.LEISTUNGSZAEHLER,
                    ist_lastgang_vorhanden=True,
                    prognose_leistung=Menge(wert=Decimal(40), einheit=Mengeneinheit.KW),
                    prognose_arbeit_lieferzeitraum=Menge(wert=Decimal(2500), einheit=Mengeneinheit.KWH),
                    prognose_jahresarbeit=Menge(wert=Decimal(2500), einheit=Mengeneinheit.KWH),
                    rechnungsadresse=example_adresse,
                ),
                {
                    "netzbetreiber": "Stromnetz Hamburg GmbH",
                    "lieferzeitraum": {
                        "enddatum": None,
                        "startdatum": None,
                        "einheit": Zeiteinheit.TAG,
                        "endzeitpunkt": None,
                        "dauer": Decimal("5"),
                        "startzeitpunkt": None,
                        "_id": None,
                    },
                    "zaehlertechnik": Zaehlertyp.LEISTUNGSZAEHLER,
                    "kunde": "Dei Mudder ihr Kunde",
                    "marktlokationsbezeichnung": "Zentraler Einkauf, Hamburg",
                    "marktlokationsadresse": {
                        "hausnummer": "27A",
                        "adresszusatz": None,
                        "postfach": None,
                        "postleitzahl": "82031",
                        "landescode": Landescode.DE,  # type: ignore[attr-defined]
                        "ort": "Grünwald",
                        "strasse": "Nördliche Münchner Straße",
                        "coErgaenzung": None,
                        "ortsteil": None,
                        "_id": None,
                    },
                    "rechnungsadresse": {
                        "hausnummer": "27A",
                        "adresszusatz": None,
                        "postfach": None,
                        "postleitzahl": "82031",
                        "landescode": Landescode.DE,  # type: ignore[attr-defined]
                        "ort": "Grünwald",
                        "strasse": "Nördliche Münchner Straße",
                        "coErgaenzung": None,
                        "ortsteil": None,
                        "_id": None,
                    },
                    "zaehlernummer": "1YSK4234092304",
                    "prognoseJahresarbeit": {"wert": Decimal("2500"), "einheit": Mengeneinheit.KWH, "_id": None},
                    "netzebeneLieferung": Netzebene.MSP,
                    "marktlokationsId": "56789012345",
                    "prognoseLeistung": {"wert": Decimal("40"), "einheit": Mengeneinheit.KW, "_id": None},
                    "istLastgangVorhanden": True,
                    "netzebeneMessung": Netzebene.NSP,
                    "prognoseArbeitLieferzeitraum": {
                        "wert": Decimal("2500"),
                        "einheit": Mengeneinheit.KWH,
                        "_id": None,
                    },
                    "_id": None,
                },
            ),
            pytest.param(example_ausschreibungsdetail, example_ausschreibungsdetail_dict),
        ],
    )
    def test_serialization_roundtrip(
        self, ausschreibungsdetail: Ausschreibungsdetail, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Ausschreibungsdetail
        """
        assert_serialization_roundtrip(ausschreibungsdetail, expected_json_dict)
