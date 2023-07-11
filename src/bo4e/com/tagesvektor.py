"""
Contains Tagesvektor class and corresponding marshmallow schema for de-/serialization
"""
import datetime
from typing import Annotated

from annotated_types import Len

from bo4e.com.com import COM
from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


class Tagesvektor(COM):
    """
    Abbildung eines Tagesvektors eines beliebigen äquidistanten Zeitrasters

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tagesvektor.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tagesvektor JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Tagesvektor.json>`_

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
    werte: Annotated[list[Zeitreihenwertkompakt], Len(1)]
    """
    Die Werte am angegebenen Tag;
    In Kombination aus Zeitintervall und Tag lassen sich die Zeiten der Werte eindeutig konstruieren.
    """
