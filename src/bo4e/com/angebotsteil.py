"""
Contains Angebotsteil class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..bo.marktlokation import Marktlokation
from ..utils import postprocess_docstring
from .angebotsposition import Angebotsposition
from .betrag import Betrag
from .com import COM
from .menge import Menge
from .zeitraum import Zeitraum

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
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
        `Angebotsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Angebotsteil.json>`_

    """

    #: Einzelne Positionen, die zu diesem Angebotsteil gehören
    positionen: Optional[list[Angebotsposition]] = None

    #: Identifizierung eines Subkapitels einer Anfrage, beispielsweise das Los einer Ausschreibung
    anfrage_subreferenz: Optional[str] = None
    lieferstellenangebotsteil: Optional[list[Marktlokation]] = None
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
