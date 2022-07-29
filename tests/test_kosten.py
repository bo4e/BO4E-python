import pytest
from pydantic import ValidationError

from bo4e.bo.kosten import Kosten
from bo4e.com.kostenblock import Kostenblock
from bo4e.enum.kostenklasse import Kostenklasse
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_betrag import example_betrag
from tests.test_zeitraum import example_zeitraum

example_kosten = Kosten(
    kostenklasse=Kostenklasse.FREMDKOSTEN,
    gueltigkeit=example_zeitraum,
    kostenbloecke=[
        Kostenblock(
            kostenblockbezeichnung="Mein Kostenblock",
        )
    ],
    summe_kosten=[example_betrag],
)


class TestKosten:
    @pytest.mark.parametrize(
        "kosten",
        [
            pytest.param(
                example_kosten,
                id="maximal attributes",
            )
        ],
    )
    def test_serialization_roundtrip(self, kosten: Kosten) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(kosten)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Kosten()  # type: ignore[call-arg]
        assert "3 validation errors" in str(excinfo.value)
