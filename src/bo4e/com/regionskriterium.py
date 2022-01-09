"""
Contains Regionskriterium class and corresponding marshmallow schema for de-/serialization
"""


import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.regionskriteriumtyp import Regionskriteriumtyp


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Regionskriterium(COM):
    """
    Komponente zur Abbildung eines Regionskriteriums
    """

    # required attributes
    gueltigkeitstyp: Gueltigkeitstyp = attr.ib(
        validator=attr.validators.instance_of(Gueltigkeitstyp)
    )  #: Hier wird festgelegt, ob es sich um ein einschließendes oder ausschließendes Kriterium handelt.
    regionskriteriumtyp: Regionskriteriumtyp = attr.ib(
        validator=attr.validators.instance_of(Regionskriteriumtyp)
    )  #: Hier wird das Kriterium selbst angegeben, z.B. Bundesland.
    wert: str = attr.ib(validator=attr.validators.instance_of(str))
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
