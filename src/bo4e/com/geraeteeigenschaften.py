"""
Contains Geraeteeigenschaften and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

import attrs
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.geraetemerkmal import Geraetemerkmal
from bo4e.enum.geraetetyp import Geraetetyp


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Geraeteeigenschaften(COM):
    """
    Mit dieser Komponente werden die Eigenschaften eines Gerätes in Bezug auf den Typ und weitere Merkmale modelliert

    .. HINT::
        `Geraeteeigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/GeraeteeigenschaftenSchema.json>`_

    """

    # required attributes
    #: Der Typ eines Gerätes, beispielsweise Drehstromzähler
    geraetetyp: Geraetetyp = attrs.field(validator=attrs.validators.instance_of(Geraetetyp))

    # optional attributes
    #: Weitere Merkmale des Geräts, zum Beispiel Mehrtarif, Eintarif etc..
    geraetemerkmal: Optional[Geraetemerkmal] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Geraetemerkmal))
    )


class GeraeteeigenschaftenSchema(COMSchema):
    """
    Schema for de-/serialization of Geraeteeigenschaften
    """

    class_name = Geraeteeigenschaften
    # required attributes
    geraetetyp = EnumField(Geraetetyp)

    # optional attributes
    geraetemerkmal = EnumField(Geraetemerkmal, allow_none=True)
