"""
Contains Zaehlwerk class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

import attrs
from attrs.validators import matches_re
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.mengeneinheit import Mengeneinheit


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Zaehlwerk(COM):
    """
    Mit dieser Komponente werden Zählwerke modelliert.

    .. HINT::
        `Zaehlwerk JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ZaehlwerkSchema.json>`_

    """

    zaehlwerk_id: str = attrs.field(
        validator=attrs.validators.instance_of(str)
    )  # Identifikation des Zählwerks (Registers) innerhalb des Zählers.
    # Oftmals eine laufende Nummer hinter der Zählernummer. Z.B. 47110815_1
    bezeichnung: str = attrs.field(
        validator=attrs.validators.instance_of(str)
    )  # Zusätzliche Bezeichnung, z.B. Zählwerk_Wirkarbeit.
    richtung: Energierichtung  # Die Energierichtung, Einspeisung oder Ausspeisung.
    obis_kennzahl: str = attrs.field(
        validator=matches_re(
            r"(?:(1)-((?:[0-5]?[0-9])|(?:6[0-5])):((?:[1-8]|99))\.((?:6|8|9|29))\.([0-9]{1,2}))|"
            r"(?:(7)-((?:[0-5]?[0-9])|(?:6[0-5])):(.{1,2})\.(.{1,2})\.([0-9]{1,2}))"
        )
    )  # Die OBIS-Kennzahl für das Zählwerk, die festlegt, welche auf die gemessene Größe mit dem Stand gemeldet wird.
    # Nur Zählwerkstände mit dieser OBIS-Kennzahl werden an diesem Zählwerk registriert.
    wandlerfaktor: Decimal = attrs.field(
        validator=attrs.validators.instance_of(Decimal)
    )  # Mit diesem Faktor wird eine Zählerstandsdifferenz multipliziert, um zum eigentlichen Verbrauch im Zeitraum
    # zu kommen.
    einheit: Mengeneinheit  # Die Einheit der gemessenen Größe, z.B. kWh


class ZaehlwerkSchema(COMSchema):
    """
    Schema for de-/serialization of Zaehlwerk.
    """

    class_name = Zaehlwerk
    zaehlwerk_id = fields.Str(data_key="zaehlwerkId")
    bezeichnung = fields.Str()
    richtung = EnumField(Energierichtung)
    obis_kennzahl = fields.Str(data_key="obisKennzahl")
    wandlerfaktor = fields.Decimal(as_string=True)
    einheit = EnumField(Mengeneinheit)
