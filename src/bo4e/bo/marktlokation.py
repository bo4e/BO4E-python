"""
Contains Marktlokation class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.com.geokoordinaten import Geokoordinaten, GeokoordinatenSchema
from bo4e.com.katasteradresse import Katasteradresse, KatasteradresseSchema
from bo4e.com.messlokationszuordnung import Messlokationszuordnung, MesslokationszuordnungSchema
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
@attr.s(auto_attribs=True, kw_only=True)
class Marktlokation(Geschaeftsobjekt):
    """
    Object containing information about a Marktlokation
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.MARKTLOKATION)
    #: Identifikationsnummer einer Marktlokation, an der Energie entweder verbraucht, oder erzeugt wird.
    marktlokations_id: str = attr.ib(validator=validate_marktlokations_id)
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
    verbrauchsart: Verbrauchsart = attr.ib(default=None)
    #: Gibt an, ob es sich um eine unterbrechbare Belieferung handelt
    unterbrechbar: bool = attr.ib(default=None)
    #: Codenummer des Netzbetreibers, an dessen Netz diese Marktlokation angeschlossen ist.
    netzbetreibercodenr: str = attr.ib(default=None)
    #: Typ des Netzgebietes, z.B. Verteilnetz
    gebietstyp: Gebiettyp = attr.ib(default=None)
    #: Die ID des Gebietes in der ene't-Datenbank
    netzgebietsnr: str = attr.ib(default=None)  # todo: rename to "id" (see 2021-12-15 update)
    #: Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist - im Falle eines Strom Netzes
    bilanzierungsgebiet: str = attr.ib(default=None)
    #: Codenummer des Grundversorgers, der für diese Marktlokation zuständig ist
    grundversorgercodenr: str = attr.ib(default=None)
    #: Die Gasqualität in diesem Netzgebiet. H-Gas oder L-Gas. Im Falle eines Gas-Netzes
    gasqualitaet: Gasqualitaet = attr.ib(default=None)
    #: Geschäftspartner, dem diese Marktlokation gehört
    endkunde: Geschaeftspartner = attr.ib(default=None)
    zugehoerige_messlokation: Messlokationszuordnung = attr.ib(default=None)  # todo: rename to plural
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
    lokationsadresse: Adresse = attr.ib(default=None)
    geoadresse: Geokoordinaten = attr.ib(default=None)
    """
    Alternativ zu einer postalischen Adresse kann hier ein Ort mittels Geokoordinaten angegeben werden
    (z.B. zur Identifikation von Sendemasten).
    """
    katasterinformation: Katasteradresse = attr.ib(default=None)
    """
    Alternativ zu einer postalischen Adresse und Geokoordinaten kann hier eine Ortsangabe mittels Gemarkung und
    Flurstück erfolgen.
    """

    # todo: add kundengruppe

    # pylint:disable=unused-argument
    @lokationsadresse.validator
    @geoadresse.validator
    @katasterinformation.validator
    def validate_address_info(self, address_attribute, value):
        """Checks that there is one and only one valid adress given."""
        all_address_attributes = [
            self.lokationsadresse,
            self.geoadresse,
            self.katasterinformation,
        ]
        amount_of_given_address_infos = len([i for i in all_address_attributes if i is not None])
        if amount_of_given_address_infos != 1:
            raise ValueError("No or more than one address information is given.")


class MarktlokationSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Marktlokation.
    Inherits from GeschaeftsobjektSchema.
    """

    # class_name is needed to use the correct schema for deserialisation.
    # see function `deserialize` in geschaeftsobjekt.py
    class_name = Marktlokation

    # required attributes
    marktlokations_id = fields.Str()
    sparte = EnumField(Sparte)
    energierichtung = EnumField(Energierichtung)
    bilanzierungsmethode = EnumField(Bilanzierungsmethode)
    netzebene = EnumField(Netzebene)

    # optional attributes
    verbrauchsart = EnumField(Verbrauchsart, load_default=None)
    unterbrechbar = fields.Bool(load_default=None)
    netzbetreibercodenr = fields.Str(load_default=None)
    gebietstyp = EnumField(Gebiettyp, load_default=None)
    netzgebietsnr = fields.Str(load_default=None)
    bilanzierungsgebiet = fields.Str(load_default=None)
    grundversorgercodenr = fields.Str(load_default=None)
    gasqualitaet = EnumField(Gasqualitaet, load_default=None)
    endkunde = fields.Nested(GeschaeftspartnerSchema, load_default=None)
    zugehoerige_messlokation = fields.List(fields.Nested(MesslokationszuordnungSchema), load_default=None)

    # only one of the following three optional attributes can be set
    lokationsadresse = fields.Nested(AdresseSchema, load_default=None)
    geoadresse = fields.Nested(GeokoordinatenSchema, load_default=None)
    katasterinformation = fields.Nested(KatasteradresseSchema, load_default=None)
