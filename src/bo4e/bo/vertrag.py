"""
Contains Vertrag class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Annotated, Optional

from pydantic import Field

from ..com.unterschrift import Unterschrift
from ..com.vertragskonditionen import Vertragskonditionen
from ..com.vertragsteil import Vertragsteil
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.vertragsart import Vertragsart
from ..enum.vertragsstatus import Vertragsstatus
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt
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
        `Vertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Vertrag.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.VERTRAG
    # pylint: disable=duplicate-code
    #: Eine im Verwendungskontext eindeutige Nummer für den Vertrag
    vertragsnummer: Optional[str] = None
    #: Hier ist festgelegt, um welche Art von Vertrag es sich handelt.
    vertragsart: Optional[Vertragsart] = None
    #: Gibt den Status des Vertrags an
    vertragsstatus: Optional[Vertragsstatus] = None
    #: Unterscheidungsmöglichkeiten für die Sparte
    sparte: Optional[Sparte] = None
    #: Gibt an, wann der Vertrag beginnt (inklusiv)
    vertragsbeginn: Optional[datetime] = None
    #: Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde (exklusiv)
    vertragsende: Optional[datetime] = None
    # todo: add von/bis validator
    vertragspartner1: Optional[Geschaeftspartner] = None
    """
    Der "erstgenannte" Vertragspartner.
    In der Regel der Aussteller des Vertrags.
    Beispiel: "Vertrag zwischen Vertragspartner 1 ..."
    """
    vertragspartner2: Optional[Geschaeftspartner] = None
    """
    Der "zweitgenannte" Vertragspartner.
    In der Regel der Empfänger des Vertrags.
    Beispiel "Vertrag zwischen Vertragspartner 1 und Vertragspartner 2".
    """
    vertragsteile: Optional[list[Vertragsteil]] = None
    """
    Der Vertragsteil wird dazu verwendet, eine vertragliche Leistung in Bezug zu einer Lokation
    (Markt- oder Messlokation) festzulegen.
    """

    #: Beschreibung zum Vertrag
    beschreibung: Optional[str] = None
    #: Festlegungen zu Laufzeiten und Kündigungsfristen
    vertragskonditionen: Optional[Vertragskonditionen] = None
    #: Unterzeichner des Vertragspartners 1
    unterzeichnervp1: Optional[list[Unterschrift]] = None
    #: Unterzeichner des Vertragspartners 2
    unterzeichnervp2: Optional[list[Unterschrift]] = None
