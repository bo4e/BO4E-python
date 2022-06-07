"""
Contains RegionalePreisgarantie class
and corresponding marshmallow schema for de-/serialization
"""

import attrs
from marshmallow import fields

from bo4e.com.preisgarantie import Preisgarantie, PreisgarantieSchema
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit, RegionaleGueltigkeitSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class RegionalePreisgarantie(Preisgarantie):
    """
    Abbildung einer Preisgarantie mit regionaler Abgrenzung

    .. HINT::
        `RegionalePreisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionalePreisgarantieSchema.json>`_

    """

    # required attributes
    #: Regionale Eingrenzung der Preisgarantie.
    regionale_gueltigkeit: RegionaleGueltigkeit = attrs.field(
        validator=attrs.validators.instance_of(RegionaleGueltigkeit)
    )


class RegionalePreisgarantieSchema(PreisgarantieSchema):
    """
    Schema for de-/serialization of RegionalePreisgarantie.
    """

    class_name = RegionalePreisgarantie  # type:ignore[assignment]
    # required attributes
    regionale_gueltigkeit = fields.Nested(RegionaleGueltigkeitSchema, data_key="regionaleGueltigkeit")
