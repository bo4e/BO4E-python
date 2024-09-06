"""
Contains Buendelvertrag class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Optional

import pydantic
from pydantic import Field

from ..enum.eeg_vermarktungsform import EEGVermarktungsform
from ..enum.fernsteuerbarkeit_status import FernsteuerbarkeitStatus
from ..enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from ..enum.landescode import Landescode
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt


@postprocess_docstring
class Einspeisung(Geschaeftsobjekt):
    """
    Abbildung eines Bündelvertrags.
    Es handelt sich hierbei um eine Liste von Einzelverträgen, die in einem Vertragsobjekt gebündelt sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Buendelvertrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Buendelvertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Buendelvertrag.json>`_

    """

    MarktlokationsId: Optional[str] = None

    Verguetungsempfaenger: Optional[Geschaeftspartnerrolle] = None

    EEGVermarktungsform: Optional[EEGVermarktungsform] = None

    Landescode: Optional[Landescode] = None

    FernsteuerbarkeitStatus: Optional[FernsteuerbarkeitStatus] = None
