"""
Contains Lastgang class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..bo.marktlokation import Marktlokation
    from ..bo.messlokation import Messlokation
    from ..com.menge import Menge
    from ..com.zeitreihenwert import Zeitreihenwert
    from ..enum.mengeneinheit import Mengeneinheit
    from ..enum.sparte import Sparte


# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Lastgang(Geschaeftsobjekt):
    """
    Modell zur Abbildung eines Lastganges;
    In diesem Modell werden die Messwerte mit einem vollständigen Zeitintervall (zeit_intervall_laenge) angegeben und es bietet daher eine hohe Flexibilität in der Übertragung jeglicher zeitlich veränderlicher Messgrössen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Lastgang.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lastgang JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Lastgang.json>`_

    """

    typ: Annotated[Literal[Typ.LASTGANG], Field(alias="_typ")] = Typ.LASTGANG
    sparte: Optional["Sparte"] = None
    """Angabe, ob es sich um einen Gas- oder Stromlastgang handelt"""
    messgroesse: Optional["Mengeneinheit"] = None
    """Definition der gemessenen Größe anhand ihrer Einheit"""
    #:Marktlokation, zu der der Lastgang gehört
    marktlokation: Optional["Marktlokation"] = None
    #:Marktlokation, zu der der Lastgang gehört
    messlokation: Optional["Messlokation"] = None
    werte: Optional[list["Zeitreihenwert"]] = None
    """Die im Lastgang enthaltenen Messwerte"""
    version: Optional[str] = None
    """Versionsnummer des Lastgangs"""
    obis_kennzahl: Optional[str] = None
    """Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'"""
    zeit_intervall_laenge: Optional["Menge"]
