"""
Contains RegionaleGueltigkeit class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..enum.gueltigkeitstyp import Gueltigkeitstyp
from .com import COM
from .kriteriumwert import KriteriumWert

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


class RegionaleGueltigkeit(COM):
    """
    Mit dieser Komponente können regionale Gültigkeiten, z.B. für Tarife, Zu- und Abschläge und Preise definiert werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionaleGueltigkeit.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionaleGueltigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionaleGueltigkeit.json>`_

    """

    gueltigkeitstyp: Optional[
        Gueltigkeitstyp
    ] = None  #: Unterscheidung ob Positivliste oder Negativliste übertragen wird
    kriteriums_werte: Optional[
        list[KriteriumWert]
    ] = None  #: Hier stehen die Kriterien, die die regionale Gültigkeit festlegen
