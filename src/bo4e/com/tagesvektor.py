"""
Contains Tagesvektor class and corresponding marshmallow schema for de-/serialization
"""
import datetime
from typing import List


from bo4e.com.com import COM
from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt

# pylint: disable=too-few-public-methods
from pydantic import conlist


class Tagesvektor(COM):
    """
    Abbildung eines Tagesvektors eines beliebigen äquidistanten Zeitrasters

    .. HINT::
        `Tagesvektor JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/TagesvektorSchema.json>`_

    """

    # required attributes
    # for the validator see https://github.com/Hochfrequenz/BO4E-python/issues/261
    tag: datetime.datetime
    """
    Der Zeitpunkt ab dem die Werte ermittelt wurden.
    Es kann entweder der Beginn des Strom- oder Gastages verwendet werden.
    Der Zeitpunkt sollte eindeutig sein, d.h. sowohl Datum+Uhrzeit als auch den UTC-Offset spezifizieren.
    """
    # for the validator see also https://github.com/Hochfrequenz/BO4E-python/issues/262
    werte: conlist(Zeitreihenwertkompakt, min_items=1)
    """
    Die Werte am angegebenen Tag;
    In Kombination aus Zeitintervall und Tag lassen sich die Zeiten der Werte eindeutig konstruieren.
    """
