import pytest

from bo4e import (
    Konfigurationsprodukt,
    Lokationszuordnung,
    Marktrolle,
    Menge,
    Netzlokation,
    Sparte,
    Verwendungszweck,
    VerwendungszweckProMarktrolle,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestNetzlokation:
    @pytest.mark.parametrize(
        "netzlokation",
        [
            pytest.param(
                Netzlokation(
                    netzlokations_id="3784658734657",
                    sparte=Sparte.GAS,
                    netzanschlussleistung=Menge(),
                    grundzustaendiger_msb_codenr="1829371872392",
                    steuerkanal=False,
                    obiskennzahl="82376487236",
                    verwendungszweck=VerwendungszweckProMarktrolle(
                        marktrolle=Marktrolle.LF,
                        Zwecke=[Verwendungszweck.BILANZKREISABRECHNUNG],
                    ),
                    konfigurationsprodukte=[Konfigurationsprodukt()],
                    eigenschaft_msb_lokation=Marktrolle.LF,
                    lokationsbuendel_objektcode="9992 00000 125 6",
                    lokationszuordnungen=[Lokationszuordnung()],
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, netzlokation: Netzlokation) -> None:
        """
        Test de-/serialisation of Netzlokation.
        """
        assert_serialization_roundtrip(netzlokation)
