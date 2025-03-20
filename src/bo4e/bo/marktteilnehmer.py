"""
Contains Marktteilnehmer class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..enum.marktrolle import Marktrolle
    from ..enum.rollencodetyp import Rollencodetyp
    from ..enum.sparte import Sparte
    from .geschaeftspartner import Geschaeftspartner


@postprocess_docstring
class Marktteilnehmer(Geschaeftsobjekt):
    """
    Objekt zur Aufnahme der Information zu einem Marktteilnehmer

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Marktteilnehmer.svg" type="image/svg+xml"></object>

    .. HINT::
        `Marktteilnehmer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Marktteilnehmer.json>`_

    """

    typ: Annotated[Literal[Typ.MARKTTEILNEHMER], Field(alias="_typ")] = Typ.MARKTTEILNEHMER
    marktrolle: Optional["Marktrolle"] = None
    """Gibt im Klartext die Bezeichnung der Marktrolle an"""
    rollencodenummer: Optional[str] = None
    """Gibt die Codenummer der Marktrolle an"""
    rollencodetyp: Optional["Rollencodetyp"] = None
    """Gibt den Typ des Codes an"""
    sparte: Optional["Sparte"] = None
    """Sparte des Marktteilnehmers, z.B. Gas oder Strom"""
    makoadresse: Optional[list[str]] = None
    """Die 1:1-Kommunikationsadresse des Marktteilnehmers. Diese wird in der Marktkommunikation verwendet. Konkret kann dies eine eMail-Adresse oder ein AS4-Endpunkt sein."""
    geschaeftspartner: Optional["Geschaeftspartner"] = None
    """Der zu diesem Marktteilnehmer gehörende Geschäftspartner"""
