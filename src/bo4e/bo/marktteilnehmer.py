from enum import Enum
import attr
from attr.validators import matches_re

from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.cases import JavaScriptMixin
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


class MarktteilnehmerSchema(GeschaeftspartnerSchema, JavaScriptMixin):
    # required attributes
    marktrolle = EnumField(Marktrolle)
    rollencodenummer = fields.Str()
    rollencodetyp = EnumField(Rollencodetyp)

    # optional attributes
    makoadresse = fields.Str(missing=None)

    # required attributes with default value
    bo_typ = EnumField(BoTyp)

    @post_load
    def make_marktteilnehmer(self, data, **kwargs) -> Marktteilnehmer:
        if data["bo_typ"] == BoTyp.MARKTTEILNEHMER:
            return Marktteilnehmer(**data)
        return data
