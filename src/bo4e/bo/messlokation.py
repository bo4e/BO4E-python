"""
Contains Messlokation class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..bo.geraet import Geraet
    from ..bo.lokationszuordnung import Lokationszuordnung
    from ..com.adresse import Adresse
    from ..com.dienstleistung import Dienstleistung
    from ..com.geokoordinaten import Geokoordinaten
    from ..com.katasteradresse import Katasteradresse
    from ..enum.netzebene import Netzebene
    from ..enum.sparte import Sparte
    from .zaehler import Zaehler

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Messlokation(Geschaeftsobjekt):
    """
    Object containing information about a Messlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Messlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Messlokation.json>`_

    """

    typ: Annotated[Literal[Typ.MESSLOKATION], Field(alias="_typ")] = Typ.MESSLOKATION

    messlokations_id: Optional[str] = None
    """Die Messlokations-Identifikation; Das ist die frühere Zählpunktbezeichnung"""
    sparte: Optional["Sparte"] = None
    """Sparte der Messlokation, z.B. Gas oder Strom"""

    netzebene_messung: Optional["Netzebene"] = None
    """Spannungsebene der Messung"""
    messgebietnr: Optional[str] = None
    """Die Nummer des Messgebietes in der ene't-Datenbank"""
    geraete: Optional[list["Geraet"]] = None
    """Liste der Geräte, die zu dieser Messstelle gehört"""
    messdienstleistung: Optional[list["Dienstleistung"]] = None
    """Liste der Messdienstleistungen, die zu dieser Messstelle gehört"""  # todo: rename to plural
    messlokationszaehler: Optional[list["Zaehler"]] = None
    """Zähler, die zu dieser Messlokation gehören"""

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
    messadresse: Optional["Adresse"] = None
    """
    Die Adresse, an der die Messeinrichtungen zu finden sind.
    (Nur angeben, wenn diese von der Adresse der Marktlokation abweicht.)
    """
    geoadresse: Optional["Geokoordinaten"] = None
    """
    Alternativ zu einer postalischen Adresse kann hier ein Ort mittels Geokoordinaten angegeben werden
    (z.B. zur Identifikation von Sendemasten).
    """
    katasterinformation: Optional["Katasteradresse"] = None
    """
    Alternativ zu einer postalischen Adresse und Geokoordinaten kann hier eine Ortsangabe mittels Gemarkung und
    Flurstück erfolgen.
    """
    lokationszuordnungen: Optional[list["Lokationszuordnung"]] = None
    """Lokationszuordnung, um bspw. die zugehörigen Marktlokationen anzugeben"""
    lokationsbuendel_objektcode: Optional[str] = None
    """Lokationsbuendel Code, der die Funktion dieses BOs an der Lokationsbuendelstruktur beschreibt."""
