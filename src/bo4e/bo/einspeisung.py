"""
Contains Buendelvertrag class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Optional

from ..enum.eeg_vermarktungsform import EEGVermarktungsform
from ..enum.fernsteuerbarkeit_status import FernsteuerbarkeitStatus
from ..enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from ..enum.landescode import Landescode
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt


@postprocess_docstring
class Einspeisung(Geschaeftsobjekt):
    """
    Abbildung der Einspeisung.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Einspeisung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Einspeisung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Einspeisung.json>`_

    """

    marktlokations_id: Optional[str] = None

    tranchen_id: Optional[str] = None

    verguetungsempfaenger: Optional[Geschaeftspartnerrolle] = None

    eeg_vermarktungsform: Optional[EEGVermarktungsform] = None

    landescode: Optional[Landescode] = None

    fernsteuerbarkeit_status: Optional[FernsteuerbarkeitStatus] = None
