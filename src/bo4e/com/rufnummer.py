"""
Contains Rufnummer class and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.enum.rufnummernart import Rufnummernart


# pylint: disable=too-few-public-methods


class Rufnummer(COM):
    """
    Contains information to call or fax someone

    .. graphviz:: /api/dots/bo4e/com/Rufnummer.dot

    """

    # required attributes
    #: Ausprägung der Nummer
    nummerntyp: Rufnummernart
    #: Die konkrete Nummer
    rufnummer: str
