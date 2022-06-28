"""
Contains Zustaendigkeit class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from bo4e.com.com import COM
from bo4e.enum.themengebiet import Themengebiet


# pylint: disable=too-few-public-methods


class Zustaendigkeit(COM):
    """
    Enthält die zeitliche Zuordnung eines Ansprechpartners zu Abteilungen und Zuständigkeiten.

    .. graphviz:: /api/dots/bo4e/com/Zustaendigkeit.dot

    .. HINT::
        `Zustaendigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Zustaendigkeit.json>`_

    """

    # required attributes
    themengebiet: Themengebiet
    """
    Hier kann eine thematische Zuordnung des Ansprechpartners angegeben werden
    """

    # optional attributes
    jobtitel: Optional[str] = None  #: Berufliche Rolle des Ansprechpartners
    abteilung: Optional[str] = None  #: Abteilung, in der der Ansprechpartner tätig ist
