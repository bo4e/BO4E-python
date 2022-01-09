"""
Contains Tarifeinschraenkung and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.geraet import Geraet, GeraetSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.enum.voraussetzungen import Voraussetzungen


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Tarifeinschraenkung(COM):
    """
    Mit dieser Komponente werden Einschränkungen für die Anwendung von Tarifen modelliert.
    """

    # optional attributes
    #: Weitere Produkte, die gemeinsam mit diesem Tarif bestellt werden können
    zusatzprodukte: Optional[List[str]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(str),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    #: Voraussetzungen, die erfüllt sein müssen, damit dieser Tarif zur Anwendung kommen kann
    voraussetzungen: Optional[List[Voraussetzungen]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Voraussetzungen),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    einschraenkungzaehler: Optional[List[Geraet]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Geraet),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    """ Liste der Zähler/Geräte, die erforderlich sind, damit dieser Tarif zur Anwendung gelangen kann.
    (Falls keine Zähler angegeben sind, ist der Tarif nicht an das Vorhandensein bestimmter Zähler gebunden.) """
    einschraenkungleistung: Optional[List[Menge]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Menge),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    """ Die vereinbarte Leistung, die (näherungsweise) abgenommen wird.
    Insbesondere Gastarife können daran gebunden sein, dass die Leistung einer vereinbarten Höhe entspricht. """


class TarifeinschraenkungSchema(COMSchema):
    """
    Schema for de-/serialization of Tarifeinschraenkung
    """

    class_name = Tarifeinschraenkung
    # optional attributes
    zusatzprodukte = fields.List(fields.String, load_default=None, many=True)
    voraussetzungen = fields.List(EnumField(Voraussetzungen), allow_none=True, many=True)
    einschraenkungzaehler = fields.List(fields.Nested(GeraetSchema), load_default=None)
    einschraenkungleistung = fields.List(fields.Nested(MengeSchema), load_default=None)
