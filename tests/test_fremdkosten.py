import pytest
from pydantic import ValidationError

from bo4e.bo.fremdkosten import Fremdkosten
from bo4e.com.fremdkostenblock import Fremdkostenblock
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_betrag import example_betrag
from tests.test_zeitraum import example_zeitraum


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
    def test_serialization_roundtrip(self, fremdkosten: Fremdkosten) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(fremdkosten)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Fremdkosten()  # type: ignore[call-arg]
        assert "1 validation error" in str(excinfo.value)
