"""
Contains RegionaleGueltigkeit class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated

from annotated_types import Len

from bo4e.com.com import COM
from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp

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

    # required attributes
    gueltigkeitstyp: Gueltigkeitstyp  #: Unterscheidung ob Positivliste oder Negativliste übertragen wird
    kriteriums_werte: Annotated[
        list[KriteriumWert], Len(1)
    ]  #: Hier stehen die Kriterien, die die regionale Gültigkeit festlegen
