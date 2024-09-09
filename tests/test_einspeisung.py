import pytest

from bo4e import Geschaeftspartnerrolle, Landescode
from bo4e.bo.einspeisung import Einspeisung
from bo4e.enum.eeg_vermarktungsform import EEGVermarktungsform
from bo4e.enum.fernsteuerbarkeit_status import FernsteuerbarkeitStatus
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
                    landescode=Landescode.DE,  # type:ignore[attr-defined]
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
