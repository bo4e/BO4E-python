import datetime

import pytest
from pydantic import ValidationError

from bo4e.bo.tarifpreisblatt import Tarifpreisblatt
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.tarifmerkmal import Tarifmerkmal
from bo4e.enum.tariftyp import Tariftyp
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_aufabschlag import example_aufabschlag
from tests.test_energiemix import example_energiemix
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_preisgarantie import example_preisgarantie
from tests.test_tarifpreisposition import example_tarifpreisposition
from tests.test_vertragskonditionen import example_vertragskonditionen
from tests.test_zeitraum import example_zeitraum


class TestTarifpreisblatt:
    @pytest.mark.parametrize(
        "tarifpreisblatt",
        [
            pytest.param(
                Tarifpreisblatt(
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
                    # ^^ above is all copy pasted from Tarifinfo BO
                    # vv below are the attributes of tarifpreisblatt
                    preisstand=datetime.datetime(2022, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
                    berechnungsparameter=Tarifberechnungsparameter(),
                    tarif_auf_abschlaege=[example_aufabschlag],
                    tarifpreise=[example_tarifpreisposition],
                    preisgarantie=example_preisgarantie,
                    tarifeinschraenkung=Tarifeinschraenkung(),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreisblatt: Tarifpreisblatt) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifpreisblatt)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Tarifpreisblatt()  # type: ignore[call-arg]
        assert "11 validation error" in str(excinfo.value)  # 8 from tarifinfo + 3 from tarifpreisblatt
