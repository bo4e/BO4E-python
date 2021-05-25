from decimal import Decimal

import pytest
from bo4e.bo.zaehler import Zaehler, ZaehlerSchema
from bo4e.com.zaehlwerk import Zaehlwerk
from bo4e.enum.botyp import BoTyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.zaehlerauspraegung import Zaehlerauspraegung
from bo4e.enum.zaehlertyp import Zaehlertyp


class TestZaehler:
    def test_serialisation_only_required_attributes(self):
        """
        Test serialisation of Zaehler only with required attributes
        """
        zaehler = Zaehler(
            zaehlernummer="000111222",
            sparte=Sparte.STROM,
            zaehlerauspraegung=Zaehlerauspraegung.EINRICHTUNGSZAEHLER,
            zaehlwerk=[
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
        )
        assert zaehler.versionstruktur == "2", "versionstruktur was not automatically set"
        assert zaehler.bo_typ is BoTyp.ZAEHLER, "boTyp was not automatically set"
        schema = ZaehlerSchema()
        _ = schema.dumps(zaehler, ensure_ascii=False)  # just to ensure it can be dumped.

    def test_serialization_fails_for_invalid_obis(self):
        """
        Test serialisation of Zaehler fails if OBIS is wrong.
        """
        with pytest.raises(ValueError):
            _ = Zaehler(
                zaehlernummer="000111222",
                sparte=Sparte.STROM,
                zaehlerauspraegung=Zaehlerauspraegung.EINRICHTUNGSZAEHLER,
                zaehlwerk=[
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
