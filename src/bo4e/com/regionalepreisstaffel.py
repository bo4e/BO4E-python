"""
Contains RegionalePreisstaffel class and corresponding marshmallow schema for de-/serialization
"""

import attrs
from marshmallow import fields

from bo4e.com.preisstaffel import Preisstaffel, PreisstaffelSchema
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit, RegionaleGueltigkeitSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class RegionalePreisstaffel(Preisstaffel):
    """
    Abbildung einer Preisstaffel mit regionaler Abgrenzung

    .. HINT::
        `RegionalePreisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionalePreisstaffelSchema.json>`_

    """

    # required attributes
    #: Regionale Eingrenzung der Preisstaffel
    regionale_gueltigkeit: RegionaleGueltigkeit = attrs.field(
        validator=attrs.validators.instance_of(RegionaleGueltigkeit)
    )


class RegionalePreisstaffelSchema(PreisstaffelSchema):
    """
    Schema for de-/serialization of RegionalePreisgarantie.
    """

    class_name = RegionalePreisstaffel  # type:ignore[assignment]
    # required attributes
    regionale_gueltigkeit = fields.Nested(RegionaleGueltigkeitSchema, data_key="regionaleGueltigkeit")
