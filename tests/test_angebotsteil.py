from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.bo.marktlokation import Marktlokation
from bo4e.com.adresse import Adresse
from bo4e.com.angebotsposition import Angebotsposition
from bo4e.com.angebotsteil import Angebotsteil, AngebotsteilSchema
from bo4e.com.betrag import Betrag
from bo4e.com.menge import Menge
from bo4e.com.preis import Preis
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]

example_angebotsteil: Angebotsteil = Angebotsteil(
    positionen=[
        Angebotsposition(
            positionsbezeichnung="teststring",
            positionsmenge=Menge(wert=Decimal(4000), einheit=Mengeneinheit.KWH),
            positionspreis=Preis(wert=Decimal(0.2456), einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH),
            positionskosten=Betrag(
                waehrung=Waehrungscode.EUR,
                wert=Decimal(98240),
            ),
        )
    ],
)

example_angebotsteil_json = {
    "positionen": [
        {
            "positionsbezeichnung": "teststring",
            "positionsmenge": {"wert": "4000", "einheit": "KWH"},
            "positionskosten": {"waehrung": "EUR", "wert": "98240"},
            "positionspreis": {
                "bezugswert": "KWH",
                "status": None,
                "wert": "0.2456000000000000127453603226967970840632915496826171875",
                "einheit": "EUR",
            },
        },
    ],
    "anfrageSubreferenz": None,
    "lieferstellenangebotsteil": None,
    "gesamtmengeangebotsteil": None,
    "gesamtkostenangebotsteil": None,
    "lieferzeitraum": None,
}


class TestAngebotsteil:
    @pytest.mark.parametrize(
        "angebotsteil, expected_json_dict",
        [
            pytest.param(
                Angebotsteil(
                    positionen=[
                        Angebotsposition(
                            positionsbezeichnung="testtring",
                            positionsmenge=Menge(wert=Decimal(4000), einheit=Mengeneinheit.KWH),
                            positionspreis=Preis(
                                wert=Decimal(0.2456), einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH
                            ),
                            positionskosten=Betrag(
                                waehrung=Waehrungscode.EUR,
                                wert=Decimal(98240),
                            ),
                        )
                    ],
                    anfrage_subreferenz="teststring",
                    lieferstellenangebotsteil=[
                        Marktlokation(
                            marktlokations_id="51238696781",
                            sparte=Sparte.GAS,
                            lokationsadresse=Adresse(
                                postleitzahl="82031",
                                ort="Grünwald",
                                hausnummer="27A",
                                strasse="Nördliche Münchner Straße",
                            ),
                            energierichtung=Energierichtung.EINSP,
                            bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
                            unterbrechbar=True,
                            netzebene=Netzebene.NSP,
                        )
                    ],
                    gesamtmengeangebotsteil=Menge(wert=Decimal(4000), einheit=Mengeneinheit.KWH),
                    gesamtkostenangebotsteil=Betrag(
                        waehrung=Waehrungscode.EUR,
                        wert=Decimal(98240),
                    ),
                    lieferzeitraum=Zeitraum(
                        startdatum=datetime(2020, 1, 1, tzinfo=timezone.utc),
                        enddatum=datetime(2020, 4, 1, tzinfo=timezone.utc),
                    ),
                ),
                {
                    "positionen": [
                        {
                            "positionsbezeichnung": "testtring",
                            "positionsmenge": {"wert": "4000", "einheit": "KWH"},
                            "positionskosten": {"waehrung": "EUR", "wert": "98240"},
                            "positionspreis": {
                                "bezugswert": "KWH",
                                "status": None,
                                "wert": "0.2456000000000000127453603226967970840632915496826171875",
                                "einheit": "EUR",
                            },
                        },
                    ],
                    "lieferstellenangebotsteil": [
                        {
                            "marktlokationsId": "51238696781",
                            "sparte": "GAS",
                            "lokationsadresse": {
                                "postleitzahl": "82031",
                                "ort": "Grünwald",
                                "hausnummer": "27A",
                                "strasse": "Nördliche Münchner Straße",
                                "adresszusatz": None,
                                "postfach": None,
                                "coErgaenzung": None,
                                "landescode": "DE",
                            },
                            "energierichtung": "EINSP",
                            "bilanzierungsmethode": "PAUSCHAL",
                            "unterbrechbar": True,
                            "netzebene": "NSP",
                            "netzgebietsnr": None,
                            "versionstruktur": "2",
                            "katasterinformation": None,
                            "bilanzierungsgebiet": None,
                            "grundversorgercodenr": None,
                            "endkunde": None,
                            "geoadresse": None,
                            "verbrauchsart": None,
                            "netzbetreibercodenr": None,
                            "gebietstyp": None,
                            "gasqualitaet": None,
                            "zugehoerigeMesslokation": None,
                            "externeReferenzen": [],
                            "boTyp": "MARKTLOKATION",
                        }
                    ],
                    "gesamtmengeangebotsteil": {"wert": "4000", "einheit": "KWH"},
                    "gesamtkostenangebotsteil": {"waehrung": "EUR", "wert": "98240"},
                    "anfrageSubreferenz": "teststring",
                    "lieferzeitraum": {
                        "startdatum": "2020-01-01T00:00:00+00:00",
                        "endzeitpunkt": None,
                        "einheit": None,
                        "enddatum": "2020-04-01T00:00:00+00:00",
                        "startzeitpunkt": None,
                        "dauer": None,
                    },
                },
                id="maximal attributes",
            ),
            pytest.param(
                example_angebotsteil,
                example_angebotsteil_json,
                id="minimal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, angebotsteil, expected_json_dict):
        """
        Test de-/serialisation of Angebotsteil with minimal attributes.
        """
        assert_serialization_roundtrip(angebotsteil, AngebotsteilSchema(), expected_json_dict)

    def test_angebotsteil_positionen_required(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Angebotsteil(positionen=[])

        assert "List positionen must not be empty." in str(excinfo.value)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Angebotsteil()
        assert "missing 1 required" in str(excinfo.value)
