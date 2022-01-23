"""
Contains Ansprechpartner class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.com.rufnummer import Rufnummer, RufnummerSchema
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
    nachname: str  #: Nachname (Familienname) des Ansprechpartners
    geschaeftspartner: Geschaeftspartner  #: Der Geschäftspartner, für den dieser Ansprechpartner modelliert wird

    # optional attributes
    anrede: Anrede = attr.ib(default=None)  #: Mögliche Anrede des Ansprechpartners
    individuelle_anrede: str = attr.ib(default=None)
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Sehr geehrte Frau Müller, sehr geehrter Herr Dr. Müller"
    """

    titel: Titel = attr.ib(default=None)  #: Möglicher Titel des Ansprechpartners
    vorname: str = attr.ib(default=None)  #: Vorname des Ansprechpartners
    e_mail_adresse: str = attr.ib(default=None)  #: E-Mail Adresse
    kommentar: str = attr.ib(default=None)  #: Weitere Informationen zum Ansprechpartner
    #: Adresse des Ansprechpartners, falls diese von der Adresse des Geschäftspartners abweicht
    adresse: Adresse = attr.ib(default=None)
    #: Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist
    rufnummer: Rufnummer = attr.ib(default=None)  # todo: make this a list and rename to rufnummern
    #: Liste der Abteilungen und Zuständigkeiten des Ansprechpartners
    zustaendigkeit: Zustaendigkeit = attr.ib(default=None)  # todo: make this a list and rename to "zustaendigkeiten"


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
    anrede = EnumField(Anrede, load_default=None)
    individuelle_anrede = fields.Str(load_default=None)
    titel = EnumField(Titel, load_default=None)
    vorname = fields.Str(load_default=None)
    e_mail_adresse = fields.Str(load_default=None)
    kommentar = fields.Str(load_default=None)
    adresse = fields.Nested(AdresseSchema, load_default=None)
    rufnummer = fields.Nested(RufnummerSchema, load_default=None)
    zustaendigkeit = fields.Nested(ZustaendigkeitSchema, load_default=None)
