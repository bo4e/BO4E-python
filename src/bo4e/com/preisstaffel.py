"""
Contains Preisstaffel
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:

    from .sigmoidparameter import Sigmoidparameter

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Preisstaffel(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisstaffel.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preisstaffel.json>`_

    """

    typ: Annotated[Literal[ComTyp.PREISSTAFFEL], Field(alias="_typ")] = ComTyp.PREISSTAFFEL

    bezeichnung: Optional[str] = None
    """Eine (beliebige) Bezeichnung für die Preisstaffel."""
    preis: Optional[Decimal] = None
    """Preis pro abgerechneter Mengeneinheit. Die Mengeneinheit wird durch das übergeordnete Objekt angegeben."""
    staffelgrenze_von: Optional[Decimal] = None
    """
    Inklusiver unterer Wert, ab dem die Staffel gilt (inklusiv).
    Grenzen werden bspw. wie folgt angegeben: `0 - 1000, 1001 - 2000, etc.`
    Werte zwischen den Grenzen (z.B. `1000,6`) rutschen in die obere Zone / Staffel.
    """
    staffelgrenze_bis: Optional[Decimal] = None
    """
    Exklusiver oberer Wert, bis zu dem die Staffel gilt (inklusiv).
    Grenzen werden bspw. wie folgt angegeben: `0 - 1000, 1001 - 2000, etc.`
    Werte zwischen den Grenzen (z.B. `1000,6`) rutschen in die obere Zone / Staffel.
    """
    sigmoidparameter: Optional["Sigmoidparameter"] = None
    """Parameter zur Berechnung des Preises anhand der Jahresmenge und weiterer netzbezogener Parameter"""
    artikel_id: Optional[str] = None
    """
    Standardisierte vom BDEW herausgegebene Liste, welche im Strommarkt die BDEW-Artikelnummer ablöst.
    TODO: Kann das Feld weg?
    """
