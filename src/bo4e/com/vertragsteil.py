"""
Contains Vertragsteil class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

from bo4e.com.com import COM
from bo4e.com.menge import Menge

# pylint: disable=too-few-public-methods


class Vertragsteil(COM):
    """
    Abbildung für einen Vertragsteil. Der Vertragsteil wird dazu verwendet,
    eine vertragliche Leistung in Bezug zu einer Lokation (Markt- oder Messlokation) festzulegen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragsteil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Vertragsteil.json>`_

    """

    # required attributes
    vertragsteilbeginn: datetime
    """
    Start der Gültigkeit des Vertragsteils (inklusiv)
    """
    vertragsteilende: datetime
    """
    Ende der Gültigkeit des Vertragsteils (exklusiv)
    """

    # optional attributes
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
