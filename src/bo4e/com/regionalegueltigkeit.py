"""
Contains RegionaleGueltigkeit class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List


from bo4e.com.com import COM
from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp


# pylint: disable=too-few-public-methods
from pydantic import conlist


class RegionaleGueltigkeit(COM):
    """
    Mit dieser Komponente können regionale Gültigkeiten, z.B. für Tarife, Zu- und Abschläge und Preise definiert werden.

    .. HINT::
        `RegionaleGueltigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionaleGueltigkeitSchema.json>`_

    """

    # required attributes
    gueltigkeitstyp: Gueltigkeitstyp  #: Unterscheidung ob Positivliste oder Negativliste übertragen wird
    kriteriums_werte: conlist(
        KriteriumWert, min_items=1
    )  #:  Hier stehen die Kriterien, die die regionale Gültigkeit festlegen
