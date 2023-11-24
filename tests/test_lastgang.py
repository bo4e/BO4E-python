import pytest
from _decimal import Decimal
from pydantic import ValidationError

from bo4e.bo.lastgang import Lastgang
from bo4e.bo.marktlokation import Marktlokation
from bo4e.bo.messlokation import Messlokation
from bo4e.com.adresse import Adresse
from bo4e.com.menge import Menge
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_zeitreihenwert import example_zeitreihenwert


class TestLastgang:
    @pytest.mark.parametrize(
        "lastgang_kompakt",
        [
            pytest.param(
                Lastgang(
                    version="1.1",
                    sparte=Sparte.STROM,
                    obis_kennzahl="1-0:1.8.1",
                    messgroesse=Mengeneinheit.KWH,
                    werte=[example_zeitreihenwert],
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
    def test_serialization_roundtrip(self, lastgang_kompakt: Lastgang) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(lastgang_kompakt)
