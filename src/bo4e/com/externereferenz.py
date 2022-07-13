"""
Contains ExterenzeReferenz class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods
#
class ExterneReferenz(COM):
    """
    Viele Datenobjekte weisen in unterschiedlichen Systemen eine eindeutige ID (Kundennummer, GP-Nummer etc.) auf.
    Beim Austausch von Datenobjekten zwischen verschiedenen Systemen ist es daher hilfreich,
    sich die eindeutigen IDs der anzubindenden Systeme zu merken.

    .. raw:: html

        <object data="../_static/images/bo4e/com/ExterneReferenz.svg" type="image/svg+xml"></object>

    .. HINT::
        `ExterneReferenz JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ExterneReferenz.json>`_

    """

    # required attributes
    ex_ref_name: str  #: Bezeichnung der externen Referenz (z.B. "microservice xyz" oder "SAP CRM GP-Nummer")
    ex_ref_wert: str  #: Wert der externen Referenz (z.B. "123456"; "4711")
