import pytest

from bo4e import (
    Adresse,
    Bilanzierungsmethode,
    Energierichtung,
    Geschaeftspartner,
    Kundentyp,
    Marktlokation,
    Netzebene,
    Sparte,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestMaLo:
    @pytest.mark.parametrize(
        "marktlokation",
        [
            pytest.param(
                Marktlokation(
                    marktlokations_id="51238696781",
                    sparte=Sparte.GAS,
                    lokationsadresse=Adresse(),
                    energierichtung=Energierichtung.EINSP,
                    bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
                    ist_unterbrechbar=True,  # optional attribute
                    netzebene=Netzebene.NSP,
                    endkunde=Geschaeftspartner(),
                    kundengruppen=[Kundentyp.GEWERBE, Kundentyp.PRIVAT],
                )
            )
        ],
    )
    def test_serialization_roundtrip(self, marktlokation: Marktlokation) -> None:
        """
        Test de-/serialisation of Marktlokation.
        """

        assert_serialization_roundtrip(marktlokation)
