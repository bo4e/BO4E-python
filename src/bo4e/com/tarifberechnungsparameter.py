"""
Contains Tarifberechnungsparameter class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import List, Optional

from bo4e.com.com import COM
from bo4e.com.preis import Preis
from bo4e.com.tarifpreis import Tarifpreis
from bo4e.enum.messpreistyp import Messpreistyp
from bo4e.enum.tarifkalkulationsmethode import Tarifkalkulationsmethode

# yes. there is no description in the official docs.
# https://github.com/Hochfrequenz/BO4E-python/issues/328

# pylint: disable=too-few-public-methods, empty-docstring, too-many-instance-attributes


class Tarifberechnungsparameter(COM):
    """
    In dieser Komponente sind die Berechnungsparameter für die Ermittlung der Tarifkosten zusammengefasst.
    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifberechnungsparameter.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifberechnungsparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Tarifberechnungsparameter.json>`_

    """

    # there are no required attributes
    # optional attributes

    #: Gibt an, wie die Einzelpreise des Tarifes zu verarbeiten sind
    berechnungsmethode: Optional[Tarifkalkulationsmethode] = None
    #: True, falls der Messpreis im Grundpreis (GP) enthalten ist
    messpreis_in_gp_enthalten: Optional[bool] = None

    messpreis_beruecksichtigen: Optional[bool] = None
    """
    True, falls bei der Bildung des Durchschnittspreises für die Höchst- und Mindestpreisbetrachtung der Messpreis mit
    berücksichtigt wird
    """

    #: Typ des Messpreises
    messpreistyp: Optional[Messpreistyp] = None

    #: Im Preis bereits eingeschlossene Leistung (für Gas)
    kw_inklusive: Optional[Decimal] = None
    # todo: type decimal is most likely wrong: https://github.com/Hochfrequenz/BO4E-python/issues/327

    #: Intervall, indem die über "kwInklusive" hinaus abgenommene Leistung kostenpflichtig wird (z.B. je 5 kW 20 EURO)
    kw_weitere_mengen: Optional[Decimal] = None
    # todo: type decimal is most likely wrong: https://github.com/Hochfrequenz/BO4E-python/issues/327

    #: Höchstpreis für den Durchschnitts-Arbeitspreis NT
    hoechstpreis_n_t: Optional[Preis] = None
    #: Höchstpreis für den Durchschnitts-Arbeitspreis HT
    hoechstpreis_h_t: Optional[Preis] = None
    #: Mindestpreis für den Durchschnitts-Arbeitspreis
    mindestpreis: Optional[Preis] = None
    #: Liste mit zusätzlichen Preisen, beispielsweise Messpreise und/oder Leistungspreise
    zusatzpreise: Optional[List[Tarifpreis]] = None
