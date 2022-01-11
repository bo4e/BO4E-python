"""
Contains RegionaleTarifpreisposition class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.regionalepreisstaffel import RegionalePreisstaffel, RegionalePreisstaffelSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class RegionaleTarifpreisPosition(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen im Zusammenhang mit regionalen Gültigkeiten abgebildet
    werden.
    """

    # required attributes
    #: Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Preistyp = attr.ib(validator=attr.validators.instance_of(Preistyp))
    #: Einheit des Preises (z.B. EURO)
    einheit: Waehrungseinheit = attr.ib(validator=attr.validators.instance_of(Waehrungseinheit))
    #: Größe, auf die sich die Einheit bezieht, beispielsweise kWh, Jahr
    bezugseinheit: Mengeneinheit = attr.ib(validator=attr.validators.instance_of(Mengeneinheit))
    #: Hier sind die Staffeln mit ihren Preisangaben und regionalen Gültigkeiten definiert
    preisstaffeln: List[RegionalePreisstaffel] = attr.ib(
        validator=[
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(RegionalePreisstaffel),
                iterable_validator=attr.validators.instance_of(list),
            ),
            check_list_length_at_least_one,
        ]
    )

    # optional attributes
    #: Gibt an, nach welcher Menge die vorgenannte Einschränkung erfolgt (z.B. Jahresstromverbrauch in kWh)
    mengeneinheitstaffel: Optional[List[Mengeneinheit]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Mengeneinheit),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )


class RegionaleTarifpreisPositionSchema(COMSchema):
    """
    Schema for de-/serialization of RegionaleTarifpreisPosition
    """

    class_name = RegionaleTarifpreisPosition
    # required attributes
    preistyp = EnumField(Preistyp)
    einheit = EnumField(Waehrungseinheit)
    bezugseinheit = EnumField(Mengeneinheit)
    preisstaffeln = fields.List(fields.Nested(RegionalePreisstaffelSchema))

    # optional attributes
    mengeneinheitstaffel = fields.List(EnumField(Mengeneinheit), allow_none=True)
