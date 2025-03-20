"""
Contains Preisgarantie class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.preisgarantietyp import Preisgarantietyp
    from .zeitraum import Zeitraum

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Preisgarantie(COM):
    """
    Definition für eine Preisgarantie mit der Möglichkeit verschiedener Ausprägungen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisgarantie.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preisgarantie.json>`_

    """

    preisgarantietyp: Optional["Preisgarantietyp"] = None
    """Festlegung, auf welche Preisbestandteile die Garantie gewährt wird."""
    zeitliche_gueltigkeit: Optional["Zeitraum"] = None
    """ Zeitraum, bis zu dem die Preisgarantie gilt, z.B. bis zu einem absolutem / fixem Datum
    oder als Laufzeit in Monaten. """

    # optionale attributes
    beschreibung: Optional[str] = None
    """Freitext zur Beschreibung der Preisgarantie."""
