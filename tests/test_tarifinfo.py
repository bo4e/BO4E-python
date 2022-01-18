import pytest  # type:ignore[import]

from bo4e.bo.tarifinfo import Tarifinfo, TarifinfoSchema
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.tarifmerkmal import Tarifmerkmal
from bo4e.enum.tariftyp import Tariftyp
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_energiemix import example_energiemix  # type:ignore[import]
from tests.test_marktteilnehmer import example_marktteilnehmer  # type:ignore[import]
from tests.test_vertragskonditionen import example_vertragskonditionen  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestTarifinfo:
    @pytest.mark.parametrize(
        "tarifinfo",
        [
            pytest.param(
                Tarifinfo(
                    bezeichnung="foo",
                    anbietername="der beste stromanbieter",
                    sparte=Sparte.STROM,
                    kundentypen=[Kundentyp.PRIVAT, Kundentyp.GEWERBE],
                    tarifart=Tarifart.MEHRTARIF,
                    tariftyp=Tariftyp.GRUND_ERSATZVERSORGUNG,
                    tarifmerkmale=[Tarifmerkmal.HEIZSTROM],
                    website="https://foo.inv",
                    bemerkung="super billig aber auch super dreckig",
                    vertragskonditionen=example_vertragskonditionen,
                    zeitliche_gueltigkeit=example_zeitraum,
                    energiemix=example_energiemix,
                    anbieter=example_marktteilnehmer,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifinfo: Tarifinfo):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifinfo, TarifinfoSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Tarifinfo()

        assert "missing 8 required" in str(excinfo.value)
