"""
Contains Lastgang and LastgangKompakt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional


from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.tagesvektor import Tagesvektor
from bo4e.com.zeitintervall import Zeitintervall
from bo4e.com.zeitreihenwert import Zeitreihenwert
from bo4e.enum.botyp import BoTyp
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from bo4e.validators import OBIS_PATTERN


# pylint: disable=too-few-public-methods
from pydantic import constr, conlist


class _LastgangBody(Geschaeftsobjekt):
    """
    The LastgangBody is a mixin that contains the "body" of a Lastgang that is used in both the :class:`Lastgang` as
    well as :class:`LastgangKompakt`.
    """

    #: Angabe, ob es sich um einen Gas- oder Stromlastgang handelt
    sparte: Sparte

    #: Eindeutige Nummer der Marktlokation bzw der Messlokation, zu der der Lastgang gehört
    lokations_id: str

    #: Marktlokation oder Messlokation
    lokationstyp: str
    # todo: implement a lokations-id + lokationstyp cross check (such that lokationstyp malo checks for valid malo id)
    # https://github.com/Hochfrequenz/BO4E-python/issues/321

    #: Definition der gemessenen Größe anhand ihrer Einheit
    messgroesse: Mengeneinheit

    # optional attributes
    #: Versionsnummer des Lastgangs
    version: str = None
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    obis_kennzahl: constr(regex=OBIS_PATTERN) = None


# pylint: disable=too-many-instance-attributes, too-few-public-methods


class LastgangKompakt(_LastgangBody):
    """
    Modell zur Abbildung eines kompakten Lastganges.
    In diesem Modell werden die Messwerte in Form von Tagesvektoren mit fester Anzahl von Werten übertragen.
    Daher ist dieses BO nur zur Übertragung von äquidistanten Messwertverläufen geeignet.
    """

    # required attributes
    bo_typ: BoTyp = BoTyp.LASTGANG_KOMPAKT

    #: Angabe des Rasters innerhalb aller Tagesvektoren dieses Lastgangs
    zeitintervall: Zeitintervall
    # todo: implement a cross check that this zeitintervall is actually the one used in tagesvektoren
    # https://github.com/Hochfrequenz/BO4E-python/issues/322

    #: Die im Lastgang enthaltenen Messwerte in Form von Tagesvektoren
    tagesvektoren: List[Tagesvektor]


# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Lastgang(_LastgangBody):
    """
    Modell zur Abbildung eines Lastganges;
    In diesem Modell werden die Messwerte mit einem vollständigen Zeitintervall angegeben und es bietet daher eine hohe
    Flexibilität in der Übertragung jeglicher zeitlich veränderlicher Messgrössen.

    .. HINT::
        `Lastgang JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/LastgangSchema.json>`_"

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.LASTGANG

    #: Die im Lastgang enthaltenen Messwerte
    werte: conlist(Zeitreihenwert, min_items=1)
