"""
Contains Energiemix class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import List


from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM
from bo4e.com.energieherkunft import Energieherkunft
from bo4e.enum.oekolabel import Oekolabel
from bo4e.enum.oekozertifikat import Oekozertifikat
from bo4e.enum.sparte import Sparte
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
from pydantic import conlist


class Energiemix(COM):
    """
    Zusammensetzung der gelieferten Energie aus den verschiedenen Primärenergieformen.

    .. HINT::
        `Energiemix JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/EnergiemixSchema.json>`_

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
