"""
Contains Zustaendigkeit class
and corresponding marshmallow schema for de-/serialization
"""


from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM
from bo4e.enum.themengebiet import Themengebiet


# pylint: disable=too-few-public-methods


class Zustaendigkeit(COM):
    """
    Enthält die zeitliche Zuordnung eines Ansprechpartners zu Abteilungen und Zuständigkeiten.

    .. HINT::
        `Zustaendigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ZustaendigkeitSchema.json>`_

    """

    # required attributes
    themengebiet: Themengebiet
    """
    Hier kann eine thematische Zuordnung des Ansprechpartners angegeben werden
    """

    # optional attributes
    jobtitel: str = None  #: Berufliche Rolle des Ansprechpartners
    abteilung: str = None  #: Abteilung, in der der Ansprechpartner tätig ist
