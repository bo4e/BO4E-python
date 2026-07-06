from datetime import datetime, timezone
from decimal import Decimal

import pytest

from bo4e import (
    EinheitsPreisposition,
    Energiemix,
    Kundentyp,
    Marktteilnehmer,
    Mengeneinheit,
    Operator,
    Preis,
    Preisgarantie,
    Preisreferenz,
    Region,
    Regionskriterium,
    Regionsoperation,
    Regionspreis,
    Regionszeitscheibe,
    Registeranzahl,
    RelativePreisposition,
    Sparte,
    Tarif,
    Tarifberechnungsparameter,
    Tarifeinschraenkung,
    Tarifmerkmal,
    Tarifpreiszeitscheibe,
    Tariftyp,
    Vertragskonditionen,
    Waehrungseinheit,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarif:
    @pytest.mark.parametrize(
        "tarif",
        [
            pytest.param(
                Tarif(
                    berechnungsparameter=Tarifberechnungsparameter(),
                    preisgarantie=Preisgarantie(),
                    tarifeinschraenkung=Tarifeinschraenkung(),
                    # below are the attributes of tarifinfo
                    bezeichnung="foo",
                    anbietername="der beste stromanbieter",
                    sparte=Sparte.STROM,
                    kundentypen=[Kundentyp.PRIVAT, Kundentyp.GEWERBE],
                    registeranzahl=Registeranzahl.MEHRTARIF,
                    tariftyp=Tariftyp.GRUND_ERSATZVERSORGUNG,
                    tarifmerkmale=[Tarifmerkmal.HEIZSTROM],
                    website="https://foo.inv",
                    bemerkung="super billig aber auch super dreckig",
                    vertragskonditionen=Vertragskonditionen(),
                    zeitliche_gueltigkeit=Zeitraum(),
                    energiemix=[Energiemix()],
                    anbieter=Marktteilnehmer(),
                    regionspreise=[
                        Regionspreis(
                            regionszeitscheiben=[
                                Regionszeitscheibe(
                                    zeitscheibengueltigkeit=Zeitraum(startdatum=datetime(2020, 1, 1)),
                                    region=Region(
                                        bezeichnung="Deutschland",
                                        regionsoperationen=[
                                            Regionsoperation(
                                                regionsoperator=Operator.ADDITION,
                                                prioritaet=0,
                                                bezeichnung="Deutschland",
                                                regionskriterium=Regionskriterium.BUNDESWEIT,
                                            )
                                        ],
                                    ),
                                ),
                            ],
                            tarifpreiszeitscheiben=[
                                Tarifpreiszeitscheibe(
                                    zeitscheibengueltigkeit=Zeitraum(startdatum=datetime(2020, 1, 1)),
                                    einheits_preispositionen=[
                                        EinheitsPreisposition(
                                            id="12345",
                                            bezeichnung="Arbeitspreis",
                                            preisreferenz=Preisreferenz.ENERGIEMENGE,
                                            preis=Preis(
                                                wert=Decimal("30"),
                                                einheit=Waehrungseinheit.CT,
                                                bezugswert=Mengeneinheit.KWH,
                                            ),
                                        )
                                    ],
                                    relative_preispositionen=[
                                        RelativePreisposition(
                                            bezeichnung="5% Rabatt auf Arbeitspreis",
                                            id_referenz="12345",
                                            wert=Decimal("0.95"),
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                ),
                id="all attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarif: Tarif) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarif)
