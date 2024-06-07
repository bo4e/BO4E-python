"""
Contains Preisgarantie class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.preisgarantietyp import Preisgarantietyp
    from .zeitspanne import Zeitspanne

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

    #: Festlegung, auf welche Preisbestandteile die Garantie gewährt wird.
    preisgarantietyp: Optional["Preisgarantietyp"] = None
    zeitliche_gueltigkeit: Optional["Zeitspanne"] = None
    """ Zeitspanne, in der die Preisgarantie gilt, z.B. bis zu einem absoluten / fixen Datum
    oder als Laufzeit mit Startdatum und Enddatum. """

    # optionale attributes
    #: Freitext zur Beschreibung der Preisgarantie.
    beschreibung: Optional[str] = None
