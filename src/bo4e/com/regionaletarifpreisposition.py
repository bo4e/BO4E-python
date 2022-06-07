"""
Contains RegionaleTarifpreisposition class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.regionalepreisstaffel import RegionalePreisstaffel, RegionalePreisstaffelSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class RegionaleTarifpreisposition(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen im Zusammenhang mit regionalen Gültigkeiten abgebildet
    werden.

    .. HINT::
        `RegionaleTarifpreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionaleTarifpreispositionSchema.json>`_

    """

    # required attributes
    #: Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Preistyp = attrs.field(validator=attrs.validators.instance_of(Preistyp))
    #: Einheit des Preises (z.B. EURO)
    einheit: Waehrungseinheit = attrs.field(validator=attrs.validators.instance_of(Waehrungseinheit))
    #: Größe, auf die sich die Einheit bezieht, beispielsweise kWh, Jahr
    bezugseinheit: Mengeneinheit = attrs.field(validator=attrs.validators.instance_of(Mengeneinheit))
    #: Hier sind die Staffeln mit ihren Preisangaben und regionalen Gültigkeiten definiert
    preisstaffeln: List[RegionalePreisstaffel] = attrs.field(
        validator=[
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(RegionalePreisstaffel),
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


class RegionaleTarifpreispositionSchema(COMSchema):
    """
    Schema for de-/serialization of RegionaleTarifpreisposition
    """

    class_name = RegionaleTarifpreisposition
    # required attributes
    preistyp = EnumField(Preistyp)
    einheit = EnumField(Waehrungseinheit)
    bezugseinheit = EnumField(Mengeneinheit)
    preisstaffeln = fields.List(fields.Nested(RegionalePreisstaffelSchema))

    # optional attributes
    mengeneinheitstaffel = EnumField(Mengeneinheit, load_default=None)
