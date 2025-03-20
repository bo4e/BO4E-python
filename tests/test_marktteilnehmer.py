import pytest

from bo4e import Geschaeftspartner, Marktrolle, Marktteilnehmer, Rollencodetyp, Sparte
from tests.serialization_helper import assert_serialization_roundtrip


class TestMarktteilnehmer:
    @pytest.mark.parametrize(
        "marktteilnehmer",
        [
            pytest.param(
                Marktteilnehmer(
                    marktrolle=Marktrolle.DP,
                    rollencodenummer="9903916000000",
                    rollencodetyp=Rollencodetyp.BDEW,
                    sparte=Sparte.STROM,
                    makoadresse=["stringadressewarum", "as4adresse"],
                    geschaeftspartner=Geschaeftspartner(),
                )
            )
        ],
    )
    def test_serialization_roundtrip(self, marktteilnehmer: Marktteilnehmer) -> None:
        """
        Test de-/serialisation of Marktteilnehmer.
        """

        assert_serialization_roundtrip(marktteilnehmer)
