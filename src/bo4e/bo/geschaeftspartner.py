import attr
import jsons

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.adresse import Adresse
from bo4e.enum.anrede import Anrede
from bo4e.enum.kontaktart import Kontaktart
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.botyp import BoTyp


@attr.s(auto_attribs=True, kw_only=True, frozen=True)
class Geschaeftspartner(Geschaeftsobjekt, jsons.JsonSerializable):
    """
    Objekt zur Aufnahme der Information zu einem Geschaeftspartner
    """

    bo_typ: BoTyp = attr.ib(default=BoTyp.GESCHAEFTSPARTNER)

    anrede: Anrede
    name1: str
    name2: str
    name3: str
    gewerbekennzeichnung: bool
    hrnummer: str
    amtsgericht: str
    kontaktweg: Kontaktart
    umsatzsteuerId: str
    glaeubigerId: str
    eMailAdresse: str
    website: str
    geschaeftspartnerrolle: Geschaeftspartnerrolle
    partneradresse: Adresse
