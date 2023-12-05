"""
Contains Buendelvertrag class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from datetime import datetime
from typing import Annotated, Optional

from pydantic import Field

from ..com.unterschrift import Unterschrift
from ..com.vertragskonditionen import Vertragskonditionen
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.vertragsart import Vertragsart
from ..enum.vertragsstatus import Vertragsstatus
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt
from .geschaeftspartner import Geschaeftspartner
from .vertrag import Vertrag


@postprocess_docstring
class Buendelvertrag(Geschaeftsobjekt):
    """
    Abbildung eines Bündelvertrags.
    Es handelt sich hierbei um eine Liste von Einzelverträgen, die in einem Vertragsobjekt gebündelt sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Buendelvertrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Buendelvertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Buendelvertrag.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.BUENDELVERTRAG

    # pylint: disable=duplicate-code
    #: Eine im Verwendungskontext eindeutige Nummer für den Vertrag
    vertragsnummer: Optional[str] = None
    #: Hier ist festgelegt, um welche Art von Vertrag es sich handelt. Z.B. Netznutzungvertrag
    vertragsart: Optional[Vertragsart] = None
    #: Gibt den Status des Vertrages an
    vertragsstatus: Optional[Vertragsstatus] = None
    #: Unterscheidungsmöglichkeiten für die Sparte
    sparte: Optional[Sparte] = None
    #: Gibt an, wann der Vertrag beginnt (inklusiv)
    vertragsbeginn: Optional[datetime] = None
    #: Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde (exklusiv)
    vertragsende: Optional[datetime] = None
    #: Der "erstgenannte" Vertragspartner. In der Regel der Aussteller des Vertrags.
    #: Beispiel: "Vertrag zwischen Vertagspartner 1 ..."
    vertragspartner1: Optional[Geschaeftspartner] = None
    #: Der "zweitgenannte" Vertragspartner. In der Regel der Empfänger des Vertrags.
    #: Beispiel "Vertrag zwischen Vertagspartner 1 und Vertragspartner 2"
    vertragspartner2: Optional[Geschaeftspartner] = None

    #: Die Liste mit den Einzelverträgen zu den Abnahmestellen
    einzelvertraege: Optional[list[Vertrag]] = None
    #: Festlegungen zu Laufzeiten und Kündigungsfristen
    vertragskonditionen: Optional[list[Vertragskonditionen]] = None
    #: Unterzeichner des Vertragspartners1
    unterzeichnervp1: Optional[list[Unterschrift]] = None
    #: Unterzeichner des Vertragspartners2
    unterzeichnervp2: Optional[list[Unterschrift]] = None
    #: Beschreibung zum Vertrag
    beschreibung: Optional[str] = None
