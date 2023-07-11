"""
Contains Angebotsvariante and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from annotated_types import Len

from bo4e.com.angebotsteil import Angebotsteil
from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.menge import Menge
from bo4e.enum.angebotsstatus import Angebotsstatus


class Angebotsvariante(COM):
    """
    Führt die verschiedenen Ausprägungen der Angebotsberechnung auf

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsvariante.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsvariante JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Angebotsvariante.json>`_

    """

    # required attributes
    #: Gibt den Status eines Angebotes an.
    angebotsstatus: Angebotsstatus

    #: Datum der Erstellung der Angebotsvariante
    erstellungsdatum: datetime

    #: Bis zu diesem Zeitpunkt gilt die Angebotsvariante
    bindefrist: datetime

    teile: Annotated[list[Angebotsteil], Len(1)]
    """
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.
    """

    # optional attributes
    #: Aufsummierte Wirkarbeitsmenge aller Angebotsteile
    gesamtmenge: Optional[Menge] = None
    # todo: write a validator for this: https://github.com/Hochfrequenz/BO4E-python/issues/320
    #: Aufsummierte Kosten aller Angebotsteile
    gesamtkosten: Optional[Betrag] = None
