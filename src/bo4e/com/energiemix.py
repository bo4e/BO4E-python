"""
Contains Energiemix class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.oekolabel import Oekolabel
    from ..enum.oekozertifikat import Oekozertifikat
    from ..enum.sparte import Sparte
    from .energieherkunft import Energieherkunft

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module


@postprocess_docstring
class Energiemix(COM):
    """
    Zusammensetzung der gelieferten Energie aus den verschiedenen Primärenergieformen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Energiemix.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energiemix JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Energiemix.json>`_

    """

    energiemixnummer: Optional[int] = None
    """Eindeutige Nummer zur Identifizierung des Energiemixes"""
    energieart: Optional["Sparte"] = None
    """Strom oder Gas etc."""
    bezeichnung: Optional[str] = None
    """Bezeichnung des Energiemix"""
    gueltigkeitsjahr: Optional[int] = None
    """Jahr, für das der Energiemix gilt"""
    anteil: Optional[list["Energieherkunft"]] = None
    """Anteile der jeweiligen Erzeugungsart"""

    bemerkung: Optional[str] = None
    """Bemerkung zum Energiemix"""
    co2_emission: Optional[Decimal] = None
    """Höhe des erzeugten CO2-Ausstosses in g/kWh"""
    atommuell: Optional[Decimal] = None
    """Höhe des erzeugten Atommülls in g/kWh"""
    oekozertifikate: Optional[list["Oekozertifikat"]] = None
    """Zertifikate für den Energiemix"""
    oekolabel: Optional[list["Oekolabel"]] = None
    """Ökolabel für den Energiemix"""
    ist_in_oeko_top_ten: Optional[bool] = None
    """Kennzeichen, ob der Versorger zu den Öko Top Ten gehört"""
    website: Optional[str] = None
    """Internetseite, auf der die Strommixdaten veröffentlicht sind"""
