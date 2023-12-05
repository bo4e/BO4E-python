"""
Contains Zustaendigkeit class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..enum.themengebiet import Themengebiet
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Zustaendigkeit(COM):
    """
    Enthält die zeitliche Zuordnung eines Ansprechpartners zu Abteilungen und Zuständigkeiten.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zustaendigkeit.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zustaendigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zustaendigkeit.json>`_

    """

    themengebiet: Optional[Themengebiet] = None
    """
    Hier kann eine thematische Zuordnung des Ansprechpartners angegeben werden
    """

    jobtitel: Optional[str] = None  #: Berufliche Rolle des Ansprechpartners
    abteilung: Optional[str] = None  #: Abteilung, in der der Ansprechpartner tätig ist
