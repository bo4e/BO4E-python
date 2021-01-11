import attr

from marshmallow import fields
from marshmallow_enum import EnumField

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.cases import JavaScriptMixin
from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.enum.anrede import Anrede
from bo4e.enum.kontaktart import Kontaktart
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.botyp import BoTyp


@attr.s(auto_attribs=True, kw_only=True)
class Geschaeftspartner(Geschaeftsobjekt):
    """
    Objekt zur Aufnahme der Information zu einem Geschaeftspartner
    """

    anrede: Anrede = attr.ib(default=None)
    name1: str
    name2: str = attr.ib(default=None)
    name3: str = attr.ib(default=None)
    gewerbekennzeichnung: bool
    hrnummer: str = attr.ib(default=None)
    amtsgericht: str = attr.ib(default=None)
    kontaktweg: Kontaktart = attr.ib(default=None)
    umsatzsteuer_id: str = attr.ib(default=None)
    glaeubiger_id: str = attr.ib(default=None)
    e_mail_adresse: str = attr.ib(default=None)
    website: str = attr.ib(default=None)
    geschaeftspartnerrolle: Geschaeftspartnerrolle
    partneradresse: Adresse

    bo_typ: BoTyp = attr.ib(default=BoTyp.GESCHAEFTSPARTNER)


class GeschaeftspartnerSchema(GeschaeftsobjektSchema, JavaScriptMixin):
    class_name = Geschaeftspartner

    anrede = EnumField(Anrede, missing=None)
    name1 = fields.Str()
    name2 = fields.Str(missing=None)
    name3 = fields.Str(missing=None)
    gewerbekennzeichnung = fields.Bool()
    hrnummer = fields.Str(missing=None)
    amtsgericht = fields.Str(missing=None)
    kontaktweg = EnumField(Kontaktart, missing=None)
    umsatzsteuer_id = fields.Str(missing=None)
    glaeubiger_id = fields.Str(missing=None)
    e_mail_adresse = fields.Str(missing=None)
    website = fields.Str(missing=None)
    geschaeftspartnerrolle = EnumField(Geschaeftspartnerrolle)
    partneradresse = fields.Nested(AdresseSchema)

    bo_typ = EnumField(BoTyp, missing=None)
