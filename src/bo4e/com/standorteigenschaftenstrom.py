"""
Contains StandorteigenschaftenStrom class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class StandorteigenschaftenStrom(COM):
    """
    Standorteigenschaften der Sparte Strom

    .. raw:: html

        <object data="../_static/images/bo4e/com/StandorteigenschaftenStrom.svg" type="image/svg+xml"></object>

    .. HINT::
        `StandorteigenschaftenStrom JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/StandorteigenschaftenStrom.json>`_

    """

    bilanzierungsgebiet_eic: Optional[str] = None
    """Die EIC-Nummer des Bilanzierungsgebietes"""
    # todo: use EIC validation: https://github.com/Hochfrequenz/BO4E-python/issues/147

    regelzone: Optional[str] = None
    """Der Name der Regelzone"""

    regelzone_eic: Optional[str] = None
    """De EIC-Nummer der Regelzone"""
    # todo: use EIC validation: https://github.com/Hochfrequenz/BO4E-python/issues/147
