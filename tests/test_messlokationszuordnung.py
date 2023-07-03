from datetime import datetime

from bo4e.com.messlokationszuordnung import Messlokationszuordnung
from bo4e.enum.arithmetische_operation import ArithmetischeOperation


class TestMesslokationszuordnung:
    def test_serialisation_only_required_attributes(self) -> None:
        """
        Test serialisation of Messlokationszuordnung with required attributes only
        """
        messlokations_id = "DE0010688516810000000000000012345"

        mlz = Messlokationszuordnung(
            messlokations_id=messlokations_id,
            arithmetik=ArithmetischeOperation.ADDITION,
        )

        json_string = mlz.model_dump_json(by_alias=True)

        assert messlokations_id in json_string
        assert "ADDITION" in json_string

        mlz_deserialized = Messlokationszuordnung.model_validate_json(json_string)

        assert mlz_deserialized.messlokations_id == messlokations_id
        assert mlz_deserialized.arithmetik == ArithmetischeOperation.ADDITION

    def test_serialisation_required_and_optional_attributes(self) -> None:
        """
        Test serialisation of Messlokationszuordnung with required and optional attributes
        """
        messlokations_id = "DE0010688516810000000000000012345"

        mlz = Messlokationszuordnung(
            messlokations_id=messlokations_id,
            arithmetik=ArithmetischeOperation.ADDITION,
            gueltig_seit=datetime(year=2021, month=1, day=13),
            gueltig_bis=datetime(year=2021, month=5, day=4),
        )

        mlz_json = mlz.model_dump_json(by_alias=True)

        # CamelCase keys are made because they will put into JSON strings
        # to send them to the frontend (= JavaScript land)
        assert "messlokationsId" in mlz_json
        assert messlokations_id in mlz_json
        assert "arithmetik" in mlz_json
        assert "ADDITION" in mlz_json
        assert "gueltigSeit" in mlz_json
        assert "2021-01-13T00:00:00" in mlz_json

        mlz_deserialized = Messlokationszuordnung.model_validate_json(mlz_json)

        assert mlz_deserialized.messlokations_id == messlokations_id
        assert mlz_deserialized.arithmetik == ArithmetischeOperation.ADDITION
        assert mlz_deserialized.gueltig_seit == datetime(year=2021, month=1, day=13)
        assert mlz_deserialized.gueltig_bis == datetime(year=2021, month=5, day=4)
