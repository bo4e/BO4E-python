"""
Contains Preisgarantie class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..enum.preisgarantietyp import Preisgarantietyp
from ..utils import postprocess_docstring
from .com import COM
from .zeitraum import Zeitraum

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Preisgarantie(COM):
    """
    Definition für eine Preisgarantie mit der Möglichkeit verschiedener Ausprägungen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisgarantie.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preisgarantie.json>`_

    """

    #: Festlegung, auf welche Preisbestandteile die Garantie gewährt wird.
    preisgarantietyp: Optional[Preisgarantietyp] = None
    zeitliche_gueltigkeit: Optional[Zeitraum] = None
    """ Zeitraum, bis zu dem die Preisgarantie gilt, z.B. bis zu einem absolutem / fixem Datum
    oder als Laufzeit in Monaten. """

    # optionale attributes
    #: Freitext zur Beschreibung der Preisgarantie.
    beschreibung: Optional[str] = None
