"""
Contains Lastgang and LastgangKompakt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import constr

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.marktlokation import Marktlokation
from bo4e.bo.messlokation import Messlokation
from bo4e.com.tagesvektor import Tagesvektor
from bo4e.com.zeitintervall import Zeitintervall
from bo4e.com.zeitreihenwert import Zeitreihenwert
from bo4e.enum.botyp import BoTyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte

# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Lastgang(Geschaeftsobjekt):
    """
    Modell zur Abbildung eines Lastganges;
    #todo:update docstring

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Lastgang.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lastgang JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Lastgang.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.LASTGANG

    #: Angabe, ob es sich um einen Gas- oder Stromlastgang handelt
    sparte: Optional[Sparte] = None
    #: Definition der gemessenen Größe anhand ihrer Einheit
    messgroesse: Optional[Mengeneinheit] = None
    #:Marktlokation, zu der der Lastgang gehört
    marktlokation: Optional[Marktlokation] = None
    #:Marktlokation, zu der der Lastgang gehört
    messlokation: Optional[Messlokation] = None
    #: Die im Lastgang enthaltenen Messwerte
    werte: Optional[list[Zeitreihenwert]] = None
    #: Versionsnummer des Lastgangs
    version: Optional[str] = None
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    obis_kennzahl: Optional[constr(strict=True)] = None  # type: ignore[valid-type]
    # todo:add zeit_intervall_laenge
    # todo: add COMS Zeitspanne und Menge delete Zeitintervall
    # todo:delete tagesvektor
