import pytest

from build.lib.bo4e.enum.landescode import Landescode
from src.bo4e import Geschaeftspartnerrolle
from src.bo4e.bo.einspeisung import Einspeisung
from src.bo4e.enum.eeg_vermarktungsform import EEGVermarktungsform
from src.bo4e.enum.fernsteuerbarkeit_status import FernsteuerbarkeitStatus
from tests.serialization_helper import assert_serialization_roundtrip


class TestEinspeisung:
    @pytest.mark.parametrize(
        "einspeisung",
        [
            pytest.param(
                Einspeisung(
                    marktlokations_id="teststring",
                    tranchen_id="teststring",
                    verguetungsempfaenger=Geschaeftspartnerrolle.LIEFERANT,
                    eeg_vermarktungsform=EEGVermarktungsform.KWKG_VERGUETUNG,
                    landescode=Landescode.DE,
                    fernsteuerbarkeit_status=FernsteuerbarkeitStatus.NICHT_FERNSTEUERBAR,
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, einspeisung: Einspeisung) -> None:
        """
        Test de-/serialisation of Einspeisung
        """
        assert_serialization_roundtrip(einspeisung)
