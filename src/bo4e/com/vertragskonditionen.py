"""
Contains Vertragskonditionen class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal


from marshmallow import fields

from bo4e.com.com import COM
from bo4e.com.zeitraum import Zeitraum


# pylint: disable=too-few-public-methods


class Vertragskonditionen(COM):
    """
    Abbildung für Vertragskonditionen. Die Komponente wird sowohl im Vertrag als auch im Tarif verwendet.

    .. HINT::
        `Vertragskonditionen JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/VertragskonditionenSchema.json>`_

    """

    # optional attributes
    #: Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas"
    beschreibung: str = None
    #: Anzahl der vereinbarten Abschläge pro Jahr, z.B. 12
    anzahl_abschlaege: Decimal = None
    #: Über diesen Zeitraum läuft der Vertrag
    vertragslaufzeit: Zeitraum = None
    #: Innerhalb dieser Frist kann der Vertrag gekündigt werden
    kuendigungsfrist: Zeitraum = None
    #: Falls der Vertrag nicht gekündigt wird, verlängert er sich automatisch um die hier angegebene Zeit
    vertragsverlaengerung: Zeitraum = None
    #: In diesen Zyklen werden Abschläge gestellt. Alternativ kann auch die Anzahl in den Konditionen angeben werden.
    abschlagszyklus: Zeitraum = None
