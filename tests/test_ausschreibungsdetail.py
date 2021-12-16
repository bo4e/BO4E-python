from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.ausschreibungsdetail import Ausschreibungsdetail, AusschreibungsdetailSchema
from bo4e.com.menge import Menge
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.zaehlertyp import Zaehlertyp
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_adresse import example_adresse  # type:ignore[import]
from tests.test_menge import example_menge  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestAusschreibungsdetail:
    @pytest.mark.parametrize(
        "ausschreibungsdetail, expected_json_dict",
        [
            pytest.param(
                Ausschreibungsdetail(
                    lokations_id="56789012345",
                    netzebene_lieferung=Netzebene.MSP,
                    netzebene_messung=Netzebene.NSP,
                    lokationsadresse=example_adresse,
                    lieferzeitraum=example_zeitraum,
                    netzbetreiber="Stromnetz Hamburg GmbH",
                    kunde="Dei Mudder ihr Kunde",
                    zaehlernummer="1YSK4234092304",
                    lokationsbezeichnung="Zentraler Einkauf, Hamburg",
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
                        "einheit": "TAG",
                        "endzeitpunkt": None,
                        "dauer": "5",
                        "startzeitpunkt": None,
                    },
                    "zaehlertechnik": "LEISTUNGSZAEHLER",
                    "kunde": "Dei Mudder ihr Kunde",
                    "lokationsbezeichnung": "Zentraler Einkauf, Hamburg",
                    "lokationsadresse": {
                        "hausnummer": "27A",
                        "adresszusatz": None,
                        "postfach": None,
                        "postleitzahl": "82031",
                        "landescode": "DE",
                        "ort": "Grünwald",
                        "strasse": "Nördliche Münchner Straße",
                        "coErgaenzung": None,
                    },
                    "rechnungsadresse": {
                        "hausnummer": "27A",
                        "adresszusatz": None,
                        "postfach": None,
                        "postleitzahl": "82031",
                        "landescode": "DE",
                        "ort": "Grünwald",
                        "strasse": "Nördliche Münchner Straße",
                        "coErgaenzung": None,
                    },
                    "zaehlernummer": "1YSK4234092304",
                    "prognoseJahresarbeit": {"wert": "2500", "einheit": "KWH"},
                    "netzebeneLieferung": "MSP",
                    "lokationsId": "56789012345",
                    "prognoseLeistung": {"wert": "40", "einheit": "KW"},
                    "lastgangVorhanden": True,
                    "netzebeneMessung": "NSP",
                    "prognoseArbeitLieferzeitraum": {"wert": "2500", "einheit": "KWH"},
                },
            ),
            pytest.param(
                Ausschreibungsdetail(
                    lokations_id="56789012345",
                    netzebene_lieferung=Netzebene.MSP,
                    netzebene_messung=Netzebene.NSP,
                    lokationsadresse=example_adresse,
                    lieferzeitraum=example_zeitraum,
                    rechnungsadresse=example_adresse,
                ),
                {
                    "zaehlernummer": None,
                    "zaehlertechnik": None,
                    "kunde": None,
                    "lokationsbezeichnung": None,
                    "lieferzeitraum": {
                        "dauer": "5",
                        "startdatum": None,
                        "endzeitpunkt": None,
                        "enddatum": None,
                        "einheit": "TAG",
                        "startzeitpunkt": None,
                    },
                    "lokationsadresse": {
                        "landescode": "DE",
                        "hausnummer": "27A",
                        "strasse": "Nördliche Münchner Straße",
                        "postleitzahl": "82031",
                        "ort": "Grünwald",
                        "adresszusatz": None,
                        "postfach": None,
                        "coErgaenzung": None,
                    },
                    "rechnungsadresse": {
                        "landescode": "DE",
                        "hausnummer": "27A",
                        "strasse": "Nördliche Münchner Straße",
                        "postleitzahl": "82031",
                        "ort": "Grünwald",
                        "adresszusatz": None,
                        "postfach": None,
                        "coErgaenzung": None,
                    },
                    "netzbetreiber": None,
                    "netzebeneLieferung": "MSP",
                    "prognoseArbeitLieferzeitraum": None,
                    "netzebeneMessung": "NSP",
                    "prognoseLeistung": None,
                    "lastgangVorhanden": None,
                    "prognoseJahresarbeit": None,
                    "lokationsId": "56789012345",
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, ausschreibungsdetail: Ausschreibungsdetail, expected_json_dict: dict):
        """
        Test de-/serialisation of Ausschreibungsdetail
        """
        assert_serialization_roundtrip(ausschreibungsdetail, AusschreibungsdetailSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Ausschreibungsdetail()

        assert "missing 5 required" in str(excinfo.value)
        # 'lokations_id', 'netzebene_lieferung', 'netzebene_messung', 'lokationsadresse', and 'lieferzeitraum'
