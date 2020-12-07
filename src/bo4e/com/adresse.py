import attr
import jsons

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
class Adresse(COM, jsons.JsonSerializable):
    """
    Enthält eine Adresse, die für die meisten Zwecke verwendbar ist.
    """

    # required attributes
    strasse: str = attr.ib(default=None, validator=strasse_xor_postfach)
    hausnummer: str = attr.ib(default=None, validator=strasse_xor_postfach)
    postfach: str = attr.ib(default=None, validator=strasse_xor_postfach)
    postleitzahl: str = attr.ib(validator=attr.validators.instance_of(str))
    ort: str = attr.ib(validator=attr.validators.instance_of(str))

    # optional attributes
    adresszusatz: str = attr.ib(default=None)
    co_ergaenzung: str = attr.ib(default=None)
    landescode: Landescode = attr.ib(default=Landescode.DE)
