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

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/master/json_schemas/bo/MesslokationSchema.json>`_

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
    #: Die Messlokations-Identifikation; Das ist die frühere Zählpunktbezeichnung
    messlokations_id: str = attr.ib(validator=_validate_messlokations_id)
    #: Sparte der Messlokation, z.B. Gas oder Strom
    sparte: Sparte

    # optional attributes
    #: Spannungsebene der Messung
    netzebene_messung: Optional[Netzebene] = attr.ib(default=None)
    #: Die Nummer des Messgebietes in der ene't-Datenbank
    messgebietnr: Optional[str] = attr.ib(default=None)
    #: Liste der Hardware, die zu dieser Messstelle gehört
    geraete: Optional[List[Hardware]] = attr.ib(default=None)
    #: Liste der Messdienstleistungen, die zu dieser Messstelle gehört
    messdienstleistung: Optional[List[Dienstleistung]] = attr.ib(default=None)  # todo: rename to plural
    #: Zähler, die zu dieser Messlokation gehören
    messlokationszaehler: Optional[List[Zaehler]] = attr.ib(default=None)

    # only one of the following two optional codenr attributes can be set
    grundzustaendiger_msb_codenr: Optional[str] = attr.ib(default=None)
    """
    Codenummer des grundzuständigen Messstellenbetreibers, der für diese Messlokation zuständig ist.
    (Dieser ist immer dann Messstellenbetreiber, wenn kein anderer MSB die Einrichtungen an der Messlokation betreibt.)
    """
    grundzustaendiger_msbim_codenr: Optional[str] = attr.ib(default=None)
    """
    Codenummer des grundzuständigen Messstellenbetreibers für intelligente Messsysteme, der für diese Messlokation
    zuständig ist.
    (Dieser ist immer dann Messstellenbetreiber, wenn kein anderer MSB die Einrichtungen an der Messlokation betreibt.)
    """
    # only one of the following three optional address attributes can be set
    messadresse: Optional[Adresse] = attr.ib(default=None)
    """
    Die Adresse, an der die Messeinrichtungen zu finden sind.
    (Nur angeben, wenn diese von der Adresse der Marktlokation abweicht.)
    """
    geoadresse: Optional[Geokoordinaten] = attr.ib(default=None)
    """
    Alternativ zu einer postalischen Adresse kann hier ein Ort mittels Geokoordinaten angegeben werden
    (z.B. zur Identifikation von Sendemasten).
    """
    katasterinformation: Optional[Katasteradresse] = attr.ib(default=None)
    """
    Alternativ zu einer postalischen Adresse und Geokoordinaten kann hier eine Ortsangabe mittels Gemarkung und
    Flurstück erfolgen.
    """

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
    messlokations_id = fields.Str(data_key="messlokationsId")
    sparte = EnumField(Sparte)

    # optional attributes
    netzebene_messung = EnumField(Netzebene, load_default=None, data_key="netzebeneMessung")
    messgebietnr = fields.Str(load_default=None)
    geraete = fields.List(fields.Nested(HardwareSchema), load_default=None)  #: List[Hardware]
    messdienstleistung = fields.List(fields.Nested(DienstleistungSchema), load_default=None)  #: List[Dienstleistung]
    messlokationszaehler = fields.List(fields.Nested(ZaehlerSchema), load_default=None)

    # only one of the following two optional codenr attributes can be set
    grundzustaendiger_msb_codenr = fields.Str(missing=None, data_key="grundzustaendigerMsbCodenr")
    grundzustaendiger_msbim_codenr = fields.Str(missing=None, data_key="grundzustaendigerMsbimCodenr")

    # only one of the following three optional attributes can be set
    messadresse = fields.Nested(AdresseSchema, load_default=None)
    geoadresse = fields.Nested(GeokoordinatenSchema, load_default=None)
    katasterinformation = fields.Nested(KatasteradresseSchema, load_default=None)
