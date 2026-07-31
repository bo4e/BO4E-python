"""
Contains Buendelvertrag class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.unterschrift import Unterschrift
    from ..com.vertragskonditionen import Vertragskonditionen
    from ..enum.sparte import Sparte
    from ..enum.vertragsart import Vertragsart
    from ..enum.vertragsstatus import Vertragsstatus
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
        `Buendelvertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Buendelvertrag.json>`_

    """

    typ: Annotated[Literal[BoTyp.BUENDELVERTRAG], Field(alias="_typ")] = BoTyp.BUENDELVERTRAG

    # pylint: disable=duplicate-code
    vertragsnummer: str | None = None
    """Eine im Verwendungskontext eindeutige Nummer für den Vertrag"""
    vertragsart: Optional["Vertragsart"] = None
    """Hier ist festgelegt, um welche Art von Vertrag es sich handelt. Z.B. Netznutzungvertrag"""
    vertragsstatus: Optional["Vertragsstatus"] = None
    """Gibt den Status des Vertrages an"""
    sparte: Optional["Sparte"] = None
    """Unterscheidungsmöglichkeiten für die Sparte"""
    vertragsbeginn: pydantic.AwareDatetime | None = None
    """Gibt an, wann der Vertrag beginnt (inklusiv)"""
    vertragsende: pydantic.AwareDatetime | None = None
    """Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde (exklusiv)"""
    vertragspartner1: Optional["Geschaeftspartner"] = None
    """
    Der "erstgenannte" Vertragspartner. In der Regel der Aussteller des Vertrags.
    Beispiel: "Vertrag zwischen Vertagspartner 1 ..."
    """
    vertragspartner2: Optional["Geschaeftspartner"] = None
    """
    Der "zweitgenannte" Vertragspartner. In der Regel der Empfänger des Vertrags.
    Beispiel "Vertrag zwischen Vertagspartner 1 und Vertragspartner 2"
    """

    einzelvertraege: list["Vertrag"] | None = None
    """Die Liste mit den Einzelverträgen zu den Abnahmestellen"""
    vertragskonditionen: list["Vertragskonditionen"] | None = None
    """Festlegungen zu Laufzeiten und Kündigungsfristen"""
    unterzeichnervp1: list["Unterschrift"] | None = None
    """Unterzeichner des Vertragspartners1"""
    unterzeichnervp2: list["Unterschrift"] | None = None
    """Unterzeichner des Vertragspartners2"""
    beschreibung: str | None = None
    """Beschreibung zum Vertrag"""
