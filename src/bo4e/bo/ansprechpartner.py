"""
Contains Ansprechpartner class
and corresponding marshmallow schema for de-/serialization
"""
import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.com.rufnummer import Rufnummer
from bo4e.com.zustaendigkeit import Zustaendigkeit
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.titel import Titel


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Ansprechpartner(Geschaeftsobjekt):
    """
    Object containing information about a Ansprechpartner

    .. HINT::
        `Ansprechpartner JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/AnsprechpartnerSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.ANSPRECHPARTNER
    nachname: str  #: Nachname (Familienname) des Ansprechpartners
    geschaeftspartner: Geschaeftspartner  #: Der Geschäftspartner, für den dieser Ansprechpartner modelliert wird

    # optional attributes
    anrede: Anrede = None  #: Mögliche Anrede des Ansprechpartners
    individuelle_anrede: str = None
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Sehr geehrte Frau Müller, sehr geehrter Herr Dr. Müller"
    """

    titel: Titel = None  #: Möglicher Titel des Ansprechpartners
    vorname: str = None  #: Vorname des Ansprechpartners
    e_mail_adresse: str = None  #: E-Mail Adresse
    kommentar: str = None  #: Weitere Informationen zum Ansprechpartner
    #: Adresse des Ansprechpartners, falls diese von der Adresse des Geschäftspartners abweicht
    adresse: Adresse = None
    #: Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist
    rufnummer: Rufnummer = None  # todo: make this a list and rename to rufnummern
    #: Liste der Abteilungen und Zuständigkeiten des Ansprechpartners
    zustaendigkeit: Zustaendigkeit = attrs.field(
        default=None
    )  # todo: make this a list and rename to "zustaendigkeiten"


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
    individuelle_anrede = fields.Str(load_default=None, data_key="individuelleAnrede")
    titel = EnumField(Titel, load_default=None)
    vorname = fields.Str(load_default=None)
    e_mail_adresse = fields.Str(load_default=None, data_key="eMailAdresse")
    kommentar = fields.Str(load_default=None)
    adresse = fields.Nested(AdresseSchema, load_default=None)
    rufnummer = fields.Nested(RufnummerSchema, load_default=None)
    zustaendigkeit = fields.Nested(ZustaendigkeitSchema, load_default=None)
