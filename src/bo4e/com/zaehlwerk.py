"""
Contains Zaehlwerk class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

from bo4e.com.com import COM
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.mengeneinheit import Mengeneinheit

# pylint: disable=no-name-in-module
# pylint: disable=no-name-in-module

# pylint: disable=too-few-public-methods


class Zaehlwerk(COM):
    """
    Mit dieser Komponente werden Zählwerke modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlwerk.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlwerk JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Zaehlwerk.json>`_

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
