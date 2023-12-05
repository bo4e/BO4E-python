"""
Contains Angebotsposition class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..utils import postprocess_docstring
from .betrag import Betrag
from .com import COM
from .menge import Menge
from .preis import Preis

# pylint: disable=too-few-public-methods


@postprocess_docstring
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
        `Angebotsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Angebotsposition.json>`_

    """

    #: Bezeichnung der jeweiligen Position des Angebotsteils
    positionsbezeichnung: Optional[str] = None
    #: Preis pro Einheit/Stückpreis des angebotenen Artikels.
    positionspreis: Optional[Preis] = None

    #: Menge des angebotenen Artikels (z.B. Wirkarbeit in kWh), in dieser Angebotsposition
    positionsmenge: Optional[Menge] = None
    #: Kosten (positionspreis * positionsmenge) für diese Angebotsposition
    positionskosten: Optional[Betrag] = None

    # for a preis = menge*times validation we first need to resolve
    # https://github.com/Hochfrequenz/BO4E-python/issues/126
