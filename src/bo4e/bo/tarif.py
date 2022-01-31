"""
Contains Tarif class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import List, Optional

import attr
from marshmallow import fields

from bo4e.bo.tarifinfo import Tarifinfo, TarifinfoSchema
from bo4e.com.aufabschlagregional import AufAbschlagRegional, AufAbschlagRegionalSchema
from bo4e.com.preisgarantie import Preisgarantie, PreisgarantieSchema
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter, TarifberechnungsparameterSchema
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung, TarifeinschraenkungSchema
from bo4e.com.tarifpreispositionproort import TarifpreispositionProOrt, TarifpreispositionProOrtSchema
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Tarif(Tarifinfo):
    """
    Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen

    .. HINT::
        `Tarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/master/json_schemas/bo/TarifSchema.json>`_

    """

    bo_typ: BoTyp = attr.ib(default=BoTyp.TARIF)
    # required attributes
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: datetime = attr.ib(validator=attr.validators.instance_of(datetime))
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Tarifberechnungsparameter = attr.ib(
        validator=attr.validators.instance_of(Tarifberechnungsparameter)
    )
    #: Die festgelegten Preise mit regionaler Eingrenzung z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: List[TarifpreispositionProOrt] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(TarifpreispositionProOrt),
            iterable_validator=check_list_length_at_least_one,
        )
    )

    # optional attributes
    #: Auf- und Abschläge auf die Preise oder Kosten mit regionaler Eingrenzung
    tarif_auf_abschlaege: Optional[List[AufAbschlagRegional]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(AufAbschlagRegional),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    # todo: fix inconsistency: RegionalerAufAbschlag vs. AufAbschlagRegional
    # https://github.com/Hochfrequenz/BO4E-python/issues/345

    #: Preisgarantie für diesen Tarif
    preisgarantie: Optional[Preisgarantie] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.instance_of(Preisgarantie),
        ),
    )
    # todo: fix inconsistency with regionaltarif https://github.com/Hochfrequenz/BO4E-python/issues/346
    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Optional[Tarifeinschraenkung] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Tarifeinschraenkung))
    )


class TarifSchema(TarifinfoSchema):
    """
    Schema for de-/serialization of Tarif
    """

    class_name = Tarif  # type:ignore[assignment]

    # required attributes
    preisstand = fields.DateTime()
    berechnungsparameter = fields.Nested(TarifberechnungsparameterSchema)
    tarifpreise = fields.List(fields.Nested(TarifpreispositionProOrtSchema))

    # optional attributes
    tarif_auf_abschlaege = fields.List(
        fields.Nested(AufAbschlagRegionalSchema), allow_none=True, data_key="tarifAufAbschlaege"
    )
    preisgarantie = fields.Nested(PreisgarantieSchema, allow_none=True)
    tarifeinschraenkung = fields.Nested(TarifeinschraenkungSchema, allow_none=True)
