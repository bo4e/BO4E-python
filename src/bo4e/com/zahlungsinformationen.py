"""
Contains Zahlungsinforamtionen class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Zahlungsinformationen(COM):
    """
    Die Komponente wird dazu verwendet, Zahlungsinformationen zu einem BO Rechnung zu hinterlegen

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zahlungsinformationen.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zahlungsinformationen JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zahlungsinformationen.json>`_

    """

    kontoinhaber: Optional[str] = None
    """Zahlungsempfänger bzw. Kontoinhaber"""
    iban: Optional[str] = None
    """IBAN an die überwiesen werden soll"""
    bic: Optional[str] = None
    """BIC der Bank"""
    referenz: Optional[str] = None
    """Referenz für die Überweisung"""
    ist_sepa_einzug: Optional[bool] = None
    """Wird die Zahlung eingezogen?"""
    sepa_referenz: Optional[str] = None
    """Referenz des SEPA Einzugs"""
