"""
Contains TarifpreisstaffelProOrt class
"""

from decimal import Decimal
from typing import Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class TarifpreisstaffelProOrt(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. raw:: html

        <object data="../_static/images/bo4e/com/TarifpreisstaffelProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `TarifpreisstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/TarifpreisstaffelProOrt.json>`_

    """

    typ: Annotated[Literal[ComTyp.TARIFPREISSTAFFELPROORT], Field(alias="_typ")] = ComTyp.TARIFPREISSTAFFELPROORT

    # todo: decimal doesn't make sense here imo
    # https://github.com/Hochfrequenz/BO4E-python/issues/344

    arbeitspreis: Optional[Decimal] = None
    """Der Arbeitspreis in ct/kWh"""
    arbeitspreis_n_t: Optional[Decimal] = None
    """Der Arbeitspreis für Verbräuche in der Niedertarifzeit in ct/kWh"""
    grundpreis: Optional[Decimal] = None
    """Der Grundpreis in Euro/Jahr"""
    staffelgrenze_von: Optional[Decimal] = None
    """Unterer Wert, ab dem die Staffel gilt (inklusive)"""
    staffelgrenze_bis: Optional[Decimal] = None
    """Oberer Wert, bis zu dem die Staffel gilt (exklusive)"""

    # there are no optional attributes
