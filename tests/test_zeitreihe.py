import pytest
from pydantic import ValidationError

from bo4e import Medium, Mengeneinheit, Messart, Messgroesse, Wertermittlungsverfahren, Zeitreihe
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
