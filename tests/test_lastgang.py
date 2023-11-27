import pytest
from _decimal import Decimal

from bo4e import (
    Adresse,
    Bilanzierungsmethode,
    Energierichtung,
    Lastgang,
    Marktlokation,
    Menge,
    Mengeneinheit,
    Messlokation,
    Netzebene,
    Sparte,
    Zeitreihenwert,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestLastgang:
    @pytest.mark.parametrize(
        "lastgang",
        [
            pytest.param(
                Lastgang(
                    version="1.1",
                    sparte=Sparte.STROM,
                    obis_kennzahl="1-0:1.8.1",
                    messgroesse=Mengeneinheit.KWH,
                    werte=[Zeitreihenwert()],
                    marktlokation=Marktlokation(
                        marktlokations_id="51238696781",
                        sparte=Sparte.GAS,
                        lokationsadresse=Adresse(
                            postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"
                        ),
                        energierichtung=Energierichtung.EINSP,
                        bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
                        netzebene=Netzebene.NSP,
                    ),
                    messlokation=Messlokation(
                        messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
                        sparte=Sparte.STROM,
                    ),
                    zeit_intervall_laenge=Menge(wert=Decimal(1.0), einheit=Mengeneinheit.VIERTEL_STUNDE),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, lastgang: Lastgang) -> None:
        """
        Test de-/serialisation of Lastgang.
        """
        assert_serialization_roundtrip(lastgang)
