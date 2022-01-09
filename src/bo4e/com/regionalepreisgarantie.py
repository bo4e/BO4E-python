"""
Contains RegionalePreisgarantie class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields

from bo4e.com.preisgarantie import Preisgarantie, PreisgarantieSchema
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit, RegionaleGueltigkeitSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class RegionalePreisgarantie(Preisgarantie):
    """
    Abbildung einer Preisgarantie mit regionaler Abgrenzung
    """

    # required attributes
    #: Regionale Eingrenzung der Preisgarantie.
    regionale_gueltigkeit: RegionaleGueltigkeit = attr.ib(validator=attr.validators.instance_of(RegionaleGueltigkeit))


class RegionalePreisgarantieSchema(PreisgarantieSchema):
    """
    Schema for de-/serialization of RegionalePreisgarantie.
    """

    class_name = RegionalePreisgarantie  # type:ignore[assignment]
    # required attributes
    regionale_gueltigkeit = fields.Nested(RegionaleGueltigkeitSchema)
