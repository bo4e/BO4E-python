import pytest  # type:ignore[import]

from bo4e.bo.preisblattdienstleistung import PreisblattDienstleistung, PreisblattDienstleistungSchema
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_geraeteeigenschaften import example_geraeteeigenschaften  # type:ignore[import]
from tests.test_marktteilnehmer import example_marktteilnehmer  # type:ignore[import]
from tests.test_preisposition import example_preisposition  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


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
    def test_serialization_roundtrip(self, preisblatt_dienstleistung: PreisblattDienstleistung):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(preisblatt_dienstleistung, PreisblattDienstleistungSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = PreisblattDienstleistung()
        assert "missing 7 required" in str(excinfo.value)  # 5 from preisblatt + 2 from preisblatt dienstleistung
