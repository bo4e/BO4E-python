"""
Contains Lastgang and LastgangKompakt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import Field, constr

from ..com.tagesvektor import Tagesvektor
from ..com.zeitintervall import Zeitintervall
from ..com.zeitreihenwert import Zeitreihenwert
from ..enum.mengeneinheit import Mengeneinheit
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from .geschaeftsobjekt import Geschaeftsobjekt


class _LastgangBody(Geschaeftsobjekt):
    """
    The LastgangBody is a mixin that contains the "body" of a Lastgang that is used in both the :class:`Lastgang` as
    well as :class:`LastgangKompakt`.
    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = None
    # I don't know why, but without this line mypy complains in LastgangKompakt about:
    # Incompatible types in assignment (expression has type "Typ | None", base class "_LastgangBody" defined
    # the type as "Typ")  [assignment]

    #: Angabe, ob es sich um einen Gas- oder Stromlastgang handelt
    sparte: Optional[Sparte] = None

    #: Eindeutige Nummer der Marktlokation bzw der Messlokation, zu der der Lastgang gehört
    lokations_id: Optional[str] = None

    #: Marktlokation oder Messlokation
    lokationstyp: Optional[str] = None
    # todo: implement a lokations-id + lokationstyp cross check (such that lokationstyp malo checks for valid malo id)
    # https://github.com/Hochfrequenz/BO4E-python/issues/321

    #: Definition der gemessenen Größe anhand ihrer Einheit
    messgroesse: Optional[Mengeneinheit] = None

    #: Versionsnummer des Lastgangs
    version: Optional[str] = None
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    obis_kennzahl: Optional[constr(strict=True)] = None  # type: ignore[valid-type]


# pylint: disable=too-many-instance-attributes, too-few-public-methods


class LastgangKompakt(_LastgangBody):
    """
    Modell zur Abbildung eines kompakten Lastganges.
    In diesem Modell werden die Messwerte in Form von Tagesvektoren mit fester Anzahl von Werten übertragen.
    Daher ist dieses BO nur zur Übertragung von äquidistanten Messwertverläufen geeignet.
    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.LASTGANG_KOMPAKT

    #: Angabe des Rasters innerhalb aller Tagesvektoren dieses Lastgangs
    zeitintervall: Optional[Zeitintervall] = None
    # todo: implement a cross check that this zeitintervall is actually the one used in tagesvektoren
    # https://github.com/Hochfrequenz/BO4E-python/issues/322

    #: Die im Lastgang enthaltenen Messwerte in Form von Tagesvektoren
    tagesvektoren: Optional[list[Tagesvektor]] = None


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

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.LASTGANG

    #: Die im Lastgang enthaltenen Messwerte
    werte: Optional[list[Zeitreihenwert]] = None
