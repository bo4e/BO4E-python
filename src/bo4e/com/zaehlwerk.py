"""
Contains Zaehlwerk class
"""

from decimal import Decimal
from typing import Optional

from ..com.konzessionsabgabe import Konzessionsabgabe
from ..com.verwendungszweckpromarktrolle import VerwendungszweckProMarktrolle
from ..com.zaehlzeitregister import Zaehlzeitregister
from ..enum.energierichtung import Energierichtung
from ..enum.mengeneinheit import Mengeneinheit
from ..enum.verbrauchsart import Verbrauchsart
from ..enum.waermenutzung import Waermenutzung
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=no-name-in-module
# pylint: disable=no-name-in-module

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Zaehlwerk(COM):
    """
    Mit dieser Komponente werden Zählwerke modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlwerk.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlwerk JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zaehlwerk.json>`_

    """

    #: Identifikation des Zählwerks (Registers) innerhalb des Zählers. Oftmals eine laufende Nummer hinter der Zählernummer. Z.B. 47110815_1
    zaehlwerk_id: Optional[str] = None
    #: Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit.
    bezeichnung: Optional[str] = None
    #: Die Energierichtung, Einspeisung oder Ausspeisung.
    richtung: Optional[Energierichtung] = None
    #: Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird. Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert.
    obis_kennzahl: Optional[str] = None
    #: Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum zu kommen.
    wandlerfaktor: Optional[Decimal] = None
    #: Die Einheit der gemessenen Größe, z.B. kWh
    einheit: Optional[Mengeneinheit] = None
    #: Schwachlastfaehigkeit
    ist_schwachlastfaehig: Optional[bool] = None
    #: Verwendungungszweck der Werte Marktlokation
    verwendungszwecke: Optional[list[VerwendungszweckProMarktrolle]] = None
    #: Stromverbrauchsart/Verbrauchsart Marktlokation
    verbrauchsart: Optional[Verbrauchsart] = None
    #: Unterbrechbarkeit Marktlokation
    ist_unterbrechbar: Optional[bool] = None
    #: Wärmenutzung Marktlokation
    waermenutzung: Optional[Waermenutzung] = None
    #: Konzessionsabgabe
    konzessionsabgabe: Optional[Konzessionsabgabe] = None
    #: Steuerbefreiung
    ist_steuerbefreit: Optional[bool] = None
    #: Anzahl der Vorkommastellen
    vorkommastelle: Optional[int] = None
    #: Anzahl der Nachkommastellen
    nachkommastelle: Optional[int] = None
    #: Abrechnungsrelevant
    ist_abrechnungsrelevant: Optional[bool] = None
    #: Anzahl Ablesungen pro Jahr
    anzahlAblesungen: Optional[int] = None
    #: Erweiterte Definition der Zählzeit in Bezug auf ein Register
    zaehlzeitregister: Optional[Zaehlzeitregister] = None
