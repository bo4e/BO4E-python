"""
Contains Geschaeftspartner class
and corresponding marshmallow schema for de-/serialization
"""
# pylint: disable=too-many-instance-attributes, too-few-public-methods
from typing import List, Optional, Type

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart


@attr.s(auto_attribs=True, kw_only=True)
class Geschaeftspartner(Geschaeftsobjekt):
    """
    Object containing information about a Geschaeftspartner
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.GESCHAEFTSPARTNER)
    name1: str
    gewerbekennzeichnung: bool
    geschaeftspartnerrolle: List[Geschaeftspartnerrolle] = attr.ib(validator=attr.validators.instance_of(List))

    # optional attributes
    anrede: Anrede = attr.ib(default=None)
    name2: Optional[str] = attr.ib(default=None)
    name3: Optional[str] = attr.ib(default=None)
    hrnummer: Optional[str] = attr.ib(default=None)
    amtsgericht: Optional[str] = attr.ib(default=None)
    kontaktweg: List[Kontaktart] = attr.ib(default=[])
    umsatzsteuer_id: Optional[str] = attr.ib(default=None)
    glaeubiger_id: Optional[str] = attr.ib(default=None)
    e_mail_adresse: Optional[str] = attr.ib(default=None)
    website: Optional[str] = attr.ib(default=None)
    partneradresse: Adresse = attr.ib(default=None)


class GeschaeftspartnerSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Geschaeftspartner.
    """

    # class_name is needed to use the correct schema for deserialisation.
    # see function `deserialize` in geschaeftsobjekt.py
    class_name: Type[Geschaeftspartner] = Geschaeftspartner

    # required attributes
    name1 = fields.Str()
    gewerbekennzeichnung = fields.Bool()
    geschaeftspartnerrolle = fields.List(EnumField(Geschaeftspartnerrolle))

    # optional attributes
    anrede = EnumField(Anrede, load_default=None)
    name2 = fields.Str(load_default=None)
    name3 = fields.Str(load_default=None)
    hrnummer = fields.Str(load_default=None)
    amtsgericht = fields.Str(load_default=None)
    kontaktweg = fields.List(EnumField(Kontaktart), load_default=None)
    umsatzsteuer_id = fields.Str(load_default=None)
    glaeubiger_id = fields.Str(load_default=None)
    e_mail_adresse = fields.Str(load_default=None)
    website = fields.Str(load_default=None)
    partneradresse = fields.Nested(AdresseSchema, load_default=None)
