import attr
import jsons

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
class Adresse(COM, jsons.JsonSerializable):
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
