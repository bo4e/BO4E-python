"""
Contains Vertrag class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.unterschrift import Unterschrift, UnterschriftSchema
from bo4e.com.vertragskonditionen import Vertragskonditionen, VertragskonditionenSchema
from bo4e.com.vertragsteil import Vertragsteil, VertragsteilSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.vertragsart import Vertragsart
from bo4e.enum.vertragsstatus import Vertragsstatus


# pylint: disable=unused-argument
def at_least_one_vertragsteil(instance, attribute, value):
    """
    Ensures that the Vertrag has at least one entry in the Vertragsteile list.
    """
    if len(value) == 0:
        raise ValueError("The Vertrag must have at least 1 Vertragsteil")


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Vertrag(Geschaeftsobjekt):
    """
    Modell für die Abbildung von Vertragsbeziehungen.
    Das Objekt dient dazu, alle Arten von Verträgen, die in der Energiewirtschaft Verwendung finden, abzubilden.
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.VERTRAG)
    vertragsnummer: str = attr.ib(validator=attr.validators.instance_of(str))
    vertragsart: Vertragsart = attr.ib(validator=attr.validators.instance_of(Vertragsart))
    vertragsstatus: Vertragsstatus = attr.ib(validator=attr.validators.instance_of(Vertragsstatus))
    sparte: Sparte = attr.ib(validator=attr.validators.instance_of(Sparte))
    vertragsbeginn: datetime = attr.ib(validator=attr.validators.instance_of(datetime))
    vertragsende: datetime = attr.ib(validator=attr.validators.instance_of(datetime))

    vertragspartner1: Geschaeftspartner = attr.ib(validator=attr.validators.instance_of(Geschaeftspartner))
    vertragspartner2: Geschaeftspartner = attr.ib(validator=attr.validators.instance_of(Geschaeftspartner))
    vertragsteile: List[Vertragsteil] = attr.ib(validator=at_least_one_vertragsteil)

    # optional attributes
    beschreibung: Optional[str] = attr.ib(default=None)
    vertragskonditionen: Optional[Vertragskonditionen] = attr.ib(default=None)
    unterzeichnervp1: Optional[List[Unterschrift]] = attr.ib(default=None)
    unterzeichnervp2: Optional[List[Unterschrift]] = attr.ib(default=None)


class VertragSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Vertrag.
    """

    # class_name is needed to use the correct schema for deserialisation.
    # see function `deserialize` in geschaeftsobjekt.py
    class_name = Vertrag

    # required attributes
    vertragsnummer = fields.Str()
    vertragsart = EnumField(Vertragsart)
    vertragsstatus = EnumField(Vertragsstatus)
    sparte = EnumField(Sparte)
    vertragsbeginn = fields.DateTime()
    vertragsende = fields.DateTime()

    vertragspartner1 = fields.Nested(GeschaeftspartnerSchema)
    vertragspartner2 = fields.Nested(GeschaeftspartnerSchema)
    vertragsteile = fields.Nested(VertragsteilSchema, many=True)

    # optional attributes
    beschreibung = fields.Str(load_default=None)
    vertragskonditionen = fields.Nested(VertragskonditionenSchema, load_default=None)
    unterzeichnervp1 = fields.Nested(UnterschriftSchema, load_default=None, many=True)
    unterzeichnervp2 = fields.Nested(UnterschriftSchema, load_default=None, many=True)
