from decimal import Decimal
from typing import Any, Dict

import pytest

from bo4e.bo.geraet import Geraet
from bo4e.com.menge import Menge
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.enum.geraetetyp import Geraetetyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.typ import Typ
from bo4e.enum.voraussetzungen import Voraussetzungen
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_geraet import example_geraet

example_tarifeinschraenkung = Tarifeinschraenkung(
    zusatzprodukte=["foo", "bar"],
    voraussetzungen=[Voraussetzungen.ALTVERTRAG, Voraussetzungen.DIREKTVERTRIEB],
    einschraenkungzaehler=[
        example_geraet,
        Geraet(geraetenummer="197foo"),
    ],
    einschraenkungleistung=[
        Menge(wert=Decimal(12.5), einheit=Mengeneinheit.MWH),
        Menge(wert=Decimal(30), einheit=Mengeneinheit.KWH),
    ],
)


class TestTarifeinschraenkung:
    @pytest.mark.parametrize(
        "tarifeinschraenkung, expected_json_dict",
        [
            pytest.param(
                Tarifeinschraenkung(),
                {
                    "zusatzprodukte": None,
                    "voraussetzungen": None,
                    "einschraenkungzaehler": None,
                    "einschraenkungleistung": None,
                    "_id": None,
                },
                id="minimal attributes",
            ),
            pytest.param(
                Tarifeinschraenkung(
                    zusatzprodukte=["foo", "bar"],
                    voraussetzungen=[Voraussetzungen.ALTVERTRAG, Voraussetzungen.DIREKTVERTRIEB],
                    einschraenkungzaehler=[
                        example_geraet,
                        Geraet(geraetenummer="197foo"),
                    ],
                    einschraenkungleistung=[
                        Menge(wert=Decimal(12.5), einheit=Mengeneinheit.MWH),
                        Menge(wert=Decimal(30), einheit=Mengeneinheit.KWH),
                    ],
                ),
                {
                    "zusatzprodukte": ["foo", "bar"],
                    "voraussetzungen": ["ALTVERTRAG", "DIREKTVERTRIEB"],
                    "einschraenkungzaehler": [
                        {
                            "versionstruktur": "2",
                            "_typ": Typ.GERAET,
                            "externeReferenzen": None,
                            "geraetenummer": "0815",
                            "geraeteklasse": "WANDLER",
                            "geraetetyp": "BLOCKSTROMWANDLER",
                            "bezeichnung": "56k Modem",
                            "_id": None,
                        },
                        {
                            "versionstruktur": "2",
                            "_typ": Typ.GERAET,
                            "externeReferenzen": None,
                            "geraetenummer": "197foo",
                            "bezeichnung": None,
                            "geraeteklasse": None,
                            "geraetetyp": None,
                            "_id": None,
                        },
                    ],
                    "einschraenkungleistung": [
                        {"wert": Decimal("12.5"), "einheit": Mengeneinheit.MWH, "_id": None},
                        {"wert": Decimal("30"), "einheit": Mengeneinheit.KWH, "_id": None},
                    ],
                    "_id": None,
                },
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, tarifeinschraenkung: Tarifeinschraenkung, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Tarifeinschraenkung
        """
        assert_serialization_roundtrip(tarifeinschraenkung, expected_json_dict)
