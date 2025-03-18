from datetime import datetime

import pytest
from _decimal import Decimal

from bo4e.com.abweichung import Abweichung
from bo4e.com.abweichungsposition import Abweichungsposition
from bo4e.com.avisposition import Avisposition
from bo4e.com.betrag import Betrag
from bo4e.com.rueckmeldungsposition import Rueckmeldungsposition
from bo4e.enum.abweichungsgrund import Abweichungsgrund
from bo4e.enum.waehrungscode import Waehrungscode
from tests.serialization_helper import assert_serialization_roundtrip


class TestAvisposition:
    @pytest.mark.parametrize(
        "avisposition",
        [
            pytest.param(
                Avisposition(
                    rechnungs_nummer="12345",
                    rechnungs_datum=datetime(2022, 1, 1, 0, 0, 0),
                    ist_storno=True,
                    gesamtbrutto=Betrag(
                        wert=Decimal(100.5),
                        waehrung=Waehrungscode.EUR,
                    ),
                    zu_zahlen=Betrag(
                        wert=Decimal(15.5),
                        waehrung=Waehrungscode.EUR,
                    ),
                    ist_selbstausgestellt=True,
                    referenz="1234",
                    abweichungen=[
                        Abweichung(
                            abweichungsgrund=Abweichungsgrund.UNBEKANNTE_MARKTLOKATION_MESSLOKATION,
                            abweichungsgrund_bemerkung="sonst",
                            zugehoerige_rechnung="458011",
                            abschlagsrechnung="4580112",
                            abweichungsgrund_code="14",
                            abweichungsgrund_codeliste="G_0081",
                        ),
                    ],
                    positionen=[
                        Rueckmeldungsposition(
                            positionsnummer="1",
                            abweichungspositionen=[
                                Abweichungsposition(
                                    abweichungsgrund_code="foo",
                                    abweichungsgrund_codeliste="foo",
                                    abweichungsgrund_bemerkung="foo",
                                    zugehoerige_rechnung="458011",
                                    zugehoerige_bestellung="foo",
                                ),
                            ],
                        ),
                    ],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, avisposition: Avisposition) -> None:
        """
        Test de-/serialisation of Avisposition.
        """
        assert_serialization_roundtrip(avisposition)
