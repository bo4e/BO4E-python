from bo4e.com.standorteigenschaftengas import StandorteigenschaftenGas, StandorteigenschaftenGasSchema


class TestStandorteigenschaftenGas:
    @pytest.mark.parameterize("")
    def test_serialization(self):
        seg = StandorteigenschaftenGas(netzkontonummern=[])
