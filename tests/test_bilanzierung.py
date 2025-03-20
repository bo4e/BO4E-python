from datetime import datetime, timezone

import pytest
from _decimal import Decimal

from bo4e.bo.bilanzierung import Bilanzierung
from bo4e.com.lastprofil import Lastprofil
from bo4e.com.menge import Menge
from bo4e.com.tagesparameter import Tagesparameter
from bo4e.enum.aggregationsverantwortung import Aggregationsverantwortung
from bo4e.enum.fallgruppenzuordnung import Fallgruppenzuordnung
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.profilart import Profilart
from bo4e.enum.profiltyp import Profiltyp
from bo4e.enum.profilverfahren import Profilverfahren
from bo4e.enum.prognosegrundlage import Prognosegrundlage
from bo4e.enum.wahlrechtprognosegrundlage import WahlrechtPrognosegrundlage
from bo4e.enum.zeitreihentyp import Zeitreihentyp
from tests.serialization_helper import assert_serialization_roundtrip


class TestBilanzierung:
    @pytest.mark.parametrize(
        "bilanzierung",
        [
            pytest.param(
                Bilanzierung(
                    marktlokations_id="51238696781",
                    lastprofil=[
                        Lastprofil(
                            bezeichnung="foo",
                            profilschar="foo2",
                            verfahren=Profilverfahren.SYNTHETISCH,
                            ist_einspeisung=True,
                            tagesparameter=Tagesparameter(
                                klimazone="7624q",
                                temperaturmessstelle="1234x",
                                dienstanbieter="ZT1",
                                herausgeber="BDEW",
                            ),
                            profilart=Profilart.ART_LASTPROFIL,
                            herausgeber="BDEW",
                        )
                    ],
                    bilanzierungsbeginn=datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    bilanzierungsende=datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    bilanzkreis="foo",
                    jahresverbrauchsprognose=Menge(wert=Decimal(3.41), einheit=Mengeneinheit.MWH),
                    temperatur_arbeit=Menge(wert=Decimal(3.41), einheit=Mengeneinheit.MWH),
                    # todo: check einheiten
                    kundenwert=Menge(wert=Decimal(3.41), einheit=Mengeneinheit.MWH),
                    verbrauchsaufteilung=Decimal(1.5),
                    zeitreihentyp=Zeitreihentyp.EGS,
                    aggregationsverantwortung=Aggregationsverantwortung.VNB,
                    prognosegrundlage=Prognosegrundlage.WERTE,
                    details_prognosegrundlage=[Profiltyp.SLP_SEP],
                    wahlrecht_prognosegrundlage=WahlrechtPrognosegrundlage.DURCH_LF,
                    fallgruppenzuordnung=Fallgruppenzuordnung.GABI_RLM_MIT_TAGESBAND,
                    prioritaet=1,
                    grund_wahlrecht_prognosegrundlage=WahlrechtPrognosegrundlage.DURCH_LF_NICHT_GEGEBEN,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, bilanzierung: Bilanzierung) -> None:
        assert_serialization_roundtrip(bilanzierung)
