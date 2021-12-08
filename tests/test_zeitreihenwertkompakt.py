from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt, ZeitreihenwertkompaktSchema
from bo4e.enum.messwertstatus import Messwertstatus
from bo4e.enum.messwertstatuszusatz import Messwertstatuszusatz


class TestZeitreihenwertkompakt:
    def test_serialization(self):
        zrwk = Zeitreihenwertkompakt(
            wert=Decimal(1.5), status=Messwertstatus.ABGELESEN, statuszusatz=Messwertstatuszusatz.Z78_GERAETEWECHSEL
        )

        schema = ZeitreihenwertkompaktSchema()

        json_string = schema.dumps(zrwk, ensure_ascii=False)

        assert "1.5" in json_string
        assert "ABGELESEN" in json_string
        assert "Z78_GERAETEWECHSEL" in json_string
        deserialized_zrwk: Zeitreihenwertkompakt = schema.loads(json_string)

        assert isinstance(deserialized_zrwk.wert, Decimal)
        assert deserialized_zrwk.wert == Decimal(1.5)
        assert isinstance(deserialized_zrwk.status, Messwertstatus)
        assert deserialized_zrwk.status == Messwertstatus.ABGELESEN
        assert isinstance(deserialized_zrwk.statuszusatz, Messwertstatuszusatz)
        assert deserialized_zrwk.statuszusatz == Messwertstatuszusatz.Z78_GERAETEWECHSEL
        assert deserialized_zrwk == zrwk

    def test_wrong_datatype(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Zeitreihenwertkompakt(wert="1.5")

        assert "wert" in str(excinfo.value)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Zeitreihenwertkompakt(status=Messwertstatus.ABGELESEN)

        assert "missing 1 required" in str(excinfo.value)

    def test_only_required(self):
        zrwk = Zeitreihenwertkompakt(
            wert=Decimal(1.5),
        )

        schema = ZeitreihenwertkompaktSchema()

        json_string = schema.dumps(zrwk, ensure_ascii=False)

        assert "1.5" in json_string

        deserialized_zrwk: Zeitreihenwertkompakt = schema.loads(json_string)

        assert deserialized_zrwk == zrwk
