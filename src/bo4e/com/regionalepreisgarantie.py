"""
Contains RegionalePreisgarantie class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .preisgarantie import Preisgarantie

if TYPE_CHECKING:
    from .regionalegueltigkeit import RegionaleGueltigkeit

# pylint: disable=too-few-public-methods


@postprocess_docstring
class RegionalePreisgarantie(Preisgarantie):
    """
    Abbildung einer Preisgarantie mit regionaler Abgrenzung

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalePreisgarantie.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalePreisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/RegionalePreisgarantie.json>`_

    """

    #: Regionale Eingrenzung der Preisgarantie.
    regionale_gueltigkeit: Optional["RegionaleGueltigkeit"] = None
