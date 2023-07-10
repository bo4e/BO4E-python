"""
Contains Angebotsteil class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Annotated, List, Optional

from annotated_types import Len

from bo4e.bo.marktlokation import Marktlokation
from bo4e.com.angebotsposition import Angebotsposition
from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.menge import Menge
from bo4e.com.zeitraum import Zeitraum

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


class Angebotsteil(COM):
    """
    Mit dieser Komponente wird ein Teil einer Angebotsvariante abgebildet.
    Hier werden alle Angebotspositionen aggregiert.
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsteil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Angebotsteil.json>`_

    """

    # required attributes
    #: Einzelne Positionen, die zu diesem Angebotsteil gehören
    positionen: Annotated[list[Angebotsposition], Len(1)]

    # optional attributes
    #: Identifizierung eines Subkapitels einer Anfrage, beispielsweise das Los einer Ausschreibung
    anfrage_subreferenz: Optional[str] = None
    lieferstellenangebotsteil: Optional[List[Marktlokation]] = None
    """
    Marktlokationen, für die dieses Angebotsteil gilt, falls vorhanden.
    Durch die Marktlokation ist auch die Lieferadresse festgelegt
    """
    #: Summe der Verbräuche aller in diesem Angebotsteil eingeschlossenen Lieferstellen
    gesamtmengeangebotsteil: Optional[Menge] = None
    #: Summe der Jahresenergiekosten aller in diesem Angebotsteil enthaltenen Lieferstellen
    gesamtkostenangebotsteil: Optional[Betrag] = None
    #: Hier kann der Belieferungszeitraum angegeben werden, für den dieser Angebotsteil gilt
    lieferzeitraum: Optional[Zeitraum] = None
