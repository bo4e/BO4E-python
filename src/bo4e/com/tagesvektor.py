"""
Contains Tagesvektor class and corresponding marshmallow schema for de-/serialization
"""
import datetime
from typing import List

import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema
from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt, ZeitreihenwertkompaktSchema

# pylint: disable=too-few-public-methods
from bo4e.validators import check_list_length_at_least_one


@attrs.define(auto_attribs=True, kw_only=True)
class Tagesvektor(COM):
    """
    Abbildung eines Tagesvektors eines beliebigen äquidistanten Zeitrasters

    .. HINT::
        `Tagesvektor JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TagesvektorSchema.json>`_

    """

    # required attributes
    # for the validator see https://github.com/Hochfrequenz/BO4E-python/issues/261
    tag: datetime.datetime = attrs.field(validator=attrs.validators.instance_of(datetime.datetime))
    """
    Der Zeitpunkt ab dem die Werte ermittelt wurden.
    Es kann entweder der Beginn des Strom- oder Gastages verwendet werden.
    Der Zeitpunkt sollte eindeutig sein, d.h. sowohl Datum+Uhrzeit als auch den UTC-Offset spezifizieren.
    """
    # for the validator see also https://github.com/Hochfrequenz/BO4E-python/issues/262
    # https://www.attrs.org/en/stable/api.html#attrs.validators.deep_iterable
    werte: List[Zeitreihenwertkompakt] = attrs.field(
        validator=[
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Zeitreihenwertkompakt),
                iterable_validator=attrs.validators.instance_of(list),
            ),
            check_list_length_at_least_one,
        ]
    )
    """
    Die Werte am angegebenen Tag;
    In Kombination aus Zeitintervall und Tag lassen sich die Zeiten der Werte eindeutig konstruieren.
    """


class TagesvektorSchema(COMSchema):
    """
    Schema for de-/serialization of Tagesvektor
    """

    class_name = Tagesvektor
    # required attributes
    tag = fields.DateTime()
    werte = fields.List(fields.Nested(ZeitreihenwertkompaktSchema))
