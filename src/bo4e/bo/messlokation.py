"""
Contains Messlokation class
and corresponding marshmallow schema for de-/serialization
"""
import re
from typing import List, Optional

import attr
from iso3166 import countries  # type:ignore[import]
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.zaehler import Zaehler, ZaehlerSchema
from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.com.dienstleistung import Dienstleistung, DienstleistungSchema
from bo4e.com.geokoordinaten import Geokoordinaten, GeokoordinatenSchema
from bo4e.com.hardware import Hardware, HardwareSchema
from bo4e.com.katasteradresse import Katasteradresse, KatasteradresseSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte

# Structure of a Messlokations-ID
# Ländercode nach DIN ISO 3166 (2 Stellen)
# Verteilnetzbetreiber (6 Stellen)
# Postleitzahl (5 Stellen)
# Zählpunktnummer (20 Stellen alphanumerisch)
# source: https://de.wikipedia.org/wiki/Z%C3%A4hlpunkt#Struktur_der_Z%C3%A4hlpunktbezeichnung

_melo_id_pattern = re.compile(r"^[A-Z]{2}\d{6}\d{5}[A-Z\d]{20}$")


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Messlokation(Geschaeftsobjekt):
    """
    Object containing information about a Messlokation
    """

    # pylint: disable=unused-argument, no-self-use
    def _validate_messlokations_id(self, messlokations_id_attribute, value):
        if not value:
            raise ValueError("The messlokations_id must not be empty.")
        if not _melo_id_pattern.match(value):
            raise ValueError(f"The messlokations_id '{value}' does not match {_melo_id_pattern.pattern}")
        if not value[0:2] in countries:
            raise ValueError(f"The country code '{value[0:2]}' is not a valid country code")

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.MESSLOKATION)
    messlokations_id: str = attr.ib(validator=_validate_messlokations_id)
    sparte: Sparte

    # optional attributes
    netzebene_messung: Optional[Netzebene] = attr.ib(default=None)
    messgebietnr: Optional[str] = attr.ib(default=None)
    geraete: Optional[List[Hardware]] = attr.ib(default=None)
    messdienstleistung: Optional[List[Dienstleistung]] = attr.ib(default=None)
    messlokationszaehler: Optional[List[Zaehler]] = attr.ib(default=None)

    # only one of the following two optional codenr attributes can be set
    grundzustaendiger_msb_codenr: Optional[str] = attr.ib(default=None)
    grundzustaendiger_msbim_codenr: Optional[str] = attr.ib(default=None)

    # only one of the following three optional address attributes can be set
    messadresse: Optional[Adresse] = attr.ib(default=None)
    geoadresse: Optional[Geokoordinaten] = attr.ib(default=None)
    katasterinformation: Optional[Katasteradresse] = attr.ib(default=None)

    @messadresse.validator
    @geoadresse.validator
    @katasterinformation.validator
    def validate_address_info(self, address_attribute, value):
        """Checks that if an address is given, that there is only one valid address given"""
        all_address_attributes = [
            self.messadresse,
            self.geoadresse,
            self.katasterinformation,
        ]
        amount_of_given_address_infos = len([i for i in all_address_attributes if i is not None])
        if amount_of_given_address_infos > 1:
            raise ValueError("More than one address information is given.")

    @grundzustaendiger_msb_codenr.validator
    @grundzustaendiger_msbim_codenr.validator
    def validate_grundzustaendiger_x_codenr(self, attribute, value):
        """Checks that if a codenr is given, that there is only one valid codenr given."""
        all_grundzustaendiger_x_codenr_attributes = [
            self.grundzustaendiger_msb_codenr,
            self.grundzustaendiger_msbim_codenr,
        ]
        amount_of_given_grundzustaendiger_x_codenr = len(
            [i for i in all_grundzustaendiger_x_codenr_attributes if i is not None]
        )
        if amount_of_given_grundzustaendiger_x_codenr > 1:
            raise ValueError("More than one codenr is given.")


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

    # optional attributes
    netzebene_messung = EnumField(Netzebene, load_default=None)
    messgebietnr = fields.Str(load_default=None)
    geraete = fields.List(fields.Nested(HardwareSchema), load_default=None)  #: List[Hardware]
    messdienstleistung = fields.List(fields.Nested(DienstleistungSchema), load_default=None)  #: List[Dienstleistung]
    messlokationszaehler = fields.List(fields.Nested(ZaehlerSchema), load_default=None)

    # only one of the following two optional codenr attributes can be set
    grundzustaendiger_msb_codenr = fields.Str(load_default=None)
    grundzustaendiger_msbim_codenr = fields.Str(load_default=None)

    # only one of the following three optional attributes can be set
    messadresse = fields.Nested(AdresseSchema, load_default=None)
    geoadresse = fields.Nested(GeokoordinatenSchema, load_default=None)
    katasterinformation = fields.Nested(KatasteradresseSchema, load_default=None)
