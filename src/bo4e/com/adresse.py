import attr

from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

from bo4e.cases import JavaScriptMixin
from bo4e.com.com import COM
from bo4e.enum.landescode import Landescode


def strasse_xor_postfach(instance, attribute, value):
    if (
        instance.strasse is None or instance.hausnummer is None
    ) and instance.postfach is None:
        raise ValueError("Either strasse and hausnummer or postfach are required.")
    elif (
        instance.strasse is not None or instance.hausnummer is not None
    ) and instance.postfach is not None:
        raise ValueError("Only strasse and hausnummer or postfach are required.")


@attr.s(auto_attribs=True, kw_only=True)
class Adresse(COM):
    """
    Enthält eine Adresse, die für die meisten Zwecke verwendbar ist.
    """

    # required attributes
    strasse: str
    hausnummer: str
    postleitzahl: str
    ort: str

    # optional attributes
    postfach: str = attr.ib(default=None)
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
