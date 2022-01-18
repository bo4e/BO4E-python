import pytest  # type:ignore[import]

from bo4e.bo.kosten import Kosten, KostenSchema
from bo4e.com.kostenblock import Kostenblock
from bo4e.enum.kostenklasse import Kostenklasse
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_betrag import example_betrag  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestKosten:
    @pytest.mark.parametrize(
        "kosten",
        [
            pytest.param(
                Kosten(
                    kostenklasse=Kostenklasse.FREMDKOSTEN,
                    gueltigkeit=example_zeitraum,
                    kostenbloecke=[
                        Kostenblock(
                            kostenblockbezeichnung="Mein Kostenblock",
                        )
                    ],
                    summe_kosten=[example_betrag],
                ),
                id="maximal attributes",
            )
        ],
    )
    def test_serialization_roundtrip(self, kosten: Kosten):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(kosten, KostenSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Kosten()
        assert "missing 3 required" in str(excinfo.value)
