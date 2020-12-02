import attr
import jsons

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.adresse import Adresse
from bo4e.enum.anrede import Anrede
from bo4e.enum.kontaktart import Kontaktart
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.botyp import BoTyp


@attr.s(auto_attribs=True, kw_only=True)
class Geschaeftspartner(Geschaeftsobjekt, jsons.JsonSerializable):
    """
    Objekt zur Aufnahme der Information zu einem Geschaeftspartner
    """

    anrede: Anrede = attr.ib(default=None)
    name1: str
    name2: str = attr.ib(default=None)
    name3: str = attr.ib(default=None)
    gewerbekennzeichnung: bool
    hrnummer: str = attr.ib(default=None)
    amtsgericht: str = attr.ib(default=None)
    kontaktweg: Kontaktart = attr.ib(default=None)
    umsatzsteuerId: str = attr.ib(default=None)
    glaeubigerId: str = attr.ib(default=None)
    eMailAdresse: str = attr.ib(default=None)
    website: str = attr.ib(default=None)
    geschaeftspartnerrolle: Geschaeftspartnerrolle
    partneradresse: Adresse

    bo_typ: BoTyp = attr.ib(default=BoTyp.GESCHAEFTSPARTNER)
