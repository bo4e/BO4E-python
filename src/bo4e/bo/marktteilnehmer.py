import attr
import jsons

from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.enum.botyp import BoTyp
from bo4e.enum.marktrolle import Marktrolle
from bo4e.enum.rollencodetyp import Rollencodetyp


@attr.s(auto_attribs=True, kw_only=True, frozen=True)
class Marktteilehmer(Geschaeftspartner, jsons.JsonSerializable):
    """
    Objekt zur Aufnahme der Information zu einem Marktteilnehmer
    """

    # required attributes
    marktrolle: Marktrolle
    rollencodenummer: str
    rollencodetyp: Rollencodetyp

    # optional attributes
    makoadresse: str = attr.ib(default=None)

    # required attributes with default value
    bo_typ: BoTyp = attr.ib(default=BoTyp.MARKTTEILNEHMER)
