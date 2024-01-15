"""
Contains Energiemix class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

from ..enum.oekolabel import Oekolabel
from ..enum.oekozertifikat import Oekozertifikat
from ..enum.sparte import Sparte
from ..utils import postprocess_docstring
from .com import COM
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
        `Energiemix JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Energiemix.json>`_

    """

    #: Eindeutige Nummer zur Identifizierung des Energiemixes
    energiemixnummer: Optional[int] = None
    #: Strom oder Gas etc.
    energieart: Optional[Sparte] = None
    #: Bezeichnung des Energiemix
    bezeichnung: Optional[str] = None
    #: Jahr, für das der Energiemix gilt
    gueltigkeitsjahr: Optional[int] = None
    #: Anteile der jeweiligen Erzeugungsart
    anteil: Optional[list[Energieherkunft]] = None

    #: Bemerkung zum Energiemix
    bemerkung: Optional[str] = None
    #: Höhe des erzeugten CO2-Ausstosses in g/kWh
    co2_emission: Optional[Decimal] = None
    #: Höhe des erzeugten Atommülls in g/kWh
    atommuell: Optional[Decimal] = None
    #: Zertifikate für den Energiemix
    oekozertifikate: Optional[list[Oekozertifikat]] = None
    #: Ökolabel für den Energiemix
    oekolabel: Optional[list[Oekolabel]] = None
    #: Kennzeichen, ob der Versorger zu den Öko Top Ten gehört
    ist_in_oeko_top_ten: Optional[bool] = None
    #: Internetseite, auf der die Strommixdaten veröffentlicht sind
    website: Optional[str] = None
