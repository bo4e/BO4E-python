"""
Contains StandorteigenschaftenAllgemein class
and corresponding marshmallow schema for de-/serialization
"""


import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class StandorteigenschaftenAllgemein(COM):
    """
    Allgemeine Standorteigenschaften
    """

    # required attributes
    #: Die Postleitzahl des Standorts
    postleitzahl: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Die Ortsbezeichnung des Standorts
    ort: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Der Name des Kreises in dem der Standort liegt
    kreisname: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Der Name der Gemeinde des Standortes
    gemeindename: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Die standardisierte Kennziffer der Gemeinde
    gemeindekennziffer: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Anzahl der Einwohner in der Gemeinde
    gemeindeeinwohner: int = attr.ib(validator=attr.validators.instance_of(int))
    #: Das Bundesland zu dem der Standort gehört
    bundesland: str = attr.ib(validator=attr.validators.instance_of(str))


class StandorteigenschaftenAllgemeinSchema(COMSchema):
    """
    Schema for de-/serialization of StandorteigenschaftenAllgemein.
    """

    # required attributes
    postleitzahl = fields.Str()
    ort = fields.Str()
    kreisname = fields.Str()
    gemeindename = fields.Str()
    gemeindekennziffer = fields.Str()
    gemeindeeinwohner = fields.Int()
    bundesland = fields.Str()

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> StandorteigenschaftenAllgemein:
        """Deserialize JSON to StandorteigenschaftenAllgemein object"""
        return StandorteigenschaftenAllgemein(**data)
