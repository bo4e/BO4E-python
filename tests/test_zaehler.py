from datetime import datetime
from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e.bo.zaehler import Zaehler
from bo4e.com.externereferenz import ExterneReferenz
from bo4e.com.zaehlwerk import Zaehlwerk
from bo4e.enum.botyp import BoTyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.zaehlerauspraegung import Zaehlerauspraegung
from bo4e.enum.zaehlertyp import Zaehlertyp


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
            tarifart=Tarifart.ZWEITARIF,
            zaehlerkonstante=Decimal(0.9),
            eichung_bis=datetime(2022, 1, 1, 0, 0, 0),
            externe_referenzen=[ExterneReferenz(ex_ref_name="zaehler im anderen system", ex_ref_wert="7890")],
            letzte_eichung=datetime(2019, 6, 30, 0, 0, 0),
        )
        assert zaehler.versionstruktur == "2", "versionstruktur was not automatically set"
        assert zaehler.bo_typ is BoTyp.ZAEHLER, "boTyp was not automatically set"
        assert zaehler.zaehlwerke[0].richtung == Energierichtung.EINSP
        assert zaehler.zaehlwerke[0].einheit == Mengeneinheit.KW
        json_string = zaehler.json(by_alias=True, ensure_ascii=False)
        assert "richtung" in json_string, "Zaehlwerk->richtung was not serialized"
        assert "einheit" in json_string, "Zaehlwerk->einheit was not serialized"
        deserialized_zaehler = Zaehler.parse_raw(json_string)
        assert deserialized_zaehler == zaehler

    def test_serialization_fails_for_invalid_obis(self) -> None:
        """
        Test serialisation of Zaehler fails if OBIS is wrong.
        """
        with pytest.raises(ValidationError) as excinfo:
            _ = Zaehler(
                zaehlernummer="000111222",
                sparte=Sparte.STROM,
                zaehlerauspraegung=Zaehlerauspraegung.EINRICHTUNGSZAEHLER,
                zaehlwerke=[
                    Zaehlwerk(
                        zaehlwerk_id="98765",
                        einheit=Mengeneinheit.KW,
                        richtung=Energierichtung.EINSP,
                        bezeichnung="my zaehlwerk",
                        obis_kennzahl="foo",  # <-- this is not a valid obis. it triggered the value error
                        wandlerfaktor=Decimal(0.95),
                    )
                ],
                zaehlertyp=Zaehlertyp.DREHSTROMZAEHLER,
                tarifart=Tarifart.ZWEITARIF,
            )
        assert "1 validation error" in str(excinfo.value)
        assert "obisKennzahl" in str(excinfo.value)
        assert "string does not match regex" in str(excinfo.value)

    def test_serialization_fails_for_empty_zaehlwerke(self) -> None:
        """
        Test serialisation of Zaehler fails if there are no zaehlwerke.
        """
        with pytest.raises(ValidationError) as excinfo:
            _ = Zaehler(
                zaehlernummer="000111222",
                sparte=Sparte.STROM,
                zaehlerauspraegung=Zaehlerauspraegung.EINRICHTUNGSZAEHLER,
                zaehlwerke=[],
                zaehlertyp=Zaehlertyp.DREHSTROMZAEHLER,
                tarifart=Tarifart.ZWEITARIF,
            )
        assert "1 validation error" in str(excinfo.value)
        assert "ensure this value has at least 1 item" in str(excinfo.value)
