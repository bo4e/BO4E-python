"""
Contains Marktgebietinfo class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


class MarktgebietInfo(COM):
    """
    Informationen zum Marktgebiet im Gas.

    .. graphviz:: /api/dots/bo4e/com/MarktgebietInfo.dot

    """

    # required attributes
    marktgebiet: str  #: Der Name des Marktgebietes
    marktgebietcode: str  #: Die standardisierte Codenummer des Marktgebietes
