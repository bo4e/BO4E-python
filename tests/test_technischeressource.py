from decimal import Decimal

import pytest

from bo4e import (
    EMobilitaetsart,
    Erzeugungsart,
    Lokationszuordnung,
    Menge,
    Speicherart,
    TechnischeRessource,
    TechnischeRessourceNutzung,
    TechnischeRessourceVerbrauchsart,
    Waermenutzung,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestTechnischeRessource:
    @pytest.mark.parametrize(
        "technische_ressource",
        [
            pytest.param(
                TechnischeRessource(
                    technische_ressource_id="3784658734657",
                    vorgelagerte_messlokation_id="37846587343434",
                    zugeordnete_marktlokation_id="12242432423",
                    zugeordnete_steuerbare_ressource_id="281238912739",
                    nennleistungaufnahme=Menge(wert=Decimal(1000.0)),
                    nennleistungabgabe=Menge(wert=Decimal(1000.0)),
                    speicherkapazitaet=Menge(wert=Decimal(1000.0)),
                    technische_ressource_nutzung=TechnischeRessourceNutzung.SPEICHER,
                    technische_ressource_verbrauchsart=TechnischeRessourceVerbrauchsart.KRAFT_LICHT,
                    waermenutzung=Waermenutzung.SPEICHERHEIZUNG,
                    emobilitaetsart=EMobilitaetsart.WALLBOX,
                    erzeugungsart=Erzeugungsart.WIND,
                    speicherart=Speicherart.WASSERSTOFFSPEICHER,
                    lokationsbuendel_objektcode="9992 00000 125 6",
                    lokationszuordnungen=[Lokationszuordnung()],
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, technische_ressource: TechnischeRessource) -> None:
        """
        Test de-/serialisation of TechnischeRessource.
        """
        assert_serialization_roundtrip(technische_ressource)
