import attr

from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

from bo4e.cases import JavaScriptMixin
from bo4e.com.com import COM
from bo4e.enum.landescode import Landescode


def strasse_xor_postfach(instance, attribute, value):
    if instance.strasse or instance.hausnummer:
        if instance.postfach:
            raise ValueError("Enter either strasse and hausnummer OR postfach.")
        elif not instance.strasse:
            raise ValueError("Missing strasse to hausnummer.")
        elif not instance.hausnummer:
            raise ValueError("Missing hausnummer to strasse.")


@attr.s(auto_attribs=True, kw_only=True)
class Adresse(COM):
    """
    Enthält eine Adresse, die für die meisten Zwecke verwendbar ist.
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
    landescode: Landescode = attr.ib(default=Landescode.DE)


class AdresseSchema(Schema, JavaScriptMixin):
    # required attributes
    postleitzahl = fields.Str()
    ort = fields.Str()

    # optional attributes
    strasse = fields.Str(missing=None)
    hausnummer = fields.Str(missing=None)
    postfach = fields.Str(missing=None)
    adresszusatz = fields.Str(missing=None)
    co_ergaenzung = fields.Str(missing=None)
    landescode = EnumField(Landescode)

    @post_load
    def deserialise(self, data, **kwargs) -> Adresse:
        return Adresse(**data)
