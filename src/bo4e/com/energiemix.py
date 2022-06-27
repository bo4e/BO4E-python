"""
Contains Energiemix class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import List

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.com.com import COM
from bo4e.com.energieherkunft import Energieherkunft
from bo4e.enum.oekolabel import Oekolabel
from bo4e.enum.oekozertifikat import Oekozertifikat
from bo4e.enum.sparte import Sparte


class Energiemix(COM):
    """
    Zusammensetzung der gelieferten Energie aus den verschiedenen Primärenergieformen.

    .. graphviz:: /api/dots/bo4e/com/Energiemix.dot

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
    anteil: conlist(Energieherkunft, min_items=1)

    # optional attributes
    #: Bemerkung zum Energiemix
    bemerkung: str = None
    #: Höhe des erzeugten CO2-Ausstosses in g/kWh
    co2_emission: Decimal = None
    #: Höhe des erzeugten Atommülls in g/kWh
    atommuell: Decimal = None
    #: Zertifikate für den Energiemix
    oekozertifikate: List[Oekozertifikat] = []
    #: Ökolabel für den Energiemix
    oekolabel: List[Oekolabel] = []
    #: Kennzeichen, ob der Versorger zu den Öko Top Ten gehört
    oeko_top_ten: bool = None
    #: Internetseite, auf der die Strommixdaten veröffentlicht sind
    website: str = None
