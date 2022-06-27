"""
Contains Vertragsteil class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

from bo4e.com.com import COM
from bo4e.com.menge import Menge


# pylint: disable=too-few-public-methods


class Vertragsteil(COM):
    """
    Abbildung für einen Vertragsteil. Der Vertragsteil wird dazu verwendet,
    eine vertragliche Leistung in Bezug zu einer Lokation (Markt- oder Messlokation) festzulegen.

    .. graphviz:: /api/dots/bo4e/com/Vertragsteil.dot

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
    lokation: str = None
    """
    Der Identifier für diejenigen Markt- oder Messlokation, die zu diesem Vertragsteil gehören.
    Verträge für mehrere Lokationen werden mit mehreren Vertragsteilen abgebildet
    """
    vertraglich_fixierte_menge: Menge = None
    """
    Für die Lokation festgeschriebene Abnahmemenge
    """
    minimale_abnahmemenge: Menge = None
    """
    Für die Lokation festgelegte Mindestabnahmemenge (inklusiv)
    """
    maximale_abnahmemenge: Menge = None
    """
    Für die Lokation festgelegte maximale Abnahmemenge (exklusiv)
    """
