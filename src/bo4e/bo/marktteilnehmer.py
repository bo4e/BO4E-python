"""
Contains Marktteilnehmer class
and corresponding marshmallow schema for de-/serialization
"""
import attrs
from attrs.validators import matches_re
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.marktrolle import Marktrolle
from bo4e.enum.rollencodetyp import Rollencodetyp


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Marktteilnehmer(Geschaeftspartner):
    """
    Objekt zur Aufnahme der Information zu einem Marktteilnehmer

    .. HINT::
        `Marktteilnehmer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/MarktteilnehmerSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = attrs.field(default=BoTyp.MARKTTEILNEHMER)
    #: Gibt im Klartext die Bezeichnung der Marktrolle an
    marktrolle: Marktrolle
    #: Gibt die Codenummer der Marktrolle an
    rollencodenummer: str = attrs.field(validator=matches_re(r"^\d{13}$"))
    #: Gibt den Typ des Codes an
    rollencodetyp: Rollencodetyp

    # optional attributes
    #: Die 1:1-Kommunikationsadresse des Marktteilnehmers; Diese wird in der Marktkommunikation verwendet.
    makoadresse: str = attrs.field(default=None)


class MarktteilnehmerSchema(GeschaeftspartnerSchema):
    """
    Schema for de-/serialization of Marktteilnehmer.
    """

    # class_name is needed to use the correct schema for deserialization.
    # see function `deserialize` in geschaeftsobjekt.py
    class_name = Marktteilnehmer

    # required attributes
    marktrolle = EnumField(Marktrolle)
    rollencodenummer = fields.Str()
    rollencodetyp = EnumField(Rollencodetyp)

    # optional attributes
    makoadresse = fields.Str(load_default=None)
