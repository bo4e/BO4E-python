"""
Contains Buendelvertrag class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.typ import Typ
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

    typ: Annotated[Literal[Typ.BUENDELVERTRAG], Field(alias="_typ")] = Typ.BUENDELVERTRAG

    # pylint: disable=duplicate-code
    vertragsnummer: Optional[str] = None
    """Eine im Verwendungskontext eindeutige Nummer für den Vertrag"""
    vertragsart: Optional["Vertragsart"] = None
    """Hier ist festgelegt, um welche Art von Vertrag es sich handelt. Z.B. Netznutzungvertrag"""
    vertragsstatus: Optional["Vertragsstatus"] = None
    """Gibt den Status des Vertrages an"""
    sparte: Optional["Sparte"] = None
    """Unterscheidungsmöglichkeiten für die Sparte"""
    vertragsbeginn: Optional[pydantic.AwareDatetime] = None
    """Gibt an, wann der Vertrag beginnt (inklusiv)"""
    vertragsende: Optional[pydantic.AwareDatetime] = None
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

    einzelvertraege: Optional[list["Vertrag"]] = None
    """Die Liste mit den Einzelverträgen zu den Abnahmestellen"""
    vertragskonditionen: Optional[list["Vertragskonditionen"]] = None
    """Festlegungen zu Laufzeiten und Kündigungsfristen"""
    unterzeichnervp1: Optional[list["Unterschrift"]] = None
    """Unterzeichner des Vertragspartners1"""
    unterzeichnervp2: Optional[list["Unterschrift"]] = None
    """Unterzeichner des Vertragspartners2"""
    beschreibung: Optional[str] = None
    """Beschreibung zum Vertrag"""
