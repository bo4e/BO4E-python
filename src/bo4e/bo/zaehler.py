"""
Contains Zaehler class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal

# pylint: disable=unused-argument
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from annotated_types import Len

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.zaehlwerk import Zaehlwerk
from bo4e.enum.botyp import BoTyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.zaehlerauspraegung import Zaehlerauspraegung
from bo4e.enum.zaehlertyp import Zaehlertyp

# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Zaehler(Geschaeftsobjekt):
    """
    Object containing information about a meter/"Zaehler".

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zaehler.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehler JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Zaehler.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.ZAEHLER
    zaehlernummer: str  #: Nummerierung des Zählers,vergeben durch den Messstellenbetreiber
    sparte: Sparte  #: Strom oder Gas
    zaehlerauspraegung: Zaehlerauspraegung  #: Spezifikation die Richtung des Zählers betreffend
    zaehlertyp: Zaehlertyp  #: Typisierung des Zählers
    zaehlwerke: Annotated[list[Zaehlwerk], Len(1)]
    tarifart: Tarifart  #: Spezifikation bezüglich unterstützter Tarifarten

    # optional attributes
    zaehlerkonstante: Optional[Decimal] = None  #: Zählerkonstante auf dem Zähler
    eichung_bis: Optional[datetime] = None  #: Bis zu diesem Datum (exklusiv) ist der Zähler geeicht.
    letzte_eichung: Optional[datetime] = None  #: Zu diesem Datum fand die letzte Eichprüfung des Zählers statt.
    zaehlerhersteller: Optional[Geschaeftspartner] = None  #: Der Hersteller des Zählers
