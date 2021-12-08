"""
Contains Zaehler class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.zaehlwerk import Zaehlwerk, ZaehlwerkSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.zaehlerauspraegung import Zaehlerauspraegung
from bo4e.enum.zaehlertyp import Zaehlertyp


# pylint: disable=unused-argument
def at_least_one_zaehlwerk(instance, attribute, value):
    """
    Ensures that the Zaehler has at least one entry in the zaehlwerke list.
    """
    if len(value) == 0:
        raise ValueError("The Zaehler must have at least 1 Zaehlwerk")


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
    zaehlwerke: List[Zaehlwerk] = attr.ib(validator=at_least_one_zaehlwerk)
    tarifart: Tarifart  # Spezifikation bezüglich unterstützter Tarifarten

    # optional attributes
    zaehlerkonstante: Optional[Decimal] = attr.ib(default=None)  # Zählerkonstante auf dem Zähler
    eichung_bis: Optional[datetime] = attr.ib(default=None)  # Bis zu diesem Datum ist der Zähler geeicht.
    letzte_eichung: Optional[datetime] = attr.ib(
        default=None
    )  # Zu diesem Datum fand die letzte Eichprüfung des Zählers statt.
    zaehlerhersteller: Optional[Geschaeftspartner] = attr.ib(default=None)  # Der Hersteller des Zählers.


class ZaehlerSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Zaehler.
    """

    # class_name is needed to use the correct schema for deserialisation.
    # see function `deserialize` in geschaeftsobjekt.py
    class_name = Zaehler

    # required attributes
    zaehlernummer = fields.Str()
    sparte = EnumField(Sparte)
    zaehlerauspraegung = EnumField(Zaehlerauspraegung)
    zaehlertyp = EnumField(Zaehlertyp)
    tarifart = EnumField(Tarifart)
    zaehlwerke = fields.Nested(ZaehlwerkSchema, many=True)

    # optional attributes
    zaehlerkonstante = fields.Decimal(load_default=None, as_string=True)
    eichung_bis = fields.DateTime(load_default=None)
    letzte_eichung = fields.DateTime(load_default=None)

    zaehlerhersteller = fields.Nested(GeschaeftspartnerSchema, load_default=None)
