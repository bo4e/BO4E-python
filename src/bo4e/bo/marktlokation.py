import attr
import jsons

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.com.geokoordinaten import Geokoordinaten
from bo4e.com.katasteradresse import Katasteradresse
from bo4e.enum.sparte import Sparte
from bo4e.enum.botyp import BoTyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.verbrauchsart import Verbrauchsart
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.gebietstyp import Gebietstyp
from bo4e.enum.gasqualitaet import Gasqualitaet


@attr.s(auto_attribs=True, kw_only=True, frozen=True)
class Marktlokation(Geschaeftsobjekt, jsons.JsonSerializable):
    """
    Objekt zur Aufnahme der Informationen zu einer Marktlokation
    """

    marktlokations_id: str
    sparte: Sparte
    energierichtung: Energierichtung
    bilanzierungsmethode: Bilanzierungsmethode
    verbrauchsart: Verbrauchsart = attr.ib(default=None)
    unterbrechbar: bool = attr.ib(default=None)
    netzebene: Netzebene
    netzbetreibercodenr: str = attr.ib(default=None)
    gebietstyp: Gebietstyp = attr.ib(default=None)
    netzgebietsnr: str = attr.ib(default=None)
    bilanzierungsgebiet: str = attr.ib(default=None)
    grundversorgercodenr: str = attr.ib(default=None)
    gasqualitaet: Gasqualitaet = attr.ib(default=None)
    endkunde: Geschaeftspartner = attr.ib(default=None)
    zugehoerige_messlokation: str = attr.ib(default=None)

    lokationsadresse: Adresse = attr.ib(default=None)
    geoadresse: Geokoordinaten = attr.ib(default=None)
    katasterinformation: Katasteradresse = attr.ib(default=None)

    bo_typ: BoTyp = attr.ib(default=BoTyp.MARKTLOKATION)

    @lokationsadresse.validator
    @geoadresse.validator
    @katasterinformation.validator
    def validate_address_info(self, address_attribute, value):
        all_address_attributes = [
            self.lokationsadresse,
            self.geoadresse,
            self.katasterinformation,
        ]
        amount_of_given_address_infos = len(
            [i for i in all_address_attributes if i is not None]
        )
        if amount_of_given_address_infos != 1:
            raise ValueError("No or more than one address information is given.")
