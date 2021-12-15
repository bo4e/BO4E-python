"""
Contains RegionalePreisgarantie class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load

from bo4e.com.preisgarantie import Preisgarantie, PreisgarantieSchema
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit, RegionaleGueltigkeitSchema

# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class RegionalePreisgarantie(Preisgarantie):
    """
    Abbildung einer Preisgarantie mit regionaler Abgrenzung.
    """

    # required attributes
    #: Regionale Eingrenzung der Preisgarantie.
    regionale_gueltigkeit: RegionaleGueltigkeit = attr.ib(validator=attr.validators.instance_of(RegionaleGueltigkeit))


class RegionalePreisgarantieSchema(PreisgarantieSchema):
    """
    Schema for de-/serialization of RegionalePreisgarantie.
    """

    # required attributes
    regionale_gueltigkeit = fields.Nested(RegionaleGueltigkeitSchema)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> RegionalePreisgarantie:
        """Deserialize JSON to Energiemix object"""
        return RegionalePreisgarantie(**data)
