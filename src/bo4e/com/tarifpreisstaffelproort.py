"""
Contains TarifpreisstaffelProOrt class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class TarifpreisstaffelProOrt(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. HINT::
        `TarifpreisstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TarifpreisstaffelProOrtSchema.json>`_

    """

    # todo: decimal doesn't make sense here imo
    # https://github.com/Hochfrequenz/BO4E-python/issues/344

    # required attributes
    #: Der Arbeitspreis in ct/kWh
    arbeitspreis: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    #: Der Arbeitspreis für Verbräuche in der Niedertarifzeit in ct/kWh
    arbeitspreis_n_t: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    #: Der Grundpreis in Euro/Jahr
    grundpreis: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    #: Unterer Wert, ab dem die Staffel gilt (inklusive)
    staffelgrenze_von: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    #: Oberer Wert, bis zu dem die Staffel gilt (exklusive)
    staffelgrenze_bis: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))

    # there are no optional attributes


class TarifpreisstaffelProOrtSchema(COMSchema):
    """
    Schema for (de)serialization of TarifpreisstaffelProOrt
    """

    class_name = TarifpreisstaffelProOrt

    # required attributes
    arbeitspreis = fields.Decimal(as_string=True)
    arbeitspreis_n_t = fields.Decimal(as_string=True, data_key="arbeitspreisNT")
    grundpreis = fields.Decimal(as_string=True)
    staffelgrenze_von = fields.Decimal(as_string=True, data_key="staffelgrenzeVon")
    staffelgrenze_bis = fields.Decimal(as_string=True, data_key="staffelgrenzeBis")
