"""
Contains Messlokation class
and corresponding marshmallow schema for de-/serialization
"""
import re
from typing import Annotated, Any, List, Optional

from iso3166 import countries
from pydantic import Field, field_validator, model_validator

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
from bo4e.validators import combinations_of_fields

# Structure of a Messlokations-ID
# Ländercode nach DIN ISO 3166 (2 Stellen)
# Verteilnetzbetreiber (6 Stellen)
# Postleitzahl (5 Stellen)
# Zählpunktnummer (20 Stellen alphanumerisch)
# source: https://de.wikipedia.org/wiki/Z%C3%A4hlpunkt#Struktur_der_Z%C3%A4hlpunktbezeichnung

_melo_id_pattern = re.compile(r"^[A-Z]{2}\d{6}\d{5}[A-Z\d]{20}$")


# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Messlokation(Geschaeftsobjekt):
    """
    Object containing information about a Messlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Messlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Messlokation.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.MESSLOKATION
    #: Die Messlokations-Identifikation; Das ist die frühere Zählpunktbezeichnung
    messlokations_id: Annotated[str, Field(pattern=_melo_id_pattern.pattern)]
    #: Sparte der Messlokation, z.B. Gas oder Strom
    sparte: Sparte

    # optional attributes
    #: Spannungsebene der Messung
    netzebene_messung: Optional[Netzebene] = None
    #: Die Nummer des Messgebietes in der ene't-Datenbank
    messgebietnr: Optional[str] = None
    #: Liste der Hardware, die zu dieser Messstelle gehört
    geraete: Optional[List[Hardware]] = None
    #: Liste der Messdienstleistungen, die zu dieser Messstelle gehört
    messdienstleistung: Optional[List[Dienstleistung]] = None  # todo: rename to plural
    #: Zähler, die zu dieser Messlokation gehören
    messlokationszaehler: Optional[List[Zaehler]] = None

    # only one of the following two optional codenr attributes can be set
    grundzustaendiger_msb_codenr: Optional[str] = None
    """
    Codenummer des grundzuständigen Messstellenbetreibers, der für diese Messlokation zuständig ist.
    (Dieser ist immer dann Messstellenbetreiber, wenn kein anderer MSB die Einrichtungen an der Messlokation betreibt.)
    """
    grundzustaendiger_msbim_codenr: Optional[str] = None
    """
    Codenummer des grundzuständigen Messstellenbetreibers für intelligente Messsysteme, der für diese Messlokation
    zuständig ist.
    (Dieser ist immer dann Messstellenbetreiber, wenn kein anderer MSB die Einrichtungen an der Messlokation betreibt.)
    """
    # only one of the following three optional address attributes can be set
    messadresse: Optional[Adresse] = None
    """
    Die Adresse, an der die Messeinrichtungen zu finden sind.
    (Nur angeben, wenn diese von der Adresse der Marktlokation abweicht.)
    """
    geoadresse: Optional[Geokoordinaten] = None
    """
    Alternativ zu einer postalischen Adresse kann hier ein Ort mittels Geokoordinaten angegeben werden
    (z.B. zur Identifikation von Sendemasten).
    """
    katasterinformation: Optional[Katasteradresse] = None
    """
    Alternativ zu einer postalischen Adresse und Geokoordinaten kann hier eine Ortsangabe mittels Gemarkung und
    Flurstück erfolgen.
    """

    # pylint: disable=unused-argument, no-self-argument
    @field_validator("messlokations_id", mode="after")
    @classmethod
    def _validate_messlokations_id_country_code(cls, messlokations_id: str) -> str:
        # The regex pattern in the annotated type above already checks for the correct format
        if not messlokations_id[0:2] in countries:
            raise ValueError(f"The country code '{messlokations_id[0:2]}' is not a valid country code")
        return messlokations_id

    # pylint: disable=duplicate-code
    _validate_address_info = combinations_of_fields(
        "messadresse",
        "geoadresse",
        "katasterinformation",
        valid_combinations={
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (0, 0, 0),
        },
        custom_error_message=(
            "More than one address information is given. "
            'You have to chose either "messadresse", "geoadresse" or "katasterinformation".'
        ),
    )
    "Checks that if an address is given, that there is only one valid address given"

    # pylint: disable=no-self-argument
    @model_validator(mode="before")
    @classmethod
    def validate_grundzustaendiger_x_codenr(cls, data: Any) -> dict[str, Any]:
        """Checks that if a codenr is given, that there is only one valid codenr given."""
        assert isinstance(data, dict), "data is not a dict"
        if (
            data.get("grundzustaendiger_msb_codenr", None) is not None
            and data.get("grundzustaendiger_msbim_codenr", None) is not None
        ):
            raise ValueError("More than one codenr is given.")
        return data
