"""
Contains AufAbschlagstaffelProOrt class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class AufAbschlagstaffelProOrt(COM):
    """
    Gibt den Wert eines Auf- oder Abschlags und dessen Staffelgrenzen an.
    """

    # required attributes
    #: Der Wert für den Auf- oder Abschlag.
    wert: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    #: Unterer Wert, ab dem die Staffel gilt.
    staffelgrenze_von: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    #: Oberer Wert, bis zu dem die Staffel gilt.
    staffelgrenze_bis: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))


class AufAbschlagstaffelProOrtSchema(COMSchema):
    """
    Schema for de-/serialization of AufAbschlagstaffelProOrt.
    """

    # required attributes
    wert = fields.Decimal(as_string=True)
    staffelgrenze_von = fields.Decimal(as_string=True)
    staffelgrenze_bis = fields.Decimal(as_string=True)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> AufAbschlagstaffelProOrt:
        """Deserialize JSON to AufAbschlagstaffelProOrt object"""
        return AufAbschlagstaffelProOrt(**data)
