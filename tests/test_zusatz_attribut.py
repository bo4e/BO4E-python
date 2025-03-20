from __future__ import annotations

import pytest

from bo4e import Anrede, Organisationstyp, Titel
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.bo.person import Person
from bo4e.com.adresse import Adresse
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.zusatzattribut import ZusatzAttribut
from tests.serialization_helper import assert_serialization_roundtrip


class TestZusatzAttribut:
    @pytest.mark.parametrize(
        "geschaeftspartner",
        [
            pytest.param(
                Geschaeftspartner(
                    zusatz_attribute=[
                        ZusatzAttribut(name="SAP GP Nummer", wert="0123456789"),
                        ZusatzAttribut(name="Schufa-ID", wert="aksdlakoeuhn"),
                    ],
                    # just some dummy data to make the GP valid
                    ansprechpartner=[Person(), Person()],
                    anrede=Anrede.EHELEUTE,
                    individuelle_anrede="Künstler",
                    titel=Titel.PROF_DR,
                    vorname="Hans",
                    nachname="Müller-Schmidt",
                    organisationstyp=Organisationstyp.PRIVATPERSON,
                    geschaeftspartnerrollen=[Geschaeftspartnerrolle.KUNDE],
                    adresse=Adresse(
                        strasse="Am Geldspeicher",
                        hausnummer="17",
                        postleitzahl="88101",
                        ort="Entenhausen",
                    ),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, geschaeftspartner: Geschaeftspartner) -> None:
        """
        Test de-/serialisation of Geschaeftspartner.
        """
        assert_serialization_roundtrip(geschaeftspartner)
