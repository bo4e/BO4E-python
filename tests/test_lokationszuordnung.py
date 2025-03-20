import pytest

from bo4e import (
    Lokationszuordnung,
    Marktlokation,
    Messlokation,
    Netzlokation,
    SteuerbareRessource,
    TechnischeRessource,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestLokationszuordnung:
    @pytest.mark.parametrize(
        "lokationszuordnung",
        [
            pytest.param(
                Lokationszuordnung(
                    marktlokationen=[Marktlokation()],
                    messlokationen=[Messlokation()],
                    netzlokationen=[Netzlokation()],
                    technische_ressourcen=[TechnischeRessource()],
                    steuerbare_ressourcen=[SteuerbareRessource()],
                    gueltigkeit=Zeitraum(),
                    zuordnungstyp="Zuordnungstyp",
                    lokationsbuendelcode="9992 00000 125 6",
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, lokationszuordnung: Lokationszuordnung) -> None:
        """
        Test de-/serialisation of Lokationszuordnung.
        """
        assert_serialization_roundtrip(lokationszuordnung)
