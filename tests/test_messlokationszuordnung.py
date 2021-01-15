from bo4e.com.messlokationszuordnung import (
    Messlokationszuordnung,
    MesslokationszuordnungSchema,
)
from bo4e.enum.arithmetische_operation import ArithmetischeOperation
from datetime import datetime


class TestMesslokationszuordnung:
    def test_serialisation_only_required_attributes(self):
        """
        Test serialisation of Messlokationszuordnung with required attributes only
        """
        messlokations_id = "DE0010688516810000000000000012345"

        mlz = Messlokationszuordnung(
            messlokations_id=messlokations_id,
            arithmetik=ArithmetischeOperation.ADDITION,
        )

        schema = MesslokationszuordnungSchema()
        json_string = schema.dumps(mlz, ensure_ascii=False)

        assert messlokations_id in json_string
        assert "ADDITION" in json_string

        mlz_deserialised = schema.loads(json_string)

        assert mlz_deserialised.messlokations_id == messlokations_id
        assert mlz_deserialised.arithmetik == ArithmetischeOperation.ADDITION

    def test_serialisation_required_and_optional_attributes(self):
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

        schema = MesslokationszuordnungSchema()
        mlz_dict = schema.dump(mlz)

        # CamelCase keys are made because they will put into JSON strings
        # to send them to the frontend (= JavaScript land)
        assert mlz_dict["messlokationsId"] == messlokations_id
        assert mlz_dict["arithmetik"] == "ADDITION"
        assert mlz_dict["gueltigSeit"] == "2021-01-13T00:00:00"

        mlz_deserialised = schema.load(mlz_dict)

        assert mlz_deserialised.messlokations_id == messlokations_id
        assert mlz_deserialised.arithmetik == ArithmetischeOperation.ADDITION
        assert mlz_deserialised.gueltig_seit == datetime(year=2021, month=1, day=13)
        assert mlz_deserialised.gueltig_bis == datetime(year=2021, month=5, day=4)
