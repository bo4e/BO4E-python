"""
Contains Bankverbindung class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.preismodell import Preismodell
    from ..enum.rechnungslegung import Rechnungslegung
    from ..enum.sparte import Sparte
    from ..enum.vertragsform import Vertragsform
    from .ausschreibungsdetail import Ausschreibungsdetail
    from .menge import Menge
    from .zeitraum import Zeitraum


@postprocess_docstring
class Bankverbindung(COM):
    """
    Eine Komponente zur Abbildung einer einzelner Bankverbindung

    .. raw:: html

        <object data="../_static/images/bo4e/com/Bankverbindung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Bankverbindung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Bankverbindung.json>`_

    """

    iban: Optional[str] = None

    kontoinhaber: Optional[str] = None

    bankkennung: Optional[str] = None

    bankname: Optional[str] = None
