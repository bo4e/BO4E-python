import pytest  # type:ignore[import]
from pydantic import ValidationError

from bo4e.bo.preisblatt import Preisblatt
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_marktteilnehmer import example_marktteilnehmer  # type:ignore[import]
from tests.test_preisposition import example_preisposition  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestPreisblatt:
    @pytest.mark.parametrize(
        "preisblatt",
        [
            pytest.param(
                Preisblatt(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=example_marktteilnehmer,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt: Preisblatt) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Preisblatt()  # type: ignore[call-arg]
        assert "5 validation errors" in str(excinfo.value)
