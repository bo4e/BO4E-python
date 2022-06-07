"""
Contains AufAbschlagstaffelProOrt class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class AufAbschlagstaffelProOrt(COM):
    """
    Gibt den Wert eines Auf- oder Abschlags und dessen Staffelgrenzen an

    .. HINT::
        `AufAbschlagstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AufAbschlagstaffelProOrtSchema.json>`_

    """

    # required attributes
    #: Der Wert für den Auf- oder Abschlag.
    wert: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    #: Unterer Wert, ab dem die Staffel gilt.
    staffelgrenze_von: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    #: Oberer Wert, bis zu dem die Staffel gilt.
    staffelgrenze_bis: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))


class AufAbschlagstaffelProOrtSchema(COMSchema):
    """
    Schema for de-/serialization of AufAbschlagstaffelProOrt
    """

    class_name = AufAbschlagstaffelProOrt
    # required attributes
    wert = fields.Decimal(as_string=True)
    staffelgrenze_von = fields.Decimal(as_string=True, data_key="staffelgrenzeVon")
    staffelgrenze_bis = fields.Decimal(as_string=True, data_key="staffelgrenzeBis")
