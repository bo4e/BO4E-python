"""
Contains Preisblatt class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.preisposition import Preisposition
    from ..com.zeitraum import Zeitraum
    from ..enum.preisstatus import Preisstatus
    from ..enum.sparte import Sparte
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
        `Preisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Preisblatt.json>`_

    """

    typ: Annotated[Literal[Typ.PREISBLATT], Field(alias="_typ")] = Typ.PREISBLATT
    bezeichnung: Optional[str] = None
    """Eine Bezeichnung für das Preisblatt"""
    sparte: Optional["Sparte"] = None
    """Preisblatt gilt für angegebene Sparte"""
    preisstatus: Optional["Preisstatus"] = None
    """Merkmal, das anzeigt, ob es sich um vorläufige oder endgültige Preise handelt"""
    gueltigkeit: Optional["Zeitraum"] = None
    """Der Zeitraum für den der Preis festgelegt ist"""
    preispositionen: Optional[list["Preisposition"]] = None
    """Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden können. Z.B. Arbeitspreis, Grundpreis etc"""
    herausgeber: Optional["Marktteilnehmer"] = None
    """Der Netzbetreiber, der die Preise veröffentlicht hat"""
