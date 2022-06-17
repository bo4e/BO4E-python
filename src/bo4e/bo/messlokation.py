"""
Contains Messlokation class
and corresponding marshmallow schema for de-/serialization
"""
import re
from typing import List, Optional


from iso3166 import countries  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.zaehler import Zaehler
from bo4e.com.adresse import Adresse
from bo4e.com.dienstleistung import Dienstleistung
from bo4e.com.geokoordinaten import Geokoordinaten
from bo4e.com.hardware import Hardware
from bo4e.com.katasteradresse import Katasteradresse
from bo4e.enum.botyp import BoTyp
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte

# Structure of a Messlokations-ID
# Ländercode nach DIN ISO 3166 (2 Stellen)
# Verteilnetzbetreiber (6 Stellen)
# Postleitzahl (5 Stellen)
# Zählpunktnummer (20 Stellen alphanumerisch)
# source: https://de.wikipedia.org/wiki/Z%C3%A4hlpunkt#Struktur_der_Z%C3%A4hlpunktbezeichnung
from pydantic import validator, StrictStr

_melo_id_pattern = re.compile(r"^[A-Z]{2}\d{6}\d{5}[A-Z\d]{20}$")


# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Messlokation(Geschaeftsobjekt):
    """
    Object containing information about a Messlokation

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/MesslokationSchema.json>`_

    """

    # pylint: disable=unused-argument
    def _validate_messlokations_id(self, messlokations_id_attribute, value):
        if not value:
            raise ValueError("The messlokations_id must not be empty.")
        if not _melo_id_pattern.match(value):
            raise ValueError(f"The messlokations_id '{value}' does not match {_melo_id_pattern.pattern}")
        if not value[0:2] in countries:
            raise ValueError(f"The country code '{value[0:2]}' is not a valid country code")

    # required attributes
    bo_typ: BoTyp = BoTyp.MESSLOKATION
    #: Die Messlokations-Identifikation; Das ist die frühere Zählpunktbezeichnung
    messlokations_id: str
    #: Sparte der Messlokation, z.B. Gas oder Strom
    sparte: Sparte

    # optional attributes
    #: Spannungsebene der Messung
    netzebene_messung: Netzebene = None
    #: Die Nummer des Messgebietes in der ene't-Datenbank
    messgebietnr: str = None
    #: Liste der Hardware, die zu dieser Messstelle gehört
    geraete: List[Hardware] = None
    #: Liste der Messdienstleistungen, die zu dieser Messstelle gehört
    messdienstleistung: List[Dienstleistung] = None  # todo: rename to plural
    #: Zähler, die zu dieser Messlokation gehören
    messlokationszaehler: List[Zaehler] = None

    # only one of the following two optional codenr attributes can be set
    grundzustaendiger_msb_codenr: str = None
    """
    Codenummer des grundzuständigen Messstellenbetreibers, der für diese Messlokation zuständig ist.
    (Dieser ist immer dann Messstellenbetreiber, wenn kein anderer MSB die Einrichtungen an der Messlokation betreibt.)
    """
    grundzustaendiger_msbim_codenr: str = None
    """
    Codenummer des grundzuständigen Messstellenbetreibers für intelligente Messsysteme, der für diese Messlokation
    zuständig ist.
    (Dieser ist immer dann Messstellenbetreiber, wenn kein anderer MSB die Einrichtungen an der Messlokation betreibt.)
    """
    # only one of the following three optional address attributes can be set
    messadresse: Adresse = None
    """
    Die Adresse, an der die Messeinrichtungen zu finden sind.
    (Nur angeben, wenn diese von der Adresse der Marktlokation abweicht.)
    """
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

    @validator("katasterinformation", always=True)
    def validate_address_info(cls, katasterinformation, values):
        """Checks that if an address is given, that there is only one valid address given"""
        all_address_attributes = [
            values["messadresse"],
            values["geoadresse"],
            katasterinformation,
        ]
        amount_of_given_address_infos = len([i for i in all_address_attributes if i is not None])
        if amount_of_given_address_infos > 1:
            raise ValueError("More than one address information is given.")

    @validator("grundzustaendiger_msbim_codenr", always=True)
    def validate_grundzustaendiger_x_codenr(cls, grundzustaendiger_msbim_codenr, values):
        """Checks that if a codenr is given, that there is only one valid codenr given."""
        all_grundzustaendiger_x_codenr_attributes = [
            values["grundzustaendiger_msb_codenr"],
            grundzustaendiger_msbim_codenr,
        ]
        amount_of_given_grundzustaendiger_x_codenr = len(
            [i for i in all_grundzustaendiger_x_codenr_attributes if i is not None]
        )
        if amount_of_given_grundzustaendiger_x_codenr > 1:
            raise ValueError("More than one codenr is given.")
        else:
            return grundzustaendiger_msbim_codenr
