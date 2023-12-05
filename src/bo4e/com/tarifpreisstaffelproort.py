"""
Contains TarifpreisstaffelProOrt class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

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
        `TarifpreisstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/TarifpreisstaffelProOrt.json>`_

    """

    # todo: decimal doesn't make sense here imo
    # https://github.com/Hochfrequenz/BO4E-python/issues/344

    #: Der Arbeitspreis in ct/kWh
    arbeitspreis: Optional[Decimal] = None
    #: Der Arbeitspreis für Verbräuche in der Niedertarifzeit in ct/kWh
    arbeitspreis_n_t: Optional[Decimal] = None
    #: Der Grundpreis in Euro/Jahr
    grundpreis: Optional[Decimal] = None
    #: Unterer Wert, ab dem die Staffel gilt (inklusive)
    staffelgrenze_von: Optional[Decimal] = None
    #: Oberer Wert, bis zu dem die Staffel gilt (exklusive)
    staffelgrenze_bis: Optional[Decimal] = None

    # there are no optional attributes
