"""
Contains Ansprechpartner class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields
from marshmallow_enum import EnumField
from bo4e.com.rufnummer import Rufnummer, RufnummerSchema
from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.zustaendigkeit import Zustaendigkeit, ZustaendigkeitSchema
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.titel import Titel

# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Ansprechpartner(Geschaeftsobjekt):
    """
    Object containing information about a Ansprechpartner
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.ANSPRECHPARTNER)
    nachname: str
    geschaeftspartner: Geschaeftspartner

    # optional attributes
    anrede: Anrede = attr.ib(default=None)
    individuelle_anrede: str = attr.ib(default=None)
    titel: Titel = attr.ib(default=None)
    vorname: str = attr.ib(default=None)
    e_mail_adresse: str = attr.ib(default=None)
    kommentar: str = attr.ib(default=None)
    adresse: Adresse = attr.ib(default=None)
    rufnummer: Rufnummer = attr.ib(default=None)
    zustaendigkeit: Zustaendigkeit = attr.ib(default=None)


class AnsprechpartnerSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Ansprechpartner.
    """

    # class_name is needed to use the correct schema for deserialisation.
    # see function `deserialize` in geschaeftsobjekt.py
    class_name = Ansprechpartner

    # required attributes
    nachname = fields.Str()
    geschaeftspartner = fields.Nested(GeschaeftspartnerSchema)

    # optional attributes
    anrede = EnumField(Anrede, missing=None)
    individuelle_anrede = fields.Str(missing=None)
    titel = EnumField(Titel, missing=None)
    vorname = fields.Str(missing=None)
    e_mail_adresse = fields.Str(missing=None)
    kommentar = fields.Str(missing=None)
    adresse = fields.Nested(AdresseSchema, missing=None)
    rufnummer = fields.Nested(RufnummerSchema, missing=None)
    zustaendigkeit = fields.Nested(ZustaendigkeitSchema, missing=None)
