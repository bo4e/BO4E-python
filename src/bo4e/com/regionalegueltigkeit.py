"""
Contains RegionaleGueltigkeit class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.com.com import COM
from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp


class RegionaleGueltigkeit(COM):
    """
    Mit dieser Komponente können regionale Gültigkeiten, z.B. für Tarife, Zu- und Abschläge und Preise definiert werden.

    .. graphviz:: /api/dots/bo4e/com/RegionaleGueltigkeit.dot

    """

    # required attributes
    gueltigkeitstyp: Gueltigkeitstyp  #: Unterscheidung ob Positivliste oder Negativliste übertragen wird
    kriteriums_werte: conlist(
        KriteriumWert, min_items=1
    )  #:  Hier stehen die Kriterien, die die regionale Gültigkeit festlegen
