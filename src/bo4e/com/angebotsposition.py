"""
Contains Angebotsposition class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.menge import Menge
from bo4e.com.preis import Preis

# pylint: disable=too-few-public-methods


class Angebotsposition(COM):
    """
    Unterhalb von Angebotsteilen sind die Angebotspositionen eingebunden.
    Hier werden die angebotenen Bestandteile einzeln aufgeführt. Beispiel:
    Positionsmenge: 4000 kWh
    Positionspreis: 24,56 ct/kWh
    Positionskosten: 982,40 EUR

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Angebotsposition.json>`_

    """

    # required attributes
    #: Bezeichnung der jeweiligen Position des Angebotsteils
    positionsbezeichnung: str
    #: Preis pro Einheit/Stückpreis des angebotenen Artikels.
    positionspreis: Preis

    # optional attributes
    #: Menge des angebotenen Artikels (z.B. Wirkarbeit in kWh), in dieser Angebotsposition
    positionsmenge: Optional[Menge] = None
    #: Kosten (positionspreis * positionsmenge) für diese Angebotsposition
    positionskosten: Optional[Betrag] = None

    # for a preis = menge*times validation we first need to resolve
    # https://github.com/Hochfrequenz/BO4E-python/issues/126
