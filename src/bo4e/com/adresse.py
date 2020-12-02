import attr
import jsons

from bo4e.com.com import COM
from bo4e.enum.landescode import Landescode


@attr.s(auto_attribs=True, kw_only=True)
class Adresse(COM, jsons.JsonSerializable):
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
