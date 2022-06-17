"""
Contains Tarifpreisposition class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional


from bo4e.com.com import COM
from bo4e.com.preisstaffel import Preisstaffel
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit


# pylint: disable=too-few-public-methods
from pydantic import conlist


class Tarifpreisposition(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden.

    .. HINT::
        `Tarifpreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TarifpreispositionSchema.json>`_

    """

    # required attributes
    #: Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Preistyp
    #: Einheit des Preises (z.B. EURO)
    einheit: Waehrungseinheit
    #: Größe, auf die sich die Einheit bezieht, beispielsweise kWh, Jahr
    bezugseinheit: Mengeneinheit
    #: Hier sind die Staffeln mit ihren Preisenangaben definiert
    preisstaffeln: conlist(Preisstaffel, min_items=1)

    # optional attributes
    #: Gibt an, nach welcher Menge die vorgenannte Einschränkung erfolgt (z.B. Jahresstromverbrauch in kWh)
    mengeneinheitstaffel: Mengeneinheit = None
