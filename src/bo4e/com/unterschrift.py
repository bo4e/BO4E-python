"""
Contains Unterschrift class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


class Unterschrift(COM):
    """
    Modellierung einer Unterschrift, z.B. für Verträge, Angebote etc.

    .. graphviz:: /api/dots/bo4e/com/Unterschrift.dot

    """

    # required attributes
    #: Name des Unterschreibers
    name: str

    # optional attributes
    ort: str = None  #: Ort, an dem die Unterschrift geleistet wird
    datum: datetime = None  #: Datum der Unterschrift
