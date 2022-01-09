"""
Contains RegionalePreisstaffel class and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields

from bo4e.com.preisstaffel import Preisstaffel, PreisstaffelSchema
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit, RegionaleGueltigkeitSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class RegionalePreisstaffel(Preisstaffel):
    """
    Abbildung einer Preisstaffel mit regionaler Abgrenzung
    """

    # required attributes
    #: Regionale Eingrenzung der Preisstaffel
    regionale_gueltigkeit: RegionaleGueltigkeit = attr.ib(validator=attr.validators.instance_of(RegionaleGueltigkeit))


class RegionalePreisstaffelSchema(PreisstaffelSchema):
    """
    Schema for de-/serialization of RegionalePreisgarantie.
    """

    class_name = RegionalePreisstaffel  # type:ignore[assignment]
    # required attributes
    regionale_gueltigkeit = fields.Nested(RegionaleGueltigkeitSchema)
