"""
Contains Tarifpreisblatt class and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import List, Optional

import attr
from marshmallow import fields

from bo4e.bo.tarifinfo import Tarifinfo, TarifinfoSchema
from bo4e.com.aufabschlag import AufAbschlag, AufAbschlagSchema
from bo4e.com.preisgarantie import Preisgarantie, PreisgarantieSchema
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter, TarifberechnungsparameterSchema
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung, TarifeinschraenkungSchema
from bo4e.com.tarifpreisposition import Tarifpreisposition, TarifpreispositionSchema
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Tarifpreisblatt(Tarifinfo):
    """
    Tarifinformation mit Preisen, Aufschlägen und Berechnungssystematik

    .. HINT::
        `Tarifpreisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/master/json_schemas/bo/TarifpreisblattSchema.json>`_

    """

    bo_typ: BoTyp = attr.ib(default=BoTyp.TARIFPREISBLATT)
    # required attributes (additional to those of Tarifinfo)
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: datetime = attr.ib(validator=attr.validators.instance_of(datetime))
    #: Die festgelegten Preise, z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: List[Tarifpreisposition] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Tarifpreisposition),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Tarifberechnungsparameter = attr.ib(
        validator=attr.validators.instance_of(Tarifberechnungsparameter)
    )

    # optional attributes
    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Optional[Tarifeinschraenkung] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Tarifeinschraenkung))
    )
    #: Festlegung von Garantien für bestimmte Preisanteile
    preisgarantie: Optional[Preisgarantie] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Preisgarantie))
    )
    #: Auf- und Abschläge auf die Preise oder Kosten
    tarif_auf_abschlaege: Optional[List[AufAbschlag]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(AufAbschlag),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )


class TarifpreisblattSchema(TarifinfoSchema):
    """
    Schema for de-/serialization of Tarifpreisblatt
    """

    class_name = Tarifpreisblatt  # type:ignore[assignment]
    # required attributes
    preisstand = fields.DateTime()
    berechnungsparameter = fields.Nested(TarifberechnungsparameterSchema)
    tarifpreise = fields.List(fields.Nested(TarifpreispositionSchema))
    # optional attributes
    tarif_auf_abschlaege = fields.List(fields.Nested(AufAbschlagSchema))
    preisgarantie = fields.Nested(PreisgarantieSchema)
    tarifeinschraenkung = fields.Nested(TarifeinschraenkungSchema)
