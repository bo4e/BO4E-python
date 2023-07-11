"""
Contains Vertrag class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Annotated, List, Optional

from annotated_types import Len

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.unterschrift import Unterschrift
from bo4e.com.vertragskonditionen import Vertragskonditionen
from bo4e.com.vertragsteil import Vertragsteil
from bo4e.enum.botyp import BoTyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.vertragsart import Vertragsart
from bo4e.enum.vertragsstatus import Vertragsstatus

# pylint: disable=unused-argument
# pylint: disable=no-name-in-module

# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Vertrag(Geschaeftsobjekt):
    """
    Modell für die Abbildung von Vertragsbeziehungen;
    Das Objekt dient dazu, alle Arten von Verträgen, die in der Energiewirtschaft Verwendung finden, abzubilden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Vertrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Vertrag.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.VERTRAG
    # pylint: disable=duplicate-code
    #: Eine im Verwendungskontext eindeutige Nummer für den Vertrag
    vertragsnummer: str
    #: Hier ist festgelegt, um welche Art von Vertrag es sich handelt.
    vertragsart: Vertragsart
    #: Gibt den Status des Vertrags an
    vertragsstatus: Vertragsstatus
    #: Unterscheidungsmöglichkeiten für die Sparte
    sparte: Sparte
    #: Gibt an, wann der Vertrag beginnt (inklusiv)
    vertragsbeginn: datetime
    #: Gibt an, wann der Vertrag (voraussichtlich) endet oder beendet wurde (exklusiv)
    vertragsende: datetime
    # todo: add von/bis validator
    vertragspartner1: Geschaeftspartner
    """
    Der "erstgenannte" Vertragspartner.
    In der Regel der Aussteller des Vertrags.
    Beispiel: "Vertrag zwischen Vertragspartner 1 ..."
    """
    vertragspartner2: Geschaeftspartner
    """
    Der "zweitgenannte" Vertragspartner.
    In der Regel der Empfänger des Vertrags.
    Beispiel "Vertrag zwischen Vertragspartner 1 und Vertragspartner 2".
    """
    vertragsteile: Annotated[list[Vertragsteil], Len(1)]
    """
    Der Vertragsteil wird dazu verwendet, eine vertragliche Leistung in Bezug zu einer Lokation
    (Markt- oder Messlokation) festzulegen.
    """

    # optional attributes
    #: Beschreibung zum Vertrag
    beschreibung: Optional[str] = None
    #: Festlegungen zu Laufzeiten und Kündigungsfristen
    vertragskonditionen: Optional[Vertragskonditionen] = None
    #: Unterzeichner des Vertragspartners 1
    unterzeichnervp1: Optional[List[Unterschrift]] = None
    #: Unterzeichner des Vertragspartners 2
    unterzeichnervp2: Optional[List[Unterschrift]] = None
