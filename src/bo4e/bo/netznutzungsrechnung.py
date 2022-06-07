"""
Contains Netznutzungsrechnung class and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.rechnung import Rechnung, RechnungSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.nnrechnungsart import NNRechnungsart
from bo4e.enum.nnrechnungstyp import NNRechnungstyp
from bo4e.enum.sparte import Sparte


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Netznutzungsrechnung(Rechnung):
    """
    Modell für die Abbildung von Netznutzungsrechnungen

    .. HINT::
        `Netznutzungsrechnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/NetznutzungsrechnungSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = attrs.field(default=BoTyp.NETZNUTZUNGSRECHNUNG)
    #: Sparte (Strom, Gas ...) für die die Rechnung ausgestellt ist
    sparte: Sparte = attrs.field(validator=attrs.validators.instance_of(Sparte))
    absendercodenummer: str = attrs.field(validator=attrs.validators.matches_re(r"^\d{13}$"))
    """
    Die Rollencodenummer des Absenders (siehe :class:`Marktteilnehmer`).
    Über die Nummer können weitere Informationen zum Marktteilnehmer ermittelt werden.
    """
    empfaengercodenummer: str = attrs.field(validator=attrs.validators.matches_re(r"^\d{13}$"))
    """
    Die Rollencodenummer des Empfängers (siehe :class:`Marktteilnehmer`).
    Über die Nummer können weitere Informationen zum Marktteilnehmer ermittelt werden.
    """
    #: Aus der INVOIC entnommen
    nnrechnungsart: NNRechnungsart = attrs.field(validator=attrs.validators.instance_of(NNRechnungsart))
    #: Aus der INVOIC entnommen
    nnrechnungstyp: NNRechnungstyp = attrs.field(validator=attrs.validators.instance_of(NNRechnungstyp))

    #: Kennzeichen, ob es sich um ein Original (true) oder eine Kopie handelt (false)
    original: bool = attrs.field(validator=attrs.validators.instance_of(bool))
    #: Kennzeichen, ob es sich um eine simulierte Rechnung, z.B. zur Rechnungsprüfung handelt
    simuliert: bool = attrs.field(validator=attrs.validators.instance_of(bool))

    # optional attributes
    lokations_id: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    """
    Die Markt- oder Messlokations-Identifikation (als Malo/Melo-Id) der Lokation, auf die sich die Rechnung bezieht
    """


class NetznutzungsrechnungSchema(RechnungSchema):
    """
    Schema for de-/serialization of Netznutzungsrechnung
    """

    class_name = Netznutzungsrechnung  # type:ignore[assignment]

    # required attributes (additional to those of Rechnung)
    sparte = EnumField(Sparte)
    absendercodenummer = fields.Str()
    empfaengercodenummer = fields.Str()
    nnrechnungsart = EnumField(NNRechnungsart)
    nnrechnungstyp = EnumField(NNRechnungstyp)
    original = fields.Boolean()
    simuliert = fields.Boolean()
    # optional attributes
    lokations_id = fields.Str(allow_none=True)
