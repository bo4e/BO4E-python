import pytest

from bo4e import AufAbschlagProOrt, AufAbschlagstaffelProOrt
from tests.serialization_helper import assert_serialization_roundtrip


class TestAufAbschlagProOrt:
    @pytest.mark.parametrize(
        "aufabschlagproort",
        [
            pytest.param(
                AufAbschlagProOrt(
                    postleitzahl="01187",
                    ort="Dresden",
                    netznr="2",
                    staffeln=[AufAbschlagstaffelProOrt()],
                ),
            )
        ],
    )
    def test_serialization_roundtrip(
        self,
        aufabschlagproort: AufAbschlagProOrt,
    ) -> None:
        """
        Test de-/serialisation of AufAbschlagProOrt.
        """
        assert_serialization_roundtrip(aufabschlagproort)
