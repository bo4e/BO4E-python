"""
Contains Regionaltarif class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import List, Optional

import attr
from marshmallow import fields

from bo4e.bo.tarifinfo import Tarifinfo, TarifinfoSchema
from bo4e.com.regionalepreisgarantie import RegionalePreisgarantie, RegionalePreisgarantieSchema
from bo4e.com.regionaleraufabschlag import RegionalerAufAbschlag, RegionalerAufAbschlagSchema
from bo4e.com.regionaletarifpreisposition import RegionaleTarifpreisposition, RegionaleTarifpreispositionSchema
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter, TarifberechnungsparameterSchema
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung, TarifeinschraenkungSchema
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, empty-docstring
@attr.s(auto_attribs=True, kw_only=True)
class Regionaltarif(Tarifinfo):
    # no description in the official docs.
    # https://github.com/Hochfrequenz/BO4E-python/issues/338
    """

    .. HINT::
        `Regionaltarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/master/json_schemas/bo/RegionaltarifSchema.json>`_
    """

    bo_typ: BoTyp = attr.ib(default=BoTyp.REGIONALTARIF)
    # required attributes
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: datetime = attr.ib(validator=attr.validators.instance_of(datetime))
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Tarifberechnungsparameter = attr.ib(
        validator=attr.validators.instance_of(Tarifberechnungsparameter)
    )
    #: Die festgelegten Preise mit regionaler Eingrenzung, z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: List[RegionaleTarifpreisposition] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(RegionaleTarifpreisposition),
            iterable_validator=check_list_length_at_least_one,
        )
    )

    # optional attributes
    #: Auf- und Abschläge auf die Preise oder Kosten mit regionaler Eingrenzung
    tarif_auf_abschlaege: Optional[List[RegionalerAufAbschlag]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(RegionalerAufAbschlag),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    #: Festlegung von Garantien für bestimmte Preisanteile
    preisgarantien: Optional[List[RegionalePreisgarantie]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(RegionalePreisgarantie),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Optional[Tarifeinschraenkung] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Tarifeinschraenkung))
    )


class RegionaltarifSchema(TarifinfoSchema):
    """
    Schema for de-/serialization of Regionaltarif
    """

    class_name = Regionaltarif  # type:ignore[assignment]

    # required attributes
    preisstand = fields.DateTime()
    berechnungsparameter = fields.Nested(TarifberechnungsparameterSchema)
    tarifpreise = fields.List(fields.Nested(RegionaleTarifpreispositionSchema))

    # optional attributes
    tarif_auf_abschlaege = fields.List(
        fields.Nested(RegionalerAufAbschlagSchema), allow_none=True, data_key="tarifAufAbschlaege"
    )
    preisgarantien = fields.List(fields.Nested(RegionalePreisgarantieSchema), allow_none=True)
    tarifeinschraenkung = fields.Nested(TarifeinschraenkungSchema, allow_none=True)
