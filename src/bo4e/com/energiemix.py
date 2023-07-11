"""
Contains Energiemix class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Annotated, List, Optional

from annotated_types import Len

from bo4e.com.com import COM
from bo4e.com.energieherkunft import Energieherkunft
from bo4e.enum.oekolabel import Oekolabel
from bo4e.enum.oekozertifikat import Oekozertifikat
from bo4e.enum.sparte import Sparte

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module


class Energiemix(COM):
    """
    Zusammensetzung der gelieferten Energie aus den verschiedenen Primärenergieformen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Energiemix.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energiemix JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Energiemix.json>`_

    """

    # required attributes
    #: Eindeutige Nummer zur Identifizierung des Energiemixes
    energiemixnummer: int
    #: Strom oder Gas etc.
    energieart: Sparte
    #: Bezeichnung des Energiemix
    bezeichnung: str
    #: Jahr, für das der Energiemix gilt
    gueltigkeitsjahr: int
    #: Anteile der jeweiligen Erzeugungsart
    anteil: Annotated[list[Energieherkunft], Len(1)]

    # optional attributes
    #: Bemerkung zum Energiemix
    bemerkung: Optional[str] = None
    #: Höhe des erzeugten CO2-Ausstosses in g/kWh
    co2_emission: Optional[Decimal] = None
    #: Höhe des erzeugten Atommülls in g/kWh
    atommuell: Optional[Decimal] = None
    #: Zertifikate für den Energiemix
    oekozertifikate: List[Oekozertifikat] = []
    #: Ökolabel für den Energiemix
    oekolabel: List[Oekolabel] = []
    #: Kennzeichen, ob der Versorger zu den Öko Top Ten gehört
    oeko_top_ten: Optional[bool] = None
    #: Internetseite, auf der die Strommixdaten veröffentlicht sind
    website: Optional[str] = None
