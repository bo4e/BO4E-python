from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.ausschreibungsdetail import Ausschreibungsdetail
from bo4e.com.menge import Menge
from bo4e.enum.landescode import Landescode
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.zaehlertyp import Zaehlertyp
from bo4e.enum.zeiteinheit import Zeiteinheit
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
    },
    "netzbetreiber": None,
    "netzebeneLieferung": Netzebene.MSP,
    "prognoseArbeitLieferzeitraum": None,
    "netzebeneMessung": Netzebene.NSP,
    "prognoseLeistung": None,
    "lastgangVorhanden": None,
    "prognoseJahresarbeit": None,
    "marktlokationsId": "56789012345",
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
                    lastgang_vorhanden=True,
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
                    },
                    "zaehlernummer": "1YSK4234092304",
                    "prognoseJahresarbeit": {"wert": Decimal("2500"), "einheit": Mengeneinheit.KWH},
                    "netzebeneLieferung": Netzebene.MSP,
                    "marktlokationsId": "56789012345",
                    "prognoseLeistung": {"wert": Decimal("40"), "einheit": Mengeneinheit.KW},
                    "lastgangVorhanden": True,
                    "netzebeneMessung": Netzebene.NSP,
                    "prognoseArbeitLieferzeitraum": {"wert": Decimal("2500"), "einheit": Mengeneinheit.KWH},
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

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Ausschreibungsdetail()  # type: ignore[call-arg]

        assert "5 validation errors" in str(excinfo.value)
        # 'lokations_id', 'netzebene_lieferung', 'netzebene_messung', 'lokationsadresse', and 'lieferzeitraum'
