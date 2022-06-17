"""
Contains AufAbschlagProOrt class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List


from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrt
from bo4e.com.com import COM


# pylint: disable=too-few-public-methods
from pydantic import conlist, StrictStr


class AufAbschlagProOrt(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang
    mit örtlichen Gültigkeiten abgebildet werden.

    .. HINT::
        `AufAbschlagProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AufAbschlagProOrtSchema.json>`_

    """

    # required attributes
    #: Die Postleitzahl des Ortes für den der Aufschlag gilt.
    postleitzahl: str
    #: Der Ort für den der Aufschlag gilt.
    ort: str
    #: Die ene't-Netznummer des Netzes in dem der Aufschlag gilt.
    netznr: str
    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung.
    staffeln: conlist(AufAbschlagstaffelProOrt, min_items=1)
