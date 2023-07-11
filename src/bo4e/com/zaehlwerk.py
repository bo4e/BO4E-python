"""
Contains Zaehlwerk class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Annotated

# pylint: disable=no-name-in-module
# pylint: disable=no-name-in-module
from pydantic import Field

from bo4e.com.com import COM
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.mengeneinheit import Mengeneinheit

# pylint: disable=too-few-public-methods


class Zaehlwerk(COM):
    """
    Mit dieser Komponente werden Zählwerke modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlwerk.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlwerk JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Zaehlwerk.json>`_

    """

    zaehlwerk_id: str  # Identifikation des Zählwerks (Registers) innerhalb des Zählers.
    # Oftmals eine laufende Nummer hinter der Zählernummer. Z.B. 47110815_1
    bezeichnung: str  # Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit.
    richtung: Energierichtung  # Die Energierichtung, Einspeisung oder Ausspeisung.
    obis_kennzahl: Annotated[
        str,
        Field(
            strict=True,
            pattern=r"(?:(1)-((?:[0-5]?[0-9])|(?:6[0-5])):((?:[1-8]|99))\.((?:6|8|9|29))\.([0-9]{1,2}))|"
            r"(?:(7)-((?:[0-5]?[0-9])|(?:6[0-5])):(.{1,2})\.(.{1,2})\.([0-9]{1,2}))",
        ),
    ]  # Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.
    # Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert.
    wandlerfaktor: Decimal  # Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum
    # zu kommen.
    einheit: Mengeneinheit  # Die Einheit der gemessenen Größe, z.B. kWh
