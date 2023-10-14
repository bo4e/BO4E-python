import pytest

from bo4e import Lastgang, Lokationstyp, Mengeneinheit, Sparte, Zeitreihenwert
from tests.serialization_helper import assert_serialization_roundtrip


class TestLastgang:
    @pytest.mark.parametrize(
        "lastgang_kompakt",
        [
            pytest.param(
                Lastgang(
                    version="1.1",
                    sparte=Sparte.STROM,
                    lokations_id="DE0000011111222223333344444555556",
                    obis_kennzahl="1-0:1.8.1",
                    lokationstyp=Lokationstyp.MELO,
                    messgroesse=Mengeneinheit.KWH,
                    werte=[Zeitreihenwert()],
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, lastgang_kompakt: Lastgang) -> None:
        """
        Test de-/serialisation of Lastgang Kompakt.
        """
        assert_serialization_roundtrip(lastgang_kompakt)
