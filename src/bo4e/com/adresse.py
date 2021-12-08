"""
Contains Adresse class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.landescode import Landescode


# pylint: disable=unused-argument
def strasse_xor_postfach(instance, attribute, value):
    """
    An address is valid if it contains a postfach XOR (a strasse AND hausnummer).
    This functions checks for these conditions of a valid address.
    """
    if instance.strasse or instance.hausnummer:
        if instance.postfach:
            raise ValueError("Enter either strasse and hausnummer OR postfach.")
        if not instance.strasse:
            raise ValueError("Missing strasse to hausnummer.")
        if not instance.hausnummer:
            raise ValueError("Missing hausnummer to strasse.")


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Adresse(COM):
    """
    Contains an address that can be used for most purposes.
    """

    # required attributes
    postleitzahl: str = attr.ib(validator=attr.validators.instance_of(str))
    ort: str = attr.ib(validator=attr.validators.instance_of(str))

    # optional attributes
    strasse: str = attr.ib(default=None, validator=strasse_xor_postfach)
    hausnummer: str = attr.ib(default=None, validator=strasse_xor_postfach)
    postfach: str = attr.ib(default=None, validator=strasse_xor_postfach)
    adresszusatz: str = attr.ib(default=None)
    co_ergaenzung: str = attr.ib(default=None)
    landescode: Landescode = attr.ib(default=Landescode.DE)  # type:ignore


class AdresseSchema(COMSchema):
    """
    Schema for de-/serialization of Adresse.
    """

    # required attributes
    postleitzahl = fields.Str()
    ort = fields.Str()

    # optional attributes
    strasse = fields.Str(load_default=None)
    hausnummer = fields.Str(load_default=None)
    postfach = fields.Str(load_default=None)
    adresszusatz = fields.Str(load_default=None)
    co_ergaenzung = fields.Str(load_default=None)
    landescode = EnumField(Landescode)

    # pylint: disable=no-self-use
    @post_load
    def deserialize(self, data, **kwargs) -> Adresse:
        """Deserialize JSON to Adresse object"""
        return Adresse(**data)
