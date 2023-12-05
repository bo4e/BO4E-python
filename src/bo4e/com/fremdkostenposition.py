"""
Contains Fremdkostenposition and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..utils import postprocess_docstring
from .kostenposition import Kostenposition

# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class Fremdkostenposition(Kostenposition):
    """
    Eine Kostenposition im Bereich der Fremdkosten

    .. raw:: html

        <object data="../_static/images/bo4e/com/Fremdkostenposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Fremdkostenposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Fremdkostenposition.json>`_

    """

    # optional attributes (additional to those from Kostenposition)
    #: Der Name des Marktpartners, der die Preise festlegt, bzw. die Kosten in Rechnung stellt
    marktpartnername: Optional[str] = None

    #: Die Codenummer (z.B. BDEW-Codenummer) des Marktpartners, der die Preise festlegt / die Kosten in Rechnung stellt
    marktpartnercode: Optional[str] = None

    #: EIC-Code des Regel- oder Marktgebietes eingetragen. Z.B. '10YDE-EON------1' für die Regelzone TenneT
    gebietcode_eic: Optional[str] = None
    # todo: see issue https://github.com/Hochfrequenz/BO4E-python/issues/147 for EIC validation

    #: Link zum veröffentlichten Preisblatt
    link_preisblatt: Optional[str] = None
