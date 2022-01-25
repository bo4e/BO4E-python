"""
Contains Ausschreibung class and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.ausschreibungslos import Ausschreibungslos, AusschreibungslosSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.ausschreibungsportal import Ausschreibungsportal
from bo4e.enum.ausschreibungsstatus import Ausschreibungsstatus
from bo4e.enum.ausschreibungstyp import Ausschreibungstyp
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class Ausschreibung(Geschaeftsobjekt):
    """
    Das BO Ausschreibung dient zur detaillierten Darstellung von ausgeschriebenen Energiemengen in der Energiewirtschaft

    .. HINT::
        `Ausschreibung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/master/json_schemas/bo/AusschreibungSchema.json>`_
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.AUSSCHREIBUNG)
    #: Vom Herausgeber der Ausschreibung vergebene eindeutige Nummer
    ausschreibungsnummer: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Aufzählung für die Typisierung von Ausschreibungen
    ausschreibungstyp: Ausschreibungstyp = attr.ib(validator=attr.validators.instance_of(Ausschreibungstyp))
    #: Bezeichnungen für die Ausschreibungsphasen
    ausschreibungsstatus: Ausschreibungsstatus = attr.ib(validator=attr.validators.instance_of(Ausschreibungsstatus))
    #: Kennzeichen, ob die Ausschreibung kostenpflichtig ist
    kostenpflichtig: bool = attr.ib(validator=attr.validators.instance_of(bool))
    #: Gibt den Veröffentlichungszeitpunkt der Ausschreibung an
    veroeffentlichungszeitpunkt: datetime = attr.ib(validator=attr.validators.instance_of(datetime))
    ausschreibender: Geschaeftspartner = attr.ib(validator=attr.validators.instance_of(Geschaeftspartner))
    """
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein
    """
    abgabefrist: Zeitraum = attr.ib(validator=attr.validators.instance_of(Zeitraum))
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher entweder eine Dauer oder ein Zeitraum in Form von Start und Ende angegeben sein
    """
    bindefrist: Zeitraum = attr.ib(validator=attr.validators.instance_of(Zeitraum))
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher entweder eine Dauer oder ein Zeitraum in Form von Start und Ende angegeben sein
    """
    #: Die einzelnen Lose, aus denen sich die Ausschreibung zusammensetzt
    lose: List[Ausschreibungslos] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Ausschreibungslos),
            iterable_validator=check_list_length_at_least_one,
        )
    )

    # optional attributes
    #: Aufzählung der unterstützten Ausschreibungsportale
    ausschreibungportal: Optional[Ausschreibungsportal] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Ausschreibungsportal))
    )
    #: Internetseite, auf der die Ausschreibung veröffentlicht wurde (falls vorhanden)
    webseite: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )


class AusschreibungSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Ausschreibung
    """

    class_name = Ausschreibung

    # required attributes
    ausschreibungsnummer = fields.Str()
    ausschreibungstyp = EnumField(Ausschreibungstyp)
    ausschreibungsstatus = EnumField(Ausschreibungsstatus)
    kostenpflichtig = fields.Bool()
    veroeffentlichungszeitpunkt = fields.DateTime()
    ausschreibender = fields.Nested(GeschaeftspartnerSchema)
    abgabefrist = fields.Nested(ZeitraumSchema)
    bindefrist = fields.Nested(ZeitraumSchema)
    lose = fields.List(fields.Nested(AusschreibungslosSchema))

    # optional attributes
    ausschreibungportal = EnumField(Ausschreibungsportal, allow_none=True)
    webseite = fields.Str(allow_none=True)
