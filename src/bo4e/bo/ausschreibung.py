"""
Contains Ausschreibung class and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import List, Optional


from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.ausschreibungslos import Ausschreibungslos
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.ausschreibungsportal import Ausschreibungsportal
from bo4e.enum.ausschreibungsstatus import Ausschreibungsstatus
from bo4e.enum.ausschreibungstyp import Ausschreibungstyp
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
from pydantic import conlist


class Ausschreibung(Geschaeftsobjekt):
    """
    Das BO Ausschreibung dient zur detaillierten Darstellung von ausgeschriebenen Energiemengen in der Energiewirtschaft

    .. HINT::
        `Ausschreibung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/AusschreibungSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.AUSSCHREIBUNG
    #: Vom Herausgeber der Ausschreibung vergebene eindeutige Nummer
    ausschreibungsnummer: str
    #: Aufzählung für die Typisierung von Ausschreibungen
    ausschreibungstyp: Ausschreibungstyp
    #: Bezeichnungen für die Ausschreibungsphasen
    ausschreibungsstatus: Ausschreibungsstatus
    #: Kennzeichen, ob die Ausschreibung kostenpflichtig ist
    kostenpflichtig: bool
    #: Gibt den Veröffentlichungszeitpunkt der Ausschreibung an
    veroeffentlichungszeitpunkt: datetime
    ausschreibender: Geschaeftspartner
    """
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein
    """
    abgabefrist: Zeitraum
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher entweder eine Dauer oder ein Zeitraum in Form von Start und Ende angegeben sein
    """
    bindefrist: Zeitraum
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher entweder eine Dauer oder ein Zeitraum in Form von Start und Ende angegeben sein
    """
    #: Die einzelnen Lose, aus denen sich die Ausschreibung zusammensetzt
    lose: conlist(Ausschreibungslos, min_items=1)

    # optional attributes
    #: Aufzählung der unterstützten Ausschreibungsportale
    ausschreibungportal: Ausschreibungsportal = None
    #: Internetseite, auf der die Ausschreibung veröffentlicht wurde (falls vorhanden)
    webseite: str = None
