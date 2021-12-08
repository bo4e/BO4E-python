"""
Contains Regionskriterium class and corresponding marshmallow schema for de-/serialization
"""


# pylint: disable=too-few-public-methods
import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.regionskriteriumtyp import Regionskriteriumtyp


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

    # required attributes
    gueltigkeitstyp = EnumField(Gueltigkeitstyp)
    regionskriteriumtyp = EnumField(Regionskriteriumtyp)
    wert = fields.String()

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Regionskriterium:
        """Deserialize JSON to Regionskriterium object"""
        return Regionskriterium(**data)
