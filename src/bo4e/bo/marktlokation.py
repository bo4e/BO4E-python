"""
Contains Marktlokation class
and corresponding marshmallow schema for de-/serialization
"""


from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.com.geokoordinaten import Geokoordinaten
from bo4e.com.katasteradresse import Katasteradresse
from bo4e.com.messlokationszuordnung import Messlokationszuordnung
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.gasqualitaet import Gasqualitaet
from bo4e.enum.gebiettyp import Gebiettyp
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte
from bo4e.enum.verbrauchsart import Verbrauchsart
from bo4e.validators import validate_marktlokations_id


# pylint: disable=too-many-instance-attributes, too-few-public-methods
from pydantic import validator, StrictBool, StrictStr


class Marktlokation(Geschaeftsobjekt):
    """
    Object containing information about a Marktlokation

    .. HINT::
        `Marktlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/MarktlokationSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.MARKTLOKATION
    #: Identifikationsnummer einer Marktlokation, an der Energie entweder verbraucht, oder erzeugt wird.
    marktlokations_id: str
    _marktlokations_id_check = validator("marktlokations_id", allow_reuse=True)(validate_marktlokations_id)
    #: Sparte der Marktlokation, z.B. Gas oder Strom
    sparte: Sparte
    #: Kennzeichnung, ob Energie eingespeist oder entnommen (ausgespeist) wird
    energierichtung: Energierichtung
    #: Die Bilanzierungsmethode, RLM oder SLP
    bilanzierungsmethode: Bilanzierungsmethode
    netzebene: Netzebene
    """
    Netzebene, in der der Bezug der Energie erfolgt.
    Bei Strom Spannungsebene der Lieferung, bei Gas Druckstufe.
    Beispiel Strom: Niederspannung Beispiel Gas: Niederdruck.
    """

    # optional attributes
    #: Verbrauchsart der Marktlokation.
    verbrauchsart: Verbrauchsart = None
    #: Gibt an, ob es sich um eine unterbrechbare Belieferung handelt
    unterbrechbar: bool = None
    #: Codenummer des Netzbetreibers, an dessen Netz diese Marktlokation angeschlossen ist.
    netzbetreibercodenr: str = None
    #: Typ des Netzgebietes, z.B. Verteilnetz
    gebietstyp: Gebiettyp = None
    #: Die ID des Gebietes in der ene't-Datenbank
    netzgebietsnr: str = None  # todo: rename to "id" (see 2021-12-15 update)
    #: Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist - im Falle eines Strom Netzes
    bilanzierungsgebiet: str = None
    #: Codenummer des Grundversorgers, der für diese Marktlokation zuständig ist
    grundversorgercodenr: str = None
    #: Die Gasqualität in diesem Netzgebiet. H-Gas oder L-Gas. Im Falle eines Gas-Netzes
    gasqualitaet: Gasqualitaet = None
    #: Geschäftspartner, dem diese Marktlokation gehört
    endkunde: Geschaeftspartner = None
    zugehoerige_messlokation: Messlokationszuordnung = None  # todo: rename to plural
    """
    Aufzählung der Messlokationen, die zu dieser Marktlokation gehören.
    Es können 3 verschiedene Konstrukte auftreten:

    Beziehung 1 : 0 : Hier handelt es sich um Pauschalanlagen ohne Messung. D.h. die Verbrauchsdaten sind direkt über
    die Marktlokation abgreifbar.
    Beziehung 1 : 1 : Das ist die Standard-Beziehung für die meisten Fälle. In diesem Fall gibt es zu einer
    Marktlokation genau eine Messlokation.
    Beziehung 1 : N : Hier liegt beispielsweise eine Untermessung vor. Der Verbrauch einer Marklokation berechnet sich
    hier aus mehreren Messungen.

    Es gibt praktisch auch noch die Beziehung N : 1, beispielsweise bei einer Zweirichtungsmessung bei der durch eine
    Messeinrichtung die Messung sowohl für die Einspreiseseite als auch für die Aussspeiseseite erfolgt.
    Da Abrechnung und Bilanzierung jedoch für beide Marktlokationen getrennt erfolgt, werden nie beide Marktlokationen
    gemeinsam betrachtet. Daher lässt sich dieses Konstrukt auf zwei 1:1-Beziehung zurückführen,
    wobei die Messlokation in beiden Fällen die gleiche ist.

    In den Zuordnungen sind ist die arithmetische Operation mit der der Verbrauch einer Messlokation zum Verbrauch einer
    Marktlokation beitrögt mit aufgeführt.
    Der Standard ist hier die Addition.
    """

    # only one of the following three optional attributes can be set
    #: Die Adresse, an der die Energie-Lieferung oder -Einspeisung erfolgt
    lokationsadresse: Adresse = None
    geoadresse: Geokoordinaten = None
    """
    Alternativ zu einer postalischen Adresse kann hier ein Ort mittels Geokoordinaten angegeben werden
    (z.B. zur Identifikation von Sendemasten).
    """
    katasterinformation: Katasteradresse = None
    """
    Alternativ zu einer postalischen Adresse und Geokoordinaten kann hier eine Ortsangabe mittels Gemarkung und
    Flurstück erfolgen.
    """

    # todo: add kundengruppe

    # pylint:disable=unused-argument
    @validator("katasterinformation", always=True)
    def validate_address_info(cls, katasterinformation, values):
        """Checks that there is one and only one valid adress given."""
        all_address_attributes = [
            values["lokationsadresse"],
            values["geoadresse"],
            katasterinformation,
        ]
        amount_of_given_address_infos = len([i for i in all_address_attributes if i is not None])
        if amount_of_given_address_infos != 1:
            raise ValueError("No or more than one address information is given.")
        else:
            return katasterinformation
