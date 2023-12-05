"""
Contains Energiemenge class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..com.verbrauch import Verbrauch
from ..enum.lokationstyp import Lokationstyp
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Energiemenge(Geschaeftsobjekt):
    """
    Abbildung von Mengen, die Lokationen zugeordnet sind

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Energiemenge.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energiemenge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Energiemenge.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.ENERGIEMENGE
    #: Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört
    lokations_id: Optional[str] = None
    # todo: add validator such that only mess- or marktlokations IDs are accepted + cross check with lokationstyp
    #: Gibt an, ob es sich um eine Markt- oder Messlokation handelt
    lokationstyp: Optional[Lokationstyp] = None

    #: Gibt den Verbrauch in einer Zeiteinheit an
    energieverbrauch: Optional[list[Verbrauch]] = None
    # there are no optional attributes
