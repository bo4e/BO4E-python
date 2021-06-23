"""
Contains Messlokation class
and corresponding marshmallow schema for de-/serialization
"""
import re
from typing import List

import attr
from marshmallow import fields
from marshmallow_enum import EnumField
from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.com.geokoordinaten import Geokoordinaten, GeokoordinatenSchema
from bo4e.com.katasteradresse import Katasteradresse, KatasteradresseSchema
from bo4e.com.hardware import Hardware, HardwareSchema
from bo4e.com.dienstleistung import Dienstleistung, DienstleistungSchema
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte


_malo_id_pattern = re.compile(r"^[1-9][\d]{10}$")


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Messlokation(Geschaeftsobjekt):
    """
    Object containing information about a Messlokation
    """

    # pylint: disable=unused-argument, no-self-use
    def _validate_marktlokations_id(self, marktlokations_id_attribute, value):
        if not value:
            raise ValueError("The marktlokations_id must not be empty.")
        if not _malo_id_pattern.match(value):
            raise ValueError(f"The marktlokations_id '{value}' does not match {_malo_id_pattern.pattern}")
        expected_checksum = Messlokation._get_checksum(value)
        actual_checksum = value[10:11]
        if expected_checksum != actual_checksum:
            # pylint: disable=line-too-long
            raise ValueError(
                f"The marktlokations_id '{value}' has checksum '{actual_checksum}' but '{expected_checksum}' was expected."
            )

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.MARKTLOKATION)
    messlokations_id: str = attr.ib(validator=_validate_marktlokations_id)
    sparte: Sparte
    netzebene: Netzebene
    energierichtung: Energierichtung
    bilanzierungsmethode: Bilanzierungsmethode

    # optional attributes
    messgebietnr: str = attr.ib(default=None)
    grundzustaendiger_msb_codenr: str = attr.ib(default=None)
    grundzustaendiger_msbim_codenr: str = attr.ib(default=None)
    grundzustaendiger_mdl_codenr: str = attr.ib(default=None)
    geraete: List[Hardware] = attr.ib(default=None)
    messdienstleistung: List[Dienstleistung] = attr.ib(default=None)

    # only one of the following three optional attributes can be set
    messadresse: Adresse = attr.ib(default=None)
    geoadresse: Geokoordinaten = attr.ib(default=None)
    katasterinformation: Katasteradresse = attr.ib(default=None)

    @messadresse.validator
    @geoadresse.validator
    @katasterinformation.validator
    def validate_address_info(self, address_attribute, value):
        """Checks that there is one and only one valid adress given."""
        all_address_attributes = [
            self.messadresse,
            self.geoadresse,
            self.katasterinformation,
        ]
        amount_of_given_address_infos = len([i for i in all_address_attributes if i is not None])
        if amount_of_given_address_infos != 1:
            raise ValueError("No or more than one address information is given.")

    @staticmethod
    def _get_checksum(malo_id: str) -> str:
        """
        Get the checksum of a marktlokations id.
        a) Quersumme aller Ziffern in ungerader Position
        b) Quersumme aller Ziffern auf gerader Position multipliziert mit 2
        c) Summe von a) und b) d) Differenz von c) zum nächsten Vielfachen von 10 (ergibt sich hier 10, wird die
           Prüfziffer 0 genommen
        https://bdew-codes.de/Content/Files/MaLo/2017-04-28-BDEW-Anwendungshilfe-MaLo-ID_Version1.0_FINAL.PDF
        :param self:
        :return: the checksum as string
        """
        odd_checksum: int = 0
        even_checksum: int = 0
        # start counting at 1 to be consistent with the above description
        # of "even" and "odd" but stop at tenth digit.
        for i in range(1, 11):
            digit = malo_id[i - 1 : i]
            if i % 2 - 1 == 0:
                odd_checksum += int(digit)
            else:
                even_checksum += 2 * int(digit)
        result: int = (10 - ((even_checksum + odd_checksum) % 10)) % 10
        return str(result)


class MesslokationSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Marktlokation.
    Inherits from GeschaeftsobjektSchema.
    """

    # class_name is needed to use the correct schema for deserialisation.
    # see function `deserialize` in geschaeftsobjekt.py
    class_name = Messlokation

    # required attributes
    messlokations_id = fields.Str()
    sparte = EnumField(Sparte)
    netzebene = EnumField(Netzebene)
    energierichtung = EnumField(Energierichtung)
    bilanzierungsmethode = EnumField(Bilanzierungsmethode)

    # optional attributes
    messgebietnr = fields.Str(missing=None)
    grundzustaendiger_msb_codenr = fields.Str(missing=None)
    grundzustaendiger_msbim_codenr = fields.Str(missing=None)
    grundzustaendiger_mdl_codenr = fields.Str(missing=None)
    geraete = fields.List(fields.Nested(HardwareSchema), missing=None)  #: List[Hardware]
    messdienstleistung = fields.List(fields.Nested(DienstleistungSchema), missing=None)  #: List[Dienstleistung]

    # only one of the following three optional attributes can be set
    messadresse = fields.Nested(AdresseSchema, missing=None)
    geoadresse = fields.Nested(GeokoordinatenSchema, missing=None)
    katasterinformation = fields.Nested(KatasteradresseSchema, missing=None)

    # # required attributes
    # marktlokations_id = fields.Str()
    # sparte = EnumField(Sparte)
    # energierichtung = EnumField(Energierichtung)
    # bilanzierungsmethode = EnumField(Bilanzierungsmethode)
    # netzebene = EnumField(Netzebene)

    # # optional attributes
    # verbrauchsart = EnumField(Verbrauchsart, missing=None)
    # unterbrechbar = fields.Bool(missing=None)
    # netzbetreibercodenr = fields.Str(missing=None)
    # gebietstyp = EnumField(Gebiettyp, missing=None)
    # netzgebietsnr = fields.Str(missing=None)
    # bilanzierungsgebiet = fields.Str(missing=None)
    # grundversorgercodenr = fields.Str(missing=None)
    # gasqualitaet = EnumField(Gasqualitaet, missing=None)
    # endkunde = fields.Nested(GeschaeftspartnerSchema, missing=None)
    # zugehoerige_messlokation = fields.List(fields.Nested(MesslokationszuordnungSchema), missing=None)

    # only one of the following three optional attributes can be set
    # messadresse = fields.Nested(AdresseSchema, missing=None)
    # geoadresse = fields.Nested(GeokoordinatenSchema, missing=None)
    # katasterinformation = fields.Nested(KatasteradresseSchema, missing=None)
