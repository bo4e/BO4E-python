from bo4e.com.marktgebietinfo import Marktgebietinfo, MarktgebietinfoSchema


class TestMarktgebietinfo:
    def test_serialization(self):
        mgi = Marktgebietinfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B")

        schema = MarktgebietinfoSchema()

        json_string = schema.dumps(mgi, ensure_ascii=False)

        assert "marktgebiet" in json_string, "No camel case serialization"

        deserialized_mgi: Marktgebietinfo = schema.loads(json_string)

        assert mgi.marktgebiet == deserialized_mgi.marktgebiet
