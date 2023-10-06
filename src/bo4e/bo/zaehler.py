"""
Contains Zaehler class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal

# pylint: disable=unused-argument
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from pydantic import Field

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.zaehlwerk import Zaehlwerk
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.typ import Typ
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

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.ZAEHLER
    zaehlernummer: Optional[str] = None  #: Nummerierung des Zählers,vergeben durch den Messstellenbetreiber
    sparte: Optional[Sparte] = None  #: Strom oder Gas
    zaehlerauspraegung: Optional[Zaehlerauspraegung] = None  #: Spezifikation die Richtung des Zählers betreffend
    zaehlertyp: Optional[Zaehlertyp] = None  #: Typisierung des Zählers
    zaehlwerke: Optional[list[Zaehlwerk]] = None
    tarifart: Optional[Tarifart] = None  #: Spezifikation bezüglich unterstützter Tarifarten

    zaehlerkonstante: Optional[Decimal] = None  #: Zählerkonstante auf dem Zähler
    eichung_bis: Optional[datetime] = None  #: Bis zu diesem Datum (exklusiv) ist der Zähler geeicht.
    letzte_eichung: Optional[datetime] = None  #: Zu diesem Datum fand die letzte Eichprüfung des Zählers statt.
    zaehlerhersteller: Optional[Geschaeftspartner] = None  #: Der Hersteller des Zählers
