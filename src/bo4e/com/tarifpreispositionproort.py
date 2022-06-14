"""
Contains TarifpreispositionProOrt class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List


from marshmallow import fields

from bo4e.com.com import COM
from bo4e.com.tarifpreisstaffelproort import TarifpreisstaffelProOrt
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
from pydantic import constr, conlist


class TarifpreispositionProOrt(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden

    .. HINT::
        `TarifpreispositionProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TarifpreispositionProOrtSchema.json>`_

    """

    # required attributes
    #: Postleitzahl des Ortes für den der Preis gilt
    postleitzahl: constr(regex=r"^\d{5}$")
    #: Ort für den der Preis gilt
    ort: str
    #: ene't-Netznummer des Netzes in dem der Preis gilt
    netznr: str
    # Hier sind die Staffeln mit ihren Preisenangaben definiert
    preisstaffeln: conlist(TarifpreisstaffelProOrt, min_items=1)
    # there are no optional attributes
