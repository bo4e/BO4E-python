"""
Contains TarifpreispositionProOrt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..utils import postprocess_docstring
from .com import COM
from .tarifpreisstaffelproort import TarifpreisstaffelProOrt

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class TarifpreispositionProOrt(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden

    .. raw:: html

        <object data="../_static/images/bo4e/com/TarifpreispositionProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `TarifpreispositionProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/TarifpreispositionProOrt.json>`_

    """

    #: Postleitzahl des Ortes für den der Preis gilt
    postleitzahl: Optional[str] = None
    #: Ort für den der Preis gilt
    ort: Optional[str] = None
    #: ene't-Netznummer des Netzes in dem der Preis gilt
    netznr: Optional[str] = None
    # Hier sind die Staffeln mit ihren Preisenangaben definiert
    preisstaffeln: Optional[list[TarifpreisstaffelProOrt]] = None
    # there are no optional attributes
