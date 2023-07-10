"""
Contains TarifpreispositionProOrt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated

from annotated_types import Len
from pydantic import Field

from bo4e.com.com import COM
from bo4e.com.tarifpreisstaffelproort import TarifpreisstaffelProOrt

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


class TarifpreispositionProOrt(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden

    .. raw:: html

        <object data="../_static/images/bo4e/com/TarifpreispositionProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `TarifpreispositionProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TarifpreispositionProOrt.json>`_

    """

    # required attributes
    #: Postleitzahl des Ortes für den der Preis gilt
    postleitzahl: Annotated[str, Field(strict=True, pattern=r"^\d{5}$")]
    #: Ort für den der Preis gilt
    ort: str
    #: ene't-Netznummer des Netzes in dem der Preis gilt
    netznr: str
    # Hier sind die Staffeln mit ihren Preisenangaben definiert
    preisstaffeln: Annotated[list[TarifpreisstaffelProOrt], Len(1)]
    # there are no optional attributes
