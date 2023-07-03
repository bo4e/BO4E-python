from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt
from bo4e.enum.messwertstatus import Messwertstatus
from bo4e.enum.messwertstatuszusatz import Messwertstatuszusatz


class TestZeitreihenwertkompakt:
    def test_serialization(self) -> None:
        zrwk = Zeitreihenwertkompakt(
            wert=Decimal(1.5), status=Messwertstatus.ABGELESEN, statuszusatz=Messwertstatuszusatz.Z78_GERAETEWECHSEL
        )

        json_string = zrwk.model_dump_json(by_alias=True)

        assert "1.5" in json_string
        assert "ABGELESEN" in json_string
        assert "Z78_GERAETEWECHSEL" in json_string
        deserialized_zrwk: Zeitreihenwertkompakt = Zeitreihenwertkompakt.model_validate_json(json_string)

        assert isinstance(deserialized_zrwk.wert, Decimal)
        assert deserialized_zrwk.wert == Decimal(1.5)
        assert isinstance(deserialized_zrwk.status, Messwertstatus)
        assert deserialized_zrwk.status == Messwertstatus.ABGELESEN
        assert isinstance(deserialized_zrwk.statuszusatz, Messwertstatuszusatz)
        assert deserialized_zrwk.statuszusatz == Messwertstatuszusatz.Z78_GERAETEWECHSEL
        assert deserialized_zrwk == zrwk

    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitreihenwertkompakt(wert="helloooo")  # type: ignore[arg-type]

        assert "wert" in str(excinfo.value)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitreihenwertkompakt(status=Messwertstatus.ABGELESEN)  # type: ignore[call-arg]

        assert "1 validation error" in str(excinfo.value)

    def test_only_required(self) -> None:
        zrwk = Zeitreihenwertkompakt(
            wert=Decimal(1.5),
        )

        json_string = zrwk.model_dump_json(by_alias=True)

        assert "1.5" in json_string

        deserialized_zrwk: Zeitreihenwertkompakt = Zeitreihenwertkompakt.model_validate_json(json_string)

        assert deserialized_zrwk == zrwk
