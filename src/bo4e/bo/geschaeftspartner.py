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
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein.
    Hinweis: Marktteilnehmer haben ein eigenes BO, welches sich von diesem BO ableitet.
    Hier sollte daher keine Zuordnung zu Marktrollen erfolgen.
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.GESCHAEFTSPARTNER)
    name1: str
    """
    Erster Teil des Namens.
    Hier kann der Firmenname oder bei Privatpersonen beispielsweise der Nachname dagestellt werden.
    Beispiele: Yellow Strom GmbH oder Hagen
    """
    # todo: replace name1/2/3 with something more readable. no one wants to deal with that. maybe serialize as name1/2/3
    # but resolve to readable python fields under the hood

    gewerbekennzeichnung: bool
    """
    Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)
    oder eine Privatperson handelt. (gewerbeKennzeichnung = false)
    """
    #: Rollen, die die Geschäftspartner inne haben (z.B. Interessent, Kunde)
    geschaeftspartnerrolle: List[Geschaeftspartnerrolle] = attr.ib(validator=attr.validators.instance_of(List))
    # todo: rename to plural

    # optional attributes
    #: Die Anrede für den GePa, Z.B. "Herr"
    anrede: Anrede = attr.ib(default=None)
    name2: Optional[str] = attr.ib(default=None)
    """
    Zweiter Teil des Namens.
    Hier kann der eine Erweiterung zum Firmennamen oder bei Privatpersonen beispielsweise der Vorname dagestellt werden.
    Beispiele: Bereich Süd oder Nina
    """

    name3: Optional[str] = attr.ib(default=None)
    """
    Dritter Teil des Namens.
    Hier können weitere Ergänzungen zum Firmennamen oder bei Privatpersonen Zusätze zum Namen dagestellt werden.
    Beispiele: und Afrika oder Sängerin
    """
    #: Handelsregisternummer des Geschäftspartners
    hrnummer: Optional[str] = attr.ib(default=None)
    #: Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat
    amtsgericht: Optional[str] = attr.ib(default=None)
    #: Bevorzugte Kontaktwege des Geschäftspartners
    kontaktweg: List[Kontaktart] = attr.ib(default=[])
    #: Die Steuer-ID des Geschäftspartners; Beispiel: "DE 813281825"
    umsatzsteuer_id: Optional[str] = attr.ib(default=None)
    #: Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird; Z.B. "DE 47116789"
    glaeubiger_id: Optional[str] = attr.ib(default=None)
    #: E-Mail-Adresse des Ansprechpartners. Z.B. "info@hochfrequenz.de"
    e_mail_adresse: Optional[str] = attr.ib(default=None)
    #: Internetseite des Marktpartners
    website: Optional[str] = attr.ib(default=None)
    #: Adressen der Geschäftspartner, an denen sich der Hauptsitz befindet
    partneradresse: Adresse = attr.ib(default=None)  # todo: is it plural or not? the docs are bad


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
