"""
Contains AufAbschlagProOrt class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List

import attrs
from marshmallow import fields

from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrt, AufAbschlagstaffelProOrtSchema
from bo4e.com.com import COM, COMSchema
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class AufAbschlagProOrt(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang
    mit örtlichen Gültigkeiten abgebildet werden.

    .. HINT::
        `AufAbschlagProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AufAbschlagProOrtSchema.json>`_

    """

    # required attributes
    #: Die Postleitzahl des Ortes für den der Aufschlag gilt.
    postleitzahl: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Der Ort für den der Aufschlag gilt.
    ort: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Die ene't-Netznummer des Netzes in dem der Aufschlag gilt.
    netznr: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung.
    staffeln: List[AufAbschlagstaffelProOrt] = attrs.field(
        validator=[attrs.validators.instance_of(List), check_list_length_at_least_one]
    )


class AufAbschlagProOrtSchema(COMSchema):
    """
    Schema for de-/serialization of AufAbschlagProOrt
    """

    class_name = AufAbschlagProOrt
    # required attributes
    postleitzahl = fields.Str()
    ort = fields.Str()
    netznr = fields.Str()
    staffeln = fields.List(fields.Nested(AufAbschlagstaffelProOrtSchema))
