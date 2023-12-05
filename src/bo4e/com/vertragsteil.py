"""
Contains Vertragsteil class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

from ..utils import postprocess_docstring
from .com import COM
from .menge import Menge

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Vertragsteil(COM):
    """
    Abbildung für einen Vertragsteil. Der Vertragsteil wird dazu verwendet,
    eine vertragliche Leistung in Bezug zu einer Lokation (Markt- oder Messlokation) festzulegen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragsteil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Vertragsteil.json>`_

    """

    vertragsteilbeginn: Optional[datetime] = None
    """
    Start der Gültigkeit des Vertragsteils (inklusiv)
    """
    vertragsteilende: Optional[datetime] = None
    """
    Ende der Gültigkeit des Vertragsteils (exklusiv)
    """

    lokation: Optional[str] = None
    """
    Der Identifier für diejenigen Markt- oder Messlokation, die zu diesem Vertragsteil gehören.
    Verträge für mehrere Lokationen werden mit mehreren Vertragsteilen abgebildet
    """
    vertraglich_fixierte_menge: Optional[Menge] = None
    """
    Für die Lokation festgeschriebene Abnahmemenge
    """
    minimale_abnahmemenge: Optional[Menge] = None
    """
    Für die Lokation festgelegte Mindestabnahmemenge (inklusiv)
    """
    maximale_abnahmemenge: Optional[Menge] = None
    """
    Für die Lokation festgelegte maximale Abnahmemenge (exklusiv)
    """
