from datetime import datetime
from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import (
    Energierichtung,
    ExterneReferenz,
    Mengeneinheit,
    Registeranzahl,
    Sparte,
    Typ,
    Zaehler,
    Zaehlerauspraegung,
    Zaehlertyp,
    Zaehlwerk,
)

example_zaehler = Zaehler(
    zaehlernummer="000111222",
    sparte=Sparte.STROM,
    zaehlerauspraegung=Zaehlerauspraegung.EINRICHTUNGSZAEHLER,
    zaehlwerke=[
        Zaehlwerk(
            zaehlwerk_id="98765",
            einheit=Mengeneinheit.KW,
            richtung=Energierichtung.EINSP,
            bezeichnung="my zaehlwerk",
            obis_kennzahl="1-0:1.8.1",
            wandlerfaktor=Decimal(0.95),
        )
    ],
    zaehlertyp=Zaehlertyp.DREHSTROMZAEHLER,
    registeranzahl=Registeranzahl.ZWEITARIF,
    zaehlerkonstante=Decimal(0.9),
    eichung_bis=datetime(2022, 1, 1, 0, 0, 0),
    externe_referenzen=[ExterneReferenz(ex_ref_name="zaehler im anderen system", ex_ref_wert="7890")],
    letzte_eichung=datetime(2019, 6, 30, 0, 0, 0),
)


class TestZaehler:
    def test_de_serialisation(self) -> None:
        """
        Test de-/serialisation of Zaehler only with required attributes
        """
        zaehler = Zaehler(
            zaehlernummer="000111222",
            sparte=Sparte.STROM,
            zaehlerauspraegung=Zaehlerauspraegung.EINRICHTUNGSZAEHLER,
            zaehlwerke=[
                Zaehlwerk(
                    zaehlwerk_id="98765",
                    einheit=Mengeneinheit.KW,
                    richtung=Energierichtung.EINSP,
                    bezeichnung="my zaehlwerk",
                    obis_kennzahl="1-0:1.8.1",
                    wandlerfaktor=Decimal(0.95),
                )
            ],
            zaehlertyp=Zaehlertyp.DREHSTROMZAEHLER,
            registeranzahl=Registeranzahl.ZWEITARIF,
            zaehlerkonstante=Decimal(0.9),
            eichung_bis=datetime(2022, 1, 1, 0, 0, 0),
            externe_referenzen=[ExterneReferenz(ex_ref_name="zaehler im anderen system", ex_ref_wert="7890")],
            letzte_eichung=datetime(2019, 6, 30, 0, 0, 0),
        )
        assert zaehler.version is not None, "versionstruktur was not automatically set"
        assert zaehler.typ is Typ.ZAEHLER, "_typ was not automatically set"
        assert zaehler.zaehlwerke is not None
        assert zaehler.zaehlwerke[0].richtung == Energierichtung.EINSP
        assert zaehler.zaehlwerke[0].einheit == Mengeneinheit.KW
        json_string = zaehler.model_dump_json(by_alias=True)
        assert "richtung" in json_string, "Zaehlwerk->richtung was not serialized"
        assert "einheit" in json_string, "Zaehlwerk->einheit was not serialized"
        deserialized_zaehler = Zaehler.model_validate_json(json_string)
        assert deserialized_zaehler == zaehler
