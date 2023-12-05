"""
Contains Preisblatt class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from pydantic import Field

from ..com.preisposition import Preisposition
from ..com.zeitraum import Zeitraum
from ..enum.preisstatus import Preisstatus
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt
from .marktteilnehmer import Marktteilnehmer


@postprocess_docstring
class Preisblatt(Geschaeftsobjekt):
    """
    Das allgemeine Modell zur Abbildung von Preisen;
    Davon abgeleitet können, über die Zuordnung identifizierender Merkmale, spezielle Preisblatt-Varianten modelliert
    werden.

    Die jeweiligen Sätze von Merkmalen sind in der Grafik ergänzt worden und stellen jeweils eine Ausprägung für die
    verschiedenen Anwendungsfälle der Preisblätter dar.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Preisblatt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Preisblatt.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.PREISBLATT
    #: Eine Bezeichnung für das Preisblatt
    bezeichnung: Optional[str] = None
    #: Preisblatt gilt für angegebene Sparte
    sparte: Optional[Sparte] = None
    #: Merkmal, das anzeigt, ob es sich um vorläufige oder endgültige Preise handelt
    preisstatus: Optional[Preisstatus] = None
    #: Der Zeitraum für den der Preis festgelegt ist
    gueltigkeit: Optional[Zeitraum] = None
    #: Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden können. Z.B. Arbeitspreis, Grundpreis etc
    preispositionen: Optional[list[Preisposition]] = None
    #: Der Netzbetreiber, der die Preise veröffentlicht hat
    herausgeber: Optional[Marktteilnehmer] = None
