import pytest  # type:ignore[import]

from bo4e.bo.preisblattnetznutzung import PreisblattNetznutzung, PreisblattNetznutzungSchema
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.kundengruppe import Kundengruppe
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_marktteilnehmer import example_marktteilnehmer  # type:ignore[import]
from tests.test_preisposition import example_preisposition  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestPreisblatt:
    @pytest.mark.parametrize(
        "preisblatt_netznutzung",
        [
            pytest.param(
                PreisblattNetznutzung(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=example_marktteilnehmer,
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    netzebene=Netzebene.MSP,
                    kundengruppe=Kundengruppe.SLP_G_GKO,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_netznutzung: PreisblattNetznutzung):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_netznutzung, PreisblattNetznutzungSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = PreisblattNetznutzung()
        assert "missing 8 required" in str(excinfo.value)  # 5 from preisblatt + 3 from preisblatt netznutzung
