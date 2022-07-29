import pytest
from pydantic import ValidationError

from bo4e.bo.preisblattmessung import PreisblattMessung
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_geraeteeigenschaften import example_geraeteeigenschaften
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_preisposition import example_preisposition
from tests.test_zeitraum import example_zeitraum


class TestPreisblattMessung:
    @pytest.mark.parametrize(
        "preisblatt_messung",
        [
            pytest.param(
                PreisblattMessung(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=example_marktteilnehmer,
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    messebene=Netzebene.MSP,
                    inklusive_dienstleistungen=[Dienstleistungstyp.AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB],
                    zaehler=example_geraeteeigenschaften,
                    inklusive_geraete=[example_geraeteeigenschaften],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_messung: PreisblattMessung) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_messung)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = PreisblattMessung()  # type: ignore[call-arg]
        assert "8 validation errors" in str(excinfo.value)  # 5 from preisblatt + 3 from preisblatt messung
