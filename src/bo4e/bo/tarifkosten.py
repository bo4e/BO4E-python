"""
Contains Tarifkosten class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..enum.typ import Typ
from .kosten import Kosten
from .tarifinfo import Tarifinfo

# pylint: disable=too-few-public-methods


class Tarifkosten(Tarifinfo):
    """
    Objekt zur Kommunikation von Kosten, die im Rahmen der Tarifanwendung entstehen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarifkosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Tarifkosten.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.TARIFKOSTEN
    kosten: Optional[Kosten] = None
    """
    Referenz (Link) zu einem Kostenobjekt, in dem die Kosten für die Anwendung
    des Tarifs auf eine Abnahmesituation berechnet wurden
    """

    # there are no optional attributes
