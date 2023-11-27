import pytest

from bo4e import Adresse, Dienstleistung, Geraet, Messlokation, Netzebene, Sparte, Zaehler
from tests.serialization_helper import assert_serialization_roundtrip


class TestMeLo:
    @pytest.mark.parametrize(
        "melo",
        [
            pytest.param(
                Messlokation(
                    messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
                    sparte=Sparte.STROM,
                    netzebene_messung=Netzebene.MSP,
                    messgebietnr="664073",
                    geraete=[
                        Geraet(),
                        Geraet(),
                    ],
                    messdienstleistung=[
                        Dienstleistung(),
                        Dienstleistung(),
                    ],
                    messlokationszaehler=[Zaehler()],
                    grundzustaendiger_msb_codenr="9910125000002",
                    messadresse=Adresse(),
                )
            )
        ],
    )
    def test_serialization_roundtrip(self, melo: Messlokation) -> None:
        """
        Test de-/serialisation of Messlokation.
        """

        assert_serialization_roundtrip(melo)
