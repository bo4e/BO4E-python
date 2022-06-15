"""
Contains Tarifpreisposition class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.preisstaffel import Preisstaffel, PreisstaffelSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Tarifpreisposition(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden.

    .. HINT::
        `Tarifpreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TarifpreispositionSchema.json>`_

    """

    # required attributes
    #: Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Preistyp = attrs.field(validator=attrs.validators.instance_of(Preistyp))
    #: Einheit des Preises (z.B. EURO)
    einheit: Waehrungseinheit = attrs.field(validator=attrs.validators.instance_of(Waehrungseinheit))
    #: Größe, auf die sich die Einheit bezieht, beispielsweise kWh, Jahr
    bezugseinheit: Mengeneinheit = attrs.field(validator=attrs.validators.instance_of(Mengeneinheit))
    #: Hier sind die Staffeln mit ihren Preisenangaben definiert
    preisstaffeln: List[Preisstaffel] = attrs.field(
        validator=[
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Preisstaffel),
                iterable_validator=attrs.validators.instance_of(list),
            ),
            check_list_length_at_least_one,
        ]
    )

    # optional attributes
    #: Gibt an, nach welcher Menge die vorgenannte Einschränkung erfolgt (z.B. Jahresstromverbrauch in kWh)
    mengeneinheitstaffel: Optional[Mengeneinheit] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Mengeneinheit))
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
