"""
Contains Zeitintervall class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.enum.zeiteinheit import Zeiteinheit


# pylint: disable=too-few-public-methods


class Zeitintervall(COM):
    """
    Abbildung für ein Zeitintervall. Die Abbildung eines Zeitintervalls.
    Z.B. zur Anwendung als Raster in äquidistanten Zeitreihen/Lastgängen, beispielsweise 15 Minuten.

    .. graphviz:: /api/dots/bo4e/com/Zeitintervall.dot

    """

    # required attributes
    wert: int
    """
    Die Anzahl der Zeiteinheiten innerhalb  des Intervalls
    """
    zeiteinheit: Zeiteinheit
    """
    Die Einheit des Zeitintervalls
    """
