"""
Contains Zaehler class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional
from decimal import Decimal
from datetime import datetime
import attr

from marshmallow import fields
from marshmallow_enum import EnumField

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.zaehlwerk import Zaehlwerk, ZaehlwerkSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.zaehlerauspraegung import Zaehlerauspraegung
from bo4e.enum.zaehlertyp import Zaehlertyp



# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Zaehler(Geschaeftsobjekt):
    """
    Object containing information about a meter/"Zaehler".
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.ZAEHLER)
    zaehlernummer: str = attr.ib(
        validator=attr.validators.instance_of(str)
    )  # Nummerierung des Zählers, vergeben durch den Messstellenbetreiber
    sparte: Sparte
    zaehlerauspraegung: Zaehlerauspraegung
    zaehlertyp: Zaehlertyp
    tarifart: Tarifart  # Spezifikation bezüglich unterstützter Tarifarten
    energierichtung: Energierichtung

    # optional attributes
    zaehlerkonstante: Optional[Decimal] = attr.ib(default=None)  # Zählerkonstante auf dem Zähler
    eichung_bis: Optional[datetime] = attr.ib(default=None)  # Bis zu diesem Datum ist der Zähler geeicht.
    letzte_eichung: Optional[datetime] = attr.ib(
        default=None
    )  # Zu diesem Datum fand die letzte Eichprüfung des Zählers statt.
    zaehlwerk: Optional[List[Zaehlwerk]] = attr.ib(default=None)  # Die Zählwerke des Zählers.
    zaehlerhersteller: Optional[Geschaeftspartner] = attr.ib(default=None)  # Der Hersteller des Zählers.


class ZaehlerSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Zaehler.
    """

    # class_name is needed to use the correct schema for deserialisation.
    # see function `deserialise` in geschaeftsobjekt.py
    class_name = Zaehler

    # required attributes
    zaehlernummer = fields.Str()
    sparte = EnumField(Sparte)
    zaehlerauspraegung = EnumField(Zaehlerauspraegung)
    zaehlertyp = EnumField(Zaehlertyp)
    tarifart = EnumField(Tarifart)
    energierichtung = EnumField(Energierichtung)

    # optional attributes
    zaehlerkonstante = fields.Decimal(missing=None)
    eichung_bis = fields.DateTime(missing=None)
    letzte_eichung = fields.DateTime(missing=None)
    zaehlwerk = fields.Nested(ZaehlwerkSchema, missing=None)
    zaehlerhersteller = fields.Nested(GeschaeftspartnerSchema, missing=None)
