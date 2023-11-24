"""
Contains Region class and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..com.regionskriterium import Regionskriterium
from ..enum.typ import Typ
from .geschaeftsobjekt import Geschaeftsobjekt

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


class Region(Geschaeftsobjekt):
    """
    Modellierung einer Region als Menge von Kriterien, die eine Region beschreiben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Region.svg" type="image/svg+xml"></object>

    .. HINT::
        `Region JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Region.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.REGION
    #: Bezeichnung der Region
    bezeichnung: Optional[str] = None

    #: Positivliste der Kriterien zur Definition der Region
    positiv_liste: Optional[list[Regionskriterium]] = None

    #: Negativliste der Kriterien zur Definition der Region
    negativ_liste: Optional[list[Regionskriterium]] = None
