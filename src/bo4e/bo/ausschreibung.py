"""
Contains Ausschreibung class and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from pydantic import Field

from ..com.ausschreibungslos import Ausschreibungslos
from ..com.zeitraum import Zeitraum
from ..enum.ausschreibungsportal import Ausschreibungsportal
from ..enum.ausschreibungsstatus import Ausschreibungsstatus
from ..enum.ausschreibungstyp import Ausschreibungstyp
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt
from .geschaeftspartner import Geschaeftspartner


@postprocess_docstring
class Ausschreibung(Geschaeftsobjekt):
    """
    Das BO Ausschreibung dient zur detaillierten Darstellung von ausgeschriebenen Energiemengen in der Energiewirtschaft

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Ausschreibung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Ausschreibung.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.AUSSCHREIBUNG
    #: Vom Herausgeber der Ausschreibung vergebene eindeutige Nummer
    ausschreibungsnummer: Optional[str] = None
    #: Aufzählung für die Typisierung von Ausschreibungen
    ausschreibungstyp: Optional[Ausschreibungstyp] = None
    #: Bezeichnungen für die Ausschreibungsphasen
    ausschreibungsstatus: Optional[Ausschreibungsstatus] = None
    #: Kennzeichen, ob die Ausschreibung kostenpflichtig ist
    ist_kostenpflichtig: Optional[bool] = None
    #: Gibt den Veröffentlichungszeitpunkt der Ausschreibung an
    veroeffentlichungszeitpunkt: Optional[datetime] = None
    ausschreibender: Optional[Geschaeftspartner] = None
    """
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein
    """
    abgabefrist: Optional[Zeitraum] = None
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher entweder eine Dauer oder ein Zeitraum in Form von Start und Ende angegeben sein
    """
    bindefrist: Optional[Zeitraum] = None
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher entweder eine Dauer oder ein Zeitraum in Form von Start und Ende angegeben sein
    """
    #: Die einzelnen Lose, aus denen sich die Ausschreibung zusammensetzt
    lose: Optional[list[Ausschreibungslos]] = None

    #: Aufzählung der unterstützten Ausschreibungsportale
    ausschreibungportal: Optional[Ausschreibungsportal] = None
    #: Internetseite, auf der die Ausschreibung veröffentlicht wurde (falls vorhanden)
    webseite: Optional[str] = None
