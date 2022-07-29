import pytest
from pydantic import ValidationError

from bo4e.bo.preisblattnetznutzung import PreisblattNetznutzung
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.kundengruppe import Kundengruppe
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_preisposition import example_preisposition
from tests.test_zeitraum import example_zeitraum


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
    def test_serialization_roundtrip(self, preisblatt_netznutzung: PreisblattNetznutzung) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_netznutzung)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = PreisblattNetznutzung()  # type: ignore[call-arg]
        assert "8 validation errors" in str(excinfo.value)  # 5 from preisblatt + 3 from preisblatt netznutzung
