import pytest

from bo4e import Katasteradresse
from tests.serialization_helper import assert_serialization_roundtrip


class TestKatasteradresse:
    @pytest.mark.parametrize(
        "katasteradresse",
        [
            pytest.param(
                Katasteradresse(gemarkung_flur="hello", flurstueck="world"), id="all attributes at first level"
            ),
        ],
    )
    def test_serialization_roundtrip(self, katasteradresse: Katasteradresse) -> None:
        """
        Test de-/serialisation of Katasteradresse.
        """

        assert_serialization_roundtrip(katasteradresse)
