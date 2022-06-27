"""
Contains Zustaendigkeit class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.enum.themengebiet import Themengebiet


# pylint: disable=too-few-public-methods


class Zustaendigkeit(COM):
    """
    Enthält die zeitliche Zuordnung eines Ansprechpartners zu Abteilungen und Zuständigkeiten.

    .. graphviz:: /api/dots/bo4e/com/Zustaendigkeit.dot

    """

    # required attributes
    themengebiet: Themengebiet
    """
    Hier kann eine thematische Zuordnung des Ansprechpartners angegeben werden
    """

    # optional attributes
    jobtitel: str = None  #: Berufliche Rolle des Ansprechpartners
    abteilung: str = None  #: Abteilung, in der der Ansprechpartner tätig ist
