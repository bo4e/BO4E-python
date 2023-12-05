"""
Contains AufAbschlagstaffelProOrt class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class AufAbschlagstaffelProOrt(COM):
    """
    Gibt den Wert eines Auf- oder Abschlags und dessen Staffelgrenzen an

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagstaffelProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/AufAbschlagstaffelProOrt.json>`_

    """

    #: Der Wert für den Auf- oder Abschlag.
    wert: Optional[Decimal] = None
    #: Unterer Wert, ab dem die Staffel gilt.
    staffelgrenze_von: Optional[Decimal] = None
    #: Oberer Wert, bis zu dem die Staffel gilt.
    staffelgrenze_bis: Optional[Decimal] = None
