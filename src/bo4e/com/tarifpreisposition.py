"""
Contains Tarifpreisposition class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.com.com import COM
from bo4e.com.preisstaffel import Preisstaffel
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit


class Tarifpreisposition(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden.

    .. graphviz:: /api/dots/bo4e/com/Tarifpreisposition.dot

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
