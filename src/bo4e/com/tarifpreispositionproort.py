"""
Contains TarifpreispositionProOrt class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import constr, conlist

from bo4e.com.com import COM
from bo4e.com.tarifpreisstaffelproort import TarifpreisstaffelProOrt


class TarifpreispositionProOrt(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden

    .. HINT::
        `TarifpreispositionProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TarifpreispositionProOrtSchema.json>`_

    """

    # required attributes
    #: Postleitzahl des Ortes für den der Preis gilt
    postleitzahl: constr(strict=True, regex=r"^\d{5}$")
    #: Ort für den der Preis gilt
    ort: str
    #: ene't-Netznummer des Netzes in dem der Preis gilt
    netznr: str
    # Hier sind die Staffeln mit ihren Preisenangaben definiert
    preisstaffeln: conlist(TarifpreisstaffelProOrt, min_items=1)
    # there are no optional attributes
