"""
Contains Zaehlwerk class
and corresponding marshmallow schema for de-/serialization
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

    zaehlwerk_id: Optional[str] = None  # Identifikation des Zählwerks (Registers) innerhalb des Zählers.
    # Oftmals eine laufende Nummer hinter der Zählernummer. Z.B. 47110815_1
    bezeichnung: Optional[str] = None  # Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit.
    richtung: Optional[Energierichtung] = None  # Die Energierichtung, Einspeisung oder Ausspeisung.
    obis_kennzahl: Optional[
        str
    ] = None  # Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.
    # Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert.
    wandlerfaktor: Optional[
        Decimal
    ] = None  # Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum
    # zu kommen.
    einheit: Optional[Mengeneinheit] = None  # Die Einheit der gemessenen Größe, z.B. kWh
    ist_schwachlastfaehig: Optional[bool] = None  #: Schwachlastfaehigkeit
    verwendungszwecke: Optional[
        list[VerwendungszweckProMarktrolle]
    ] = None  #: Verwendungungszweck der Werte Marktlokation
    verbrauchsart: Optional[Verbrauchsart] = None  #: Stromverbrauchsart/Verbrauchsart Marktlokation
    ist_unterbrechbar: Optional[bool] = None  #: Unterbrechbarkeit Marktlokation
    waermenutzung: Optional[Waermenutzung] = None  #: Wärmenutzung Marktlokation
    konzessionsabgabe: Optional[Konzessionsabgabe] = None  #: Konzessionsabgabe
    ist_steuerbefreit: Optional[bool] = None  #: Steuerbefreiung
    vorkommastelle: Optional[int] = None  #: Anzahl der Vorkommastellen
    nachkommastelle: Optional[int] = None  #: Anzahl der Nachkommastellen
    ist_abrechnungsrelevant: Optional[bool] = None  #: Abrechnungsrelevant
    anzahlAblesungen: Optional[int] = None  #: Anzahl Ablesungen pro Jahr
    zaehlzeitregister: Optional[
        Zaehlzeitregister
    ] = None  #: Erweiterte Definition der Zählzeit in Bezug auf ein Register
