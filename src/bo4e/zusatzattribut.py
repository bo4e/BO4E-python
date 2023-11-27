"""
Contains ExterenzeReferenz class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Any, Optional

from pydantic import BaseModel


# pylint: disable=too-few-public-methods
#
class ZusatzAttribut(BaseModel):
    """
    Viele Datenobjekte weisen in unterschiedlichen Systemen eine eindeutige ID (Kundennummer, GP-Nummer etc.) auf.
    Beim Austausch von Datenobjekten zwischen verschiedenen Systemen ist es daher hilfreich,
    sich die eindeutigen IDs der anzubindenden Systeme zu merken.

    .. raw:: html

        <object data="../_static/images/bo4e/com/ZusatzAttribut.svg" type="image/svg+xml"></object>

    .. HINT::
        `ZusatzAttribute JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ZusatzAttribute.json>`_

    """

    name: Optional[str]  #: Bezeichnung der externen Referenz (z.B. "microservice xyz" oder "SAP CRM GP-Nummer")
    wert: Any  #: Wert der externen Referenz (z.B. "123456"; "4711")
