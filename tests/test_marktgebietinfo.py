from bo4e.com.marktgebietinfo import MarktgebietInfo


class TestMarktgebietinfo:
    def test_serialization(self) -> None:
        mgi = MarktgebietInfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B")

        json_string = mgi.json(by_alias=True, ensure_ascii=False)

        assert "marktgebiet" in json_string, "No camel case serialization"

        deserialized_mgi: MarktgebietInfo = MarktgebietInfo.parse_raw(json_string)

        assert mgi == deserialized_mgi
