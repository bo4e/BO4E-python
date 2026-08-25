"""
Contains Zaehlwerk class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..com.konzessionsabgabe import Konzessionsabgabe
    from ..com.messwert import Messwert
    from ..com.verwendungszweckpromarktrolle import VerwendungszweckProMarktrolle
    from ..com.zaehlzeitregister import Zaehlzeitregister
    from ..enum.energierichtung import Energierichtung
    from ..enum.mengeneinheit import Mengeneinheit
    from ..enum.verbrauchsart import Verbrauchsart
    from ..enum.waermenutzung import Waermenutzung


@postprocess_docstring
class Zaehlwerk(COM):
    """
    Mit dieser Komponente werden Zählwerke modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlwerk.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlwerk JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zaehlwerk.json>`_

    """

    typ: Annotated[Literal[ComTyp.ZAEHLWERK], Field(alias="_typ")] = ComTyp.ZAEHLWERK

    zaehlwerk_id: str | None = None
    """
    Identifikation des Zählwerks (Registers) innerhalb des Zählers.
    Oftmals eine laufende Nummer hinter der Zählernummer. Z.B. 47110815_1
    """
    bezeichnung: str | None = None
    """Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit."""
    richtung: Optional["Energierichtung"] = None
    """Die Energierichtung, Einspeisung oder Ausspeisung."""
    obis_kennzahl: str | None = None
    """
    Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.
    Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert.
    """
    wandlerfaktor: Decimal | None = None
    """
    Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum
    zu kommen.
    """
    einheit: Optional["Mengeneinheit"] = None
    """Die Einheit der gemessenen Größe, z.B. kWh"""
    ist_schwachlastfaehig: bool | None = None
    """Schwachlastfaehigkeit"""
    verwendungszwecke: list["VerwendungszweckProMarktrolle"] | None = None
    """Verwendungungszweck der Werte Marktlokation"""
    verbrauchsart: Optional["Verbrauchsart"] = None
    """Stromverbrauchsart/Verbrauchsart Marktlokation"""
    waermenutzung: Optional["Waermenutzung"] = None
    """Wärmenutzung Marktlokation"""
    konzessionsabgabe: Optional["Konzessionsabgabe"] = None
    """Konzessionsabgabe"""
    ist_steuerbefreit: bool | None = None
    """Steuerbefreiung"""
    vorkommastelle: int | None = None
    """Anzahl der Vorkommastellen"""
    nachkommastelle: int | None = None
    """Anzahl der Nachkommastellen"""
    ist_abrechnungsrelevant: bool | None = None
    """Abrechnungsrelevant"""
    anzahlAblesungen: int | None = None  # noqa: N815 (pre-existing public field name)
    """Anzahl Ablesungen pro Jahr"""
    zaehlzeitregister: Optional["Zaehlzeitregister"] = None
    """Erweiterte Definition der Zählzeit in Bezug auf ein Register"""
    messwerte: list["Messwert"] | None = None
    """Gemessene Werte des Zählwerks"""
