import attr
from attr.validators import matches_re

from marshmallow import fields
from marshmallow_enum import EnumField

from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.marktrolle import Marktrolle
from bo4e.enum.rollencodetyp import Rollencodetyp


@attr.s(auto_attribs=True, kw_only=True)
class Marktteilnehmer(Geschaeftspartner):
    """
    Objekt zur Aufnahme der Information zu einem Marktteilnehmer
    """

    # required attributes
    marktrolle: Marktrolle
    rollencodenummer: str = attr.ib(validator=matches_re(r"^\d{13}$"))
    rollencodetyp: Rollencodetyp

    # optional attributes
    makoadresse: str = attr.ib(default=None)

    # required attributes with default value
    bo_typ: BoTyp = attr.ib(default=BoTyp.MARKTTEILNEHMER)

class MarktteilnehmerSchema(GeschaeftspartnerSchema):
    # class_name is needed to use the correct schema for deserialisation.
    # see fuction `deserialise` in geschaeftsobjekt.py
    class_name = Marktteilnehmer

    # required attributes
    marktrolle = EnumField(Marktrolle)
    rollencodenummer = fields.Str()
    rollencodetyp = EnumField(Rollencodetyp)

    # optional attributes
    makoadresse = fields.Str(missing=None)
