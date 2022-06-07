"""
Contains Tarifpreis class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.preis import Preis, PreisSchema
from bo4e.enum.preistyp import Preistyp


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Tarifpreis(Preis):
    """
    Abbildung eines Tarifpreises mit Preistyp und Beschreibung abgeleitet von COM Preis.

    .. HINT::
        `Tarifpreis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TarifpreisSchema.json>`_

    """

    # required attributes
    #:  Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Preistyp = attrs.field(validator=attrs.validators.in_(Preistyp))

    # optional attributes
    #:  Beschreibung des Preises. Hier können z.B. Preisdetails angegeben sein, beispielsweise "Drehstromzähler".
    beschreibung: Optional[str] = attrs.field(default=None)


class TarifpreisSchema(PreisSchema):
    """
    Schema for de-/serialization of Tarifpreis
    """

    class_name = Tarifpreis  # type:ignore[assignment]
    # required attributes
    preistyp = EnumField(Preistyp)

    # optional attributes
    beschreibung = fields.Str(load_default=None)
