"""
Contains Tarifpreisposition class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.preisstaffel import Preisstaffel, PreisstaffelSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Tarifpreisposition(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden.
    """

    # required attributes
    # Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Preistyp = attr.ib(validator=attr.validators.instance_of(Preistyp))
    # Einheit des Preises (z.B. EURO)
    einheit: Waehrungseinheit = attr.ib(validator=attr.validators.instance_of(Waehrungseinheit))
    # Größe, auf die sich die Einheit bezieht, beispielsweise kWh, Jahr
    bezugseinheit: Mengeneinheit = attr.ib(validator=attr.validators.instance_of(Mengeneinheit))
    # Hier sind die Staffeln mit ihren Preisenangaben definiert
    preisstaffeln: List[Preisstaffel] = attr.ib(
        validator=[
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Preisstaffel),
                iterable_validator=attr.validators.instance_of(list),
            ),
            check_list_length_at_least_one,
        ]
    )

    # optional attributes
    # Gibt an, nach welcher Menge die vorgenannte Einschränkung erfolgt (z.B. Jahresstromverbrauch in kWh)
    mengeneinheitstaffel: Optional[Mengeneinheit] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Mengeneinheit))
    )


class TarifpreispositionSchema(COMSchema):
    """
    Schema for de-/serialization of Tarifpreisposition.
    """

    class_name = Tarifpreisposition
    # required attributes
    preistyp = EnumField(Preistyp)
    einheit = EnumField(Waehrungseinheit)
    bezugseinheit = EnumField(Mengeneinheit)
    preisstaffeln = fields.List(fields.Nested(PreisstaffelSchema))

    # optional attributes
    mengeneinheitstaffel = EnumField(Mengeneinheit, load_default=None)
