"""
Contains Angebotsteil class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.bo.marktlokation import Marktlokation
from bo4e.com.angebotsposition import Angebotsposition
from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.menge import Menge
from bo4e.com.zeitraum import Zeitraum


class Angebotsteil(COM):
    """
    Mit dieser Komponente wird ein Teil einer Angebotsvariante abgebildet.
    Hier werden alle Angebotspositionen aggregiert.
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.

    .. HINT::
        `Angebotsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AngebotsteilSchema.json>`_

    """

    # required attributes
    #: Einzelne Positionen, die zu diesem Angebotsteil gehören
    positionen: conlist(Angebotsposition, min_items=1)

    # optional attributes
    #: Identifizierung eines Subkapitels einer Anfrage, beispielsweise das Los einer Ausschreibung
    anfrage_subreferenz: str = None
    lieferstellenangebotsteil: List[Marktlokation] = None
    """
    Marktlokationen, für die dieses Angebotsteil gilt, falls vorhanden.
    Durch die Marktlokation ist auch die Lieferadresse festgelegt
    """
    #: Summe der Verbräuche aller in diesem Angebotsteil eingeschlossenen Lieferstellen
    gesamtmengeangebotsteil: Menge = None
    #: Summe der Jahresenergiekosten aller in diesem Angebotsteil enthaltenen Lieferstellen
    gesamtkostenangebotsteil: Betrag = None
    #: Hier kann der Belieferungszeitraum angegeben werden, für den dieser Angebotsteil gilt
    lieferzeitraum: Zeitraum = None
