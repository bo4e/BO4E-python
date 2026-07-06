"""
Contains Zaehlzeitdefinition class
"""

# pylint: disable=unused-argument
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.zaehlzeitsaison import Zaehlzeitsaison
    from .marktteilnehmer import Marktteilnehmer

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Zaehlzeitdefinition(Geschaeftsobjekt):
    """
    Beschreibt, zu welchen Zeiten welche Register aktiv sind.

    Die `Zaehlzeitdefinition` ist unabhängig von konkreter Messhardware: sie weiß nichts über
    `Zaehlwerk`e oder `Zaehler` an einer Messlokation und definiert lediglich abstrakt, welche
    Register-Codes (z.B. "HT", "NT", aber prinzipiell beliebige freie Zeichenketten) zu welchen
    Tageszeiten gelten.

    Die zeitliche Modellierung ist dreistufig geschachtelt:

    1. ``saisons`` – ein Jahr kann in unterschiedliche Saisons aufgeteilt sein (z.B. Sommer/Winter).
       Welche Tage zu welcher Saison gehören, gibt das `saisonprofil` an.
    2. Pro Saison: ``tagtypen`` – verschiedene Tagtypen (z.B. Werktag, Wochenende, Feiertag)
       können unterschiedliche Schaltschemata haben. Welche Tage als Feiertag gelten, gibt der
       `feiertagskalender` an.
    3. Pro Tagtyp: ``umschaltzeiten`` – die eigentlichen Uhrzeiten, zu denen auf welches Register
       umgeschaltet wird.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zaehlzeitdefinition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlzeitdefinition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Zaehlzeitdefinition.json>`_

    """

    typ: Annotated[Literal[BoTyp.ZAEHLZEITDEFINITION], Field(alias="_typ")] = BoTyp.ZAEHLZEITDEFINITION

    urheber: Optional["Marktteilnehmer"] = None
    """Der Marktteilnehmer, der diese Zählzeitdefinition herausgegeben hat (typischerweise Netzbetreiber
    oder Lieferant). Identifiziert zusammen mit einer fachlichen Gültigkeit, welche Definition zu welchem
    Zeitpunkt gilt."""

    feiertagskalender: Optional[str] = None
    """Bezeichnung des Feiertagskalenders, nach dem `FEIERTAGS`-Tagtypen aufgelöst werden (z.B. "BDEW",
    landes- oder gemeindespezifische Kalender). Frei wählbare Zeichenkette, deren Bedeutung zwischen
    den Marktpartnern abgestimmt sein muss."""
    saisonprofil: Optional[str] = None
    """Bezeichnung des Saisonprofils, das die Datumsgrenzen der in `saisons` referenzierten Saisons
    festlegt (z.B. "Sommer/Winter")."""
    saisons: Optional[list["Zaehlzeitsaison"]] = None
    """Die Schaltschemata, gruppiert nach Saison."""
