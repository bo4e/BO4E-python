import pytest

from bo4e import Adresse, Geschaeftspartnerrolle, Marktrolle, Marktteilnehmer, Rollencodetyp, Sparte
from tests.serialization_helper import assert_serialization_roundtrip


class TestMarktteilnehmer:
    @pytest.mark.parametrize(
        "marktteilnehmer",
        [
            pytest.param(
                Marktteilnehmer(
                    marktrolle=Marktrolle.DL,
                    rollencodenummer="9903916000000",
                    rollencodetyp=Rollencodetyp.BDEW,
                    sparte=Sparte.STROM,
                    name1="Netze BW GmbH",
                    ist_gewerbe=True,
                    geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
                    partneradresse=Adresse(),
                )
            )
        ],
    )
    def test_serialization_roundtrip(self, marktteilnehmer: Marktteilnehmer) -> None:
        """
        Test de-/serialisation of Marktteilnehmer.
        """

        assert_serialization_roundtrip(marktteilnehmer)
