"""
Contains Fremdkostenposition and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional


from marshmallow import fields

from bo4e.com.kostenposition import Kostenposition


# pylint: disable=too-few-public-methods, too-many-instance-attributes


class Fremdkostenposition(Kostenposition):
    """
    Eine Kostenposition im Bereich der Fremdkosten

    .. HINT::
        `Fremdkostenposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/FremdkostenpositionSchema.json>`_

    """

    # optional attributes (additional to those from Kostenposition)
    #: Der Name des Marktpartners, der die Preise festlegt, bzw. die Kosten in Rechnung stellt
    marktpartnername: str = None

    #: Die Codenummer (z.B. BDEW-Codenummer) des Marktpartners, der die Preise festlegt / die Kosten in Rechnung stellt
    marktpartnercode: str = None

    #: EIC-Code des Regel- oder Marktgebietes eingetragen. Z.B. '10YDE-EON------1' für die Regelzone TenneT
    gebietcode_eic: str = None
    # todo: see issue https://github.com/Hochfrequenz/BO4E-python/issues/147 for EIC validation

    #: Link zum veröffentlichten Preisblatt
    link_preisblatt: str = None
