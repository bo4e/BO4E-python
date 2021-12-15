"""
Contains AufAbschlagProOrt class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List

import attr
from marshmallow import fields, post_load

from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrt, AufAbschlagstaffelProOrtSchema
from bo4e.com.com import COM, COMSchema
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class AufAbschlagProOrt(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang
    mit örtlichen Gültigkeiten abgebildet werden.
    """

    # required attributes
    #: Die Postleitzahl des Ortes für den der Aufschlag gilt.
    postleitzahl: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Der Ort für den der Aufschlag gilt.
    ort: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Die ene't-Netznummer des Netzes in dem der Aufschlag gilt.
    netznr: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung.
    staffeln: List[AufAbschlagstaffelProOrt] = attr.ib(
        validator=[attr.validators.instance_of(List), check_list_length_at_least_one]
    )


class AufAbschlagProOrtSchema(COMSchema):
    """
    Schema for de-/serialization of AufAbschlagProOrt.
    """

    # required attributes
    postleitzahl = fields.Str()
    ort = fields.Str()
    netznr = fields.Str()
    staffeln = fields.List(fields.Nested(AufAbschlagstaffelProOrtSchema))

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> AufAbschlagProOrt:
        """Deserialize JSON to AufAbschlagstaffelProOrt object"""
        return AufAbschlagProOrt(**data)
