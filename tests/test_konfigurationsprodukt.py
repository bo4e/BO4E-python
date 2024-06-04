import pytest

from bo4e import Konfigurationsprodukt, Marktteilnehmer
from tests.serialization_helper import assert_serialization_roundtrip


class TestKonfigurationsprodukt:
    @pytest.mark.parametrize(
        "konfigurationsprodukt",
        [
            pytest.param(
                Konfigurationsprodukt(
                    produktcode="1212121212",
                    leistungskurvendefinition="",
                    schaltzeitdefinition="",
                    marktpartner=Marktteilnehmer(),
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, konfigurationsprodukt: Konfigurationsprodukt) -> None:
        """
        Test de-/serialisation of Konfigurationsprodukt.
        """

        assert_serialization_roundtrip(konfigurationsprodukt)
