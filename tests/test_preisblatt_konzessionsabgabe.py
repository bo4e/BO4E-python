import pytest  # type:ignore[import]
from pydantic import ValidationError

from bo4e.bo.preisblattkonzessionsabgabe import PreisblattKonzessionsabgabe
from bo4e.enum.kundengruppeka import KundengruppeKA
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_marktteilnehmer import example_marktteilnehmer  # type:ignore[import]
from tests.test_preisposition import example_preisposition  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestPreisblatt:
    @pytest.mark.parametrize(
        "preisblatt_ka",
        [
            pytest.param(
                PreisblattKonzessionsabgabe(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=example_marktteilnehmer,
                    kundengruppe_k_a=KundengruppeKA.G_SONDERKUNDE,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_ka: PreisblattKonzessionsabgabe) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_ka)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = PreisblattKonzessionsabgabe()  # type: ignore[call-arg]
        assert "6 validation errors" in str(excinfo.value)  # 5 from preisblatt + 1 from preisblatt konzessionsabgabe
