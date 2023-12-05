"""
Contains Marktteilnehmer class
and corresponding marshmallow schema for de-/serialization
"""


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from pydantic import Field

from ..enum.marktrolle import Marktrolle
from ..enum.rollencodetyp import Rollencodetyp
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftspartner import Geschaeftspartner


@postprocess_docstring
class Marktteilnehmer(Geschaeftspartner):
    """
    Objekt zur Aufnahme der Information zu einem Marktteilnehmer

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Marktteilnehmer.svg" type="image/svg+xml"></object>

    .. HINT::
        `Marktteilnehmer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Marktteilnehmer.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.MARKTTEILNEHMER
    #: Gibt im Klartext die Bezeichnung der Marktrolle an
    marktrolle: Optional[Marktrolle] = None
    #: Gibt die Codenummer der Marktrolle an
    rollencodenummer: Optional[str] = None
    #: Gibt den Typ des Codes an
    rollencodetyp: Optional[Rollencodetyp] = None
    #: Sparte des Marktteilnehmers, z.B. Gas oder Strom
    sparte: Optional[Sparte] = None

    #: Die 1:1-Kommunikationsadresse des Marktteilnehmers; Diese wird in der Marktkommunikation verwendet.
    makoadresse: Optional[str] = None
