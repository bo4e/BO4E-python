"""
Contains Vertrag class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.unterschrift import Unterschrift
    from ..com.vertragskonditionen import Vertragskonditionen
    from ..com.vertragsteil import Vertragsteil
    from ..enum.sparte import Sparte
    from ..enum.vertragsart import Vertragsart
    from ..enum.vertragsstatus import Vertragsstatus
    from .geschaeftspartner import Geschaeftspartner

# pylint: disable=unused-argument
# pylint: disable=no-name-in-module

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Vertrag(Geschaeftsobjekt):
    """
    Modell für die Abbildung von Vertragsbeziehungen;
    Das Objekt dient dazu, alle Arten von Verträgen, die in der Energiewirtschaft Verwendung finden, abzubilden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Vertrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Vertrag.json>`_

    """

    typ: Annotated[Literal[BoTyp.VERTRAG], Field(alias="_typ")] = BoTyp.VERTRAG
    # pylint: disable=duplicate-code
    vertragsnummer: str | None = None
    """Eine im Verwendungskontext eindeutige Nummer für den Vertrag"""
    vertragsart: Optional["Vertragsart"] = None
    """Hier ist festgelegt, um welche Art von Vertrag es sich handelt."""
    vertragsstatus: Optional["Vertragsstatus"] = None
    """Gibt den Status des Vertrags an"""
    sparte: Optional["Sparte"] = None
    """Unterscheidungsmöglichkeiten für die Sparte"""
    vertragsbeginn: pydantic.AwareDatetime | None = None
    """Gibt an, wann der Vertrag beginnt (inklusiv)"""
    vertragsende: pydantic.AwareDatetime | None = None
    """Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde (exklusiv)"""
    # todo: add von/bis validator
    vertragspartner1: Optional["Geschaeftspartner"] = None
    """
    Der "erstgenannte" Vertragspartner.
    In der Regel der Aussteller des Vertrags.
    Beispiel: "Vertrag zwischen Vertragspartner 1 ..."
    """
    vertragspartner2: Optional["Geschaeftspartner"] = None
    """
    Der "zweitgenannte" Vertragspartner.
    In der Regel der Empfänger des Vertrags.
    Beispiel "Vertrag zwischen Vertragspartner 1 und Vertragspartner 2".
    """
    vertragsteile: list["Vertragsteil"] | None = None
    """
    Der Vertragsteil wird dazu verwendet, eine vertragliche Leistung in Bezug zu einer Lokation
    (Markt- oder Messlokation) festzulegen.
    """

    beschreibung: str | None = None
    """Beschreibung zum Vertrag"""
    vertragskonditionen: Optional["Vertragskonditionen"] = None
    """Festlegungen zu Laufzeiten und Kündigungsfristen"""
    unterzeichnervp1: list["Unterschrift"] | None = None
    """Unterzeichner des Vertragspartners 1"""
    unterzeichnervp2: list["Unterschrift"] | None = None
    """Unterzeichner des Vertragspartners 2"""
