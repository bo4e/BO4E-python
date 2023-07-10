"""
Contains Lastgang and LastgangKompakt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, List, Optional

from annotated_types import Len

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import constr

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.tagesvektor import Tagesvektor
from bo4e.com.zeitintervall import Zeitintervall
from bo4e.com.zeitreihenwert import Zeitreihenwert
from bo4e.enum.botyp import BoTyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from bo4e.validators import OBIS_PATTERN


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
    version: Optional[str] = None
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    obis_kennzahl: Optional[constr(strict=True, pattern=OBIS_PATTERN)] = None  # type: ignore[valid-type]


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

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Lastgang.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lastgang JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Lastgang.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.LASTGANG

    #: Die im Lastgang enthaltenen Messwerte
    werte: Annotated[list[Zeitreihenwert], Len(1)]
