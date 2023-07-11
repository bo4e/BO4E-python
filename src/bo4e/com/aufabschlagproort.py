"""
Contains AufAbschlagProOrt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated

from annotated_types import Len

from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrt
from bo4e.com.com import COM

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


class AufAbschlagProOrt(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang
    mit örtlichen Gültigkeiten abgebildet werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AufAbschlagProOrt.json>`_

    """

    # required attributes
    #: Die Postleitzahl des Ortes für den der Aufschlag gilt.
    postleitzahl: str
    #: Der Ort für den der Aufschlag gilt.
    ort: str
    #: Die ene't-Netznummer des Netzes in dem der Aufschlag gilt.
    netznr: str
    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung.
    staffeln: Annotated[list[AufAbschlagstaffelProOrt], Len(1)]
