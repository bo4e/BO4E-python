"""
Contains Messlokation class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

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
    messlokations_id: Optional[str] = None
    #: Sparte der Messlokation, z.B. Gas oder Strom
    sparte: Optional[Sparte] = None

    # optional attributes
    #: Spannungsebene der Messung
    netzebene_messung: Optional[Netzebene] = None
    #: Die Nummer des Messgebietes in der ene't-Datenbank
    messgebietnr: Optional[str] = None
    #: Liste der Hardware, die zu dieser Messstelle gehört
    geraete: Optional[list[Hardware]] = None
    #: Liste der Messdienstleistungen, die zu dieser Messstelle gehört
    messdienstleistung: Optional[list[Dienstleistung]] = None  # todo: rename to plural
    #: Zähler, die zu dieser Messlokation gehören
    messlokationszaehler: Optional[list[Zaehler]] = None

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
