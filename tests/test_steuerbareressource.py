import pytest

from bo4e import Marktrolle, SteuerbareRessource
from bo4e.bo.lokationszuordnung import Lokationszuordnung
from bo4e.com.konfigurationsprodukt import Konfigurationsprodukt
from bo4e.enum.steuerkanalleistungsbeschreibung import SteuerkanalLeistungsbeschreibung
from tests.serialization_helper import assert_serialization_roundtrip


class TestSteuerbareRessource:
    @pytest.mark.parametrize(
        "steuerbare_ressource",
        [
            pytest.param(
                SteuerbareRessource(
                    steuerbare_ressource_id="3784658734657",
                    steuerkanal_leistungsbeschreibung=SteuerkanalLeistungsbeschreibung.AN_AUS,
                    zugeordnete_msb_codenummer="1829371872392",
                    konfigurationsprodukte=[Konfigurationsprodukt()],
                    eigenschaft_msb_lokation=Marktrolle.LF,
                    lokationsbuendel_objektcode="9992 00000 125 6",
                    lokationszuordnungen=[Lokationszuordnung()],
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, steuerbare_ressource: SteuerbareRessource) -> None:
        """
        Test de-/serialisation of SteuerbareRessource.
        """
        assert_serialization_roundtrip(steuerbare_ressource)
