from bo4e.com.marktgebietinfo import MarktgebietInfo


class TestMarktgebietinfo:
    def test_serialization(self) -> None:
        mgi = MarktgebietInfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B")

        json_string = mgi.model_dump_json(by_alias=True)

        assert "marktgebiet" in json_string, "No camel case serialization"

        deserialized_mgi: MarktgebietInfo = MarktgebietInfo.model_validate_json(json_string)

        assert mgi == deserialized_mgi
