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
    # International Bank Account Number = IBAN for example: DE07 1234 1234 1234 1234 12

    kontoinhaber: Optional[str] = None
    # individual or entity in whose name a bank account is registered and who has legal rights over it

    bankkennung: Optional[str] = None
    # A unique code, such as a BIC (Bank Identifier Code) or SWIFT code, that identifies a specific bank in
    # international transactions (e.g., BIC: DEUTDEFF for Deutsche Bank)

    bankname: Optional[str] = None
    # name of the bank e.g. Deutsche Bank
