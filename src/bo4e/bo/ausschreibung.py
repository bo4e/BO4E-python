"""
Contains Ausschreibung class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.ausschreibungslos import Ausschreibungslos
    from ..com.zeitraum import Zeitraum
    from ..enum.ausschreibungsportal import Ausschreibungsportal
    from ..enum.ausschreibungsstatus import Ausschreibungsstatus
    from ..enum.ausschreibungstyp import Ausschreibungstyp
    from .geschaeftspartner import Geschaeftspartner


@postprocess_docstring
class Ausschreibung(Geschaeftsobjekt):
    """
    Das BO Ausschreibung dient zur detaillierten Darstellung von ausgeschriebenen Energiemengen in der Energiewirtschaft

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Ausschreibung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Ausschreibung.json>`_

    """

    typ: Annotated[Literal[Typ.AUSSCHREIBUNG], Field(alias="_typ")] = Typ.AUSSCHREIBUNG
    ausschreibungsnummer: Optional[str] = None
    """Vom Herausgeber der Ausschreibung vergebene eindeutige Nummer"""
    ausschreibungstyp: Optional["Ausschreibungstyp"] = None
    """Aufzählung für die Typisierung von Ausschreibungen"""
    ausschreibungsstatus: Optional["Ausschreibungsstatus"] = None
    """Bezeichnungen für die Ausschreibungsphasen"""
    ist_kostenpflichtig: Optional[bool] = None
    """Kennzeichen, ob die Ausschreibung kostenpflichtig ist"""
    veroeffentlichungszeitpunkt: Optional[pydantic.AwareDatetime] = None
    """Gibt den Veröffentlichungszeitpunkt der Ausschreibung an"""
    ausschreibender: Optional["Geschaeftspartner"] = None
    """
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein
    """
    abgabefrist: Optional["Zeitraum"] = None
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher entweder eine Dauer oder ein Zeitraum in Form von Start und Ende angegeben sein
    """
    bindefrist: Optional["Zeitraum"] = None
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher entweder eine Dauer oder ein Zeitraum in Form von Start und Ende angegeben sein
    """
    lose: Optional[list["Ausschreibungslos"]] = None
    """Die einzelnen Lose, aus denen sich die Ausschreibung zusammensetzt"""

    ausschreibungportal: Optional["Ausschreibungsportal"] = None
    """Aufzählung der unterstützten Ausschreibungsportale"""
    webseite: Optional[str] = None
    """Internetseite, auf der die Ausschreibung veröffentlicht wurde (falls vorhanden)"""
