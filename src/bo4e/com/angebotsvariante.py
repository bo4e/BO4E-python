"""
Contains Angebotsvariante and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Optional

from ..enum.angebotsstatus import Angebotsstatus
from ..utils import postprocess_docstring
from .angebotsteil import Angebotsteil
from .betrag import Betrag
from .com import COM
from .menge import Menge


@postprocess_docstring
class Angebotsvariante(COM):
    """
    Führt die verschiedenen Ausprägungen der Angebotsberechnung auf

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsvariante.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsvariante JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Angebotsvariante.json>`_

    """

    #: Gibt den Status eines Angebotes an.
    angebotsstatus: Optional[Angebotsstatus] = None

    #: Datum der Erstellung der Angebotsvariante
    erstellungsdatum: Optional[datetime] = None

    #: Bis zu diesem Zeitpunkt gilt die Angebotsvariante
    bindefrist: Optional[datetime] = None

    teile: Optional[list[Angebotsteil]] = None
    """
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.
    """

    #: Aufsummierte Wirkarbeitsmenge aller Angebotsteile
    gesamtmenge: Optional[Menge] = None
    # todo: write a validator for this: https://github.com/Hochfrequenz/BO4E-python/issues/320
    #: Aufsummierte Kosten aller Angebotsteile
    gesamtkosten: Optional[Betrag] = None
