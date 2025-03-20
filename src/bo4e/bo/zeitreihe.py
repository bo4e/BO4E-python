"""
Contains Zeitreihe class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.zeitreihenwert import Zeitreihenwert
    from ..enum.medium import Medium
    from ..enum.mengeneinheit import Mengeneinheit
    from ..enum.messart import Messart
    from ..enum.messgroesse import Messgroesse
    from ..enum.wertermittlungsverfahren import Wertermittlungsverfahren


@postprocess_docstring
class Zeitreihe(Geschaeftsobjekt):
    """
    Abbildung einer allgemeinen Zeitreihe mit einem Wertvektor.
    Die Werte können mit wahlfreier zeitlicher Distanz im Vektor abgelegt sein.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zeitreihe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Zeitreihe.json>`_

    """

    typ: Annotated[Literal[Typ.ZEITREIHE], Field(alias="_typ")] = Typ.ZEITREIHE
    bezeichnung: Optional[str] = None
    """Bezeichnung für die Zeitreihe"""
    messgroesse: Optional["Messgroesse"] = None
    """Beschreibt, was gemessen wurde (z.B. Strom, Spannung, Wirkleistung, Scheinleistung)"""
    messart: Optional["Messart"] = None
    """Beschreibt die Art der Messung (z.B. aktueller Wert, mittlerer Wert, maximaler Wert)"""
    medium: Optional["Medium"] = None
    """Medium, das gemessen wurde (z.B. Wasser, Dampf, Strom, Gas)"""
    einheit: Optional["Mengeneinheit"] = None
    """Alle Werte in der Tabelle haben die Einheit, die hier angegeben ist"""
    werte: Optional[list["Zeitreihenwert"]] = None
    """Hier liegen jeweils die Werte"""

    beschreibung: Optional[str] = None
    """Beschreibt die Verwendung der Zeitreihe"""
    version: Optional[str] = None
    """Version der Zeitreihe"""
    wertherkunft: Optional["Wertermittlungsverfahren"] = None
    """Kennzeichnung, wie die Werte entstanden sind, z.B. durch Messung"""
