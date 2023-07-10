"""
Contains Preisblatt class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from annotated_types import Len

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.marktteilnehmer import Marktteilnehmer
from bo4e.com.preisposition import Preisposition
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.botyp import BoTyp
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte


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
        `Preisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Preisblatt.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.PREISBLATT
    #: Eine Bezeichnung für das Preisblatt
    bezeichnung: str
    #: Preisblatt gilt für angegebene Sparte
    sparte: Sparte
    #: Merkmal, das anzeigt, ob es sich um vorläufige oder endgültige Preise handelt
    preisstatus: Preisstatus
    #: Der Zeitraum für den der Preis festgelegt ist
    gueltigkeit: Zeitraum
    #: Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden können. Z.B. Arbeitspreis, Grundpreis etc
    preispositionen: Annotated[list[Preisposition], Len(1)]
    # optional attributes
    #: Der Netzbetreiber, der die Preise veröffentlicht hat
    herausgeber: Optional[Marktteilnehmer] = None
