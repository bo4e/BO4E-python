"""
Contains RegionalePreisstaffel class and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..utils import postprocess_docstring
from .preisstaffel import Preisstaffel
from .regionalegueltigkeit import RegionaleGueltigkeit

# pylint: disable=too-few-public-methods


@postprocess_docstring
class RegionalePreisstaffel(Preisstaffel):
    """
    Abbildung einer Preisstaffel mit regionaler Abgrenzung

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalePreisstaffel.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalePreisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/RegionalePreisstaffel.json>`_

    """

    #: Regionale Eingrenzung der Preisstaffel
    regionale_gueltigkeit: Optional[RegionaleGueltigkeit] = None
