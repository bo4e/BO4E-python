"""
Contains Tarifpreis class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.preis import Preis, PreisSchema
from bo4e.enum.preistyp import Preistyp


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Tarifpreis(Preis):
    """
    Abbildung eines Tarifpreises mit Preistyp und Beschreibung abgeleitet von COM Preis.
    """

    # required attributes
    #:  Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Preistyp = attr.ib(validator=attr.validators.in_(Preistyp))

    # optional attributes
    #:  Beschreibung des Preises. Hier können z.B. Preisdetails angegeben sein, beispielsweise "Drehstromzähler".
    beschreibung: Optional[str] = attr.ib(default=None)


class TarifpreisSchema(PreisSchema):
    """
    Schema for de-/serialization of Tarifpreis.
    """

    # required attributes
    preistyp = EnumField(Preistyp)

    # optional attributes
    beschreibung = fields.Str(load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Tarifpreis:
        """Deserialize JSON to Tarifpreis object"""
        return Tarifpreis(**data)
