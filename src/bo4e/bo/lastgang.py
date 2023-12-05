"""
Contains Lastgang class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import Field, constr

from ..bo.marktlokation import Marktlokation
from ..bo.messlokation import Messlokation
from ..com.menge import Menge
from ..com.zeitreihenwert import Zeitreihenwert
from ..enum.mengeneinheit import Mengeneinheit
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Lastgang(Geschaeftsobjekt):
    """
    Modell zur Abbildung eines Lastganges;
    In diesem Modell werden die Messwerte mit einem vollständigen Zeitintervall (zeit_intervall_laenge) angegeben und es bietet daher eine hohe Flexibilität in der Übertragung jeglicher zeitlich veränderlicher Messgrössen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Lastgang.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lastgang JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Lastgang.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.LASTGANG
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
    zeit_intervall_laenge: Optional[Menge]
