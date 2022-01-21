import pytest  # type:ignore[import]

from bo4e.bo.fremdkosten import Fremdkosten, FremdkostenSchema
from bo4e.com.fremdkostenblock import Fremdkostenblock
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_betrag import example_betrag  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestFremdkosten:
    @pytest.mark.parametrize(
        "fremdkosten",
        [
            pytest.param(
                Fremdkosten(
                    gueltigkeit=example_zeitraum,
                    summe_kosten=example_betrag,
                    kostenbloecke=[Fremdkostenblock(kostenblockbezeichnung="teststring")],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, fremdkosten: Fremdkosten):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(fremdkosten, FremdkostenSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Fremdkosten()
        assert "missing 1 required" in str(excinfo.value)
