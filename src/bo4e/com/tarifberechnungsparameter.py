"""
Contains Tarifberechnungsparameter class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.preis import Preis, PreisSchema
from bo4e.com.tarifpreis import Tarifpreis, TarifpreisSchema
from bo4e.enum.messpreistyp import Messpreistyp
from bo4e.enum.tarifkalkulationsmethode import Tarifkalkulationsmethode

# yes. there is no description in the official docs.
# https://github.com/Hochfrequenz/BO4E-python/issues/328

# pylint: disable=too-few-public-methods, empty-docstring, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Tarifberechnungsparameter(COM):
    """

    .. HINT::
        `Tarifberechnungsparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TarifberechnungsparameterSchema.json>`_

    """

    # there are no required attributes
    # optional attributes

    #: Gibt an, wie die Einzelpreise des Tarifes zu verarbeiten sind
    berechnungsmethode: Optional[Tarifkalkulationsmethode] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Tarifkalkulationsmethode))
    )
    #: True, falls der Messpreis im Grundpreis (GP) enthalten ist
    messpreis_in_gp_enthalten: Optional[bool] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(bool))
    )

    messpreis_beruecksichtigen: Optional[bool] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(bool))
    )
    """
    True, falls bei der Bildung des Durchschnittspreises für die Höchst- und Mindestpreisbetrachtung der Messpreis mit
    berücksichtigt wird
    """

    #: Typ des Messpreises
    messpreistyp: Optional[Messpreistyp] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Messpreistyp))
    )

    #: Im Preis bereits eingeschlossene Leistung (für Gas)
    kw_inklusive: Optional[Decimal] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Decimal))
    )
    # todo: type decimal is most likely wrong: https://github.com/Hochfrequenz/BO4E-python/issues/327

    #: Intervall, indem die über "kwInklusive" hinaus abgenommene Leistung kostenpflichtig wird (z.B. je 5 kW 20 EURO)
    kw_weitere_mengen: Optional[Decimal] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Decimal))
    )
    # todo: type decimal is most likely wrong: https://github.com/Hochfrequenz/BO4E-python/issues/327

    #: Höchstpreis für den Durchschnitts-Arbeitspreis NT
    hoechstpreis_n_t: Optional[Preis] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Preis))
    )
    #: Höchstpreis für den Durchschnitts-Arbeitspreis HT
    hoechstpreis_h_t: Optional[Preis] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Preis))
    )
    #: Mindestpreis für den Durchschnitts-Arbeitspreis
    mindestpreis: Optional[Preis] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Preis))
    )
    #: Liste mit zusätzlichen Preisen, beispielsweise Messpreise und/oder Leistungspreise
    zusatzpreise: Optional[List[Tarifpreis]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Tarifpreis),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
    )


class TarifberechnungsparameterSchema(COMSchema):
    """
    Schema for de-/serialization of Tarifberechnungsparameter
    """

    class_name = Tarifberechnungsparameter
    # optional attributes
    berechnungsmethode = EnumField(Tarifkalkulationsmethode, allow_none=True)
    messpreis_in_gp_enthalten = fields.Bool(allow_none=True, data_key="messpreisInGpEnthalten")
    messpreis_beruecksichtigen = fields.Bool(allow_none=True, data_key="messpreisBeruecksichtigen")
    messpreistyp = EnumField(Messpreistyp, allow_none=True)
    kw_inklusive = fields.Decimal(as_string=True, allow_none=True, data_key="kwInklusive")
    kw_weitere_mengen = fields.Decimal(as_string=True, allow_none=True, data_key="kwWeitereMengen")
    hoechstpreis_n_t = fields.Nested(PreisSchema, data_key="hoechstpreisHT", allow_none=True)
    hoechstpreis_h_t = fields.Nested(PreisSchema, data_key="hoechstpreisNT", allow_none=True)
    mindestpreis = fields.Nested(PreisSchema, allow_none=True)
    zusatzpreise = fields.List(fields.Nested(TarifpreisSchema), allow_none=True)
