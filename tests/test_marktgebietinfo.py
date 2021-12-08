from bo4e.com.marktgebietinfo import MarktgebietInfo, MarktgebietInfoSchema


class TestMarktgebietinfo:
    def test_serialization(self):
        mgi = MarktgebietInfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B")

        schema = MarktgebietInfoSchema()

        json_string = schema.dumps(mgi, ensure_ascii=False)

        assert "marktgebiet" in json_string, "No camel case serialization"

        deserialized_mgi: MarktgebietInfo = schema.loads(json_string)

        assert mgi == deserialized_mgi
