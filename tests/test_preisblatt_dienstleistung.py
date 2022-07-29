import pytest
from pydantic import ValidationError

from bo4e.bo.preisblattdienstleistung import PreisblattDienstleistung
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_geraeteeigenschaften import example_geraeteeigenschaften
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_preisposition import example_preisposition
from tests.test_zeitraum import example_zeitraum


class TestPreisblattDienstleistung:
    @pytest.mark.parametrize(
        "preisblatt_dienstleistung",
        [
            pytest.param(
                PreisblattDienstleistung(
                    bezeichnung="foo",
                    sparte=Sparte.STROM,
                    preisstatus=Preisstatus.ENDGUELTIG,
                    preispositionen=[example_preisposition],
                    gueltigkeit=example_zeitraum,
                    herausgeber=example_marktteilnehmer,
                    bilanzierungsmethode=Bilanzierungsmethode.TLP_GEMEINSAM,
                    basisdienstleistung=Dienstleistungstyp.ABLESUNG_MONATLICH,
                    inklusive_dienstleistungen=[Dienstleistungstyp.AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB],
                    geraetedetails=example_geraeteeigenschaften,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisblatt_dienstleistung: PreisblattDienstleistung) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_dienstleistung)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = PreisblattDienstleistung()  # type: ignore[call-arg]
        assert "7 validation errors" in str(excinfo.value)  # 5 from preisblatt + 2 from preisblatt dienstleistung
