import pytest
from pydantic import ValidationError

from bo4e.bo.zeitreihe import Zeitreihe
from bo4e.enum.medium import Medium
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.messart import Messart
from bo4e.enum.messgroesse import Messgroesse
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_zeitreihenwert import example_zeitreihenwert


class TestZeitreihe:
    @pytest.mark.parametrize(
        "zeitreihe",
        [
            pytest.param(
                Zeitreihe(
                    bezeichnung="Foo",
                    beschreibung="Bar",
                    version="0.0.1",
                    messgroesse=Messgroesse.BLINDLEISTUNG,
                    messart=Messart.MAXIMALWERT,
                    medium=Medium.STROM,
                    einheit=Mengeneinheit.KVARH,
                    wertherkunft=Wertermittlungsverfahren.MESSUNG,
                    werte=[example_zeitreihenwert],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, zeitreihe: Zeitreihe) -> None:
        assert_serialization_roundtrip(zeitreihe)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitreihe()  # type: ignore[call-arg]

        assert "6 validation errors" in str(excinfo.value)
