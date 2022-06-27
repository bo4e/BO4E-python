"""
Contains Dienstleistung class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp


# pylint: disable=too-few-public-methods


class Dienstleistung(COM):
    """
    Abbildung einer abrechenbaren Dienstleistung.

    .. graphviz:: /api/dots/bo4e/com/Dienstleistung.dot

    """

    # required attributes
    #: Kennzeichnung der Dienstleistung
    dienstleistungstyp: Dienstleistungstyp
    #: Bezeichnung der Dienstleistung
    bezeichnung: str
