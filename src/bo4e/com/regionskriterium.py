"""
Contains Regionskriterium class and corresponding marshmallow schema for de-/serialization
"""


import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.regionskriteriumtyp import Regionskriteriumtyp


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Regionskriterium(COM):
    """
    Komponente zur Abbildung eines Regionskriteriums

    .. HINT::
        `Regionskriterium JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionskriteriumSchema.json>`_

    """

    # required attributes
    gueltigkeitstyp: Gueltigkeitstyp = attrs.field(
        validator=attrs.validators.instance_of(Gueltigkeitstyp)
    )  #: Hier wird festgelegt, ob es sich um ein einschließendes oder ausschließendes Kriterium handelt.
    regionskriteriumtyp: Regionskriteriumtyp = attrs.field(
        validator=attrs.validators.instance_of(Regionskriteriumtyp)
    )  #: Hier wird das Kriterium selbst angegeben, z.B. Bundesland.
    wert: str = attrs.field(validator=attrs.validators.instance_of(str))
    """
    Der Wert, den das Kriterium annehmen kann, z.B. NRW.
    Im Falle des Regionskriteriumstyp BUNDESWEIT spielt dieser Wert keine Rolle.
    """


class RegionskriteriumSchema(COMSchema):
    """
    Schema for de-/serialization of Regionskriterium.
    """

    class_name = Regionskriterium
    # required attributes
    gueltigkeitstyp = EnumField(Gueltigkeitstyp)
    regionskriteriumtyp = EnumField(Regionskriteriumtyp)
    wert = fields.String()
