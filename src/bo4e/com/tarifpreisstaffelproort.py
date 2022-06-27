"""
Contains TarifpreisstaffelProOrt class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


class TarifpreisstaffelProOrt(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. graphviz:: /api/dots/bo4e/com/TarifpreisstaffelProOrt.dot

    """

    # todo: decimal doesn't make sense here imo
    # https://github.com/Hochfrequenz/BO4E-python/issues/344

    # required attributes
    #: Der Arbeitspreis in ct/kWh
    arbeitspreis: Decimal
    #: Der Arbeitspreis für Verbräuche in der Niedertarifzeit in ct/kWh
    arbeitspreis_n_t: Decimal
    #: Der Grundpreis in Euro/Jahr
    grundpreis: Decimal
    #: Unterer Wert, ab dem die Staffel gilt (inklusive)
    staffelgrenze_von: Decimal
    #: Oberer Wert, bis zu dem die Staffel gilt (exklusive)
    staffelgrenze_bis: Decimal

    # there are no optional attributes
