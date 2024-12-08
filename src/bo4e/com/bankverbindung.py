"""
Contains Bankverbindung class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import Optional

from ..utils import postprocess_docstring
from .com import COM


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
    #: International Bank Account Number = IBAN z.B.: DE07 1234 1234 1234 1234 12

    kontoinhaber: Optional[str] = None
    #: Juristische Person welche das Konto hält

    bankkennung: Optional[str] = None
    #: Ein eindeutiger Code, wie z.B. BIC (Bank Identifier Code) oder SWIFT-Code, der eine bestimmte Bank bei
    #: internationalen Transaktionen identifiziert (z.B. BIC: DEUTDEFF für die Deutsche Bank)."

    bankname: Optional[str] = None
    #: Name der bank z.B. Deutsche Bank
