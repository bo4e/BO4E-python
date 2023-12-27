"""
Contains Zeitreihe class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from pydantic import Field

from ..com.zeitreihenwert import Zeitreihenwert
from ..enum.medium import Medium
from ..enum.mengeneinheit import Mengeneinheit
from ..enum.messart import Messart
from ..enum.messgroesse import Messgroesse
from ..enum.typ import Typ
from ..enum.wertermittlungsverfahren import Wertermittlungsverfahren
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt


@postprocess_docstring
class Zeitreihe(Geschaeftsobjekt):
    """
    Abbildung einer allgemeinen Zeitreihe mit einem Wertvektor.
    Die Werte können mit wahlfreier zeitlicher Distanz im Vektor abgelegt sein.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zeitreihe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Zeitreihe.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.ZEITREIHE
    #: Bezeichnung für die Zeitreihe
    bezeichnung: Optional[str] = None
    #: Beschreibt, was gemessen wurde (z.B. Strom, Spannung, Wirkleistung, Scheinleistung)
    messgroesse: Optional[Messgroesse] = None
    #: Beschreibt die Art der Messung (z.B. aktueller Wert, mittlerer Wert, maximaler Wert)
    messart: Optional[Messart] = None
    #: Medium, das gemessen wurde (z.B. Wasser, Dampf, Strom, Gas)
    medium: Optional[Medium] = None
    #: Alle Werte in der Tabelle haben die Einheit, die hier angegeben ist
    einheit: Optional[Mengeneinheit] = None
    #: Hier liegen jeweils die Werte
    werte: Optional[list[Zeitreihenwert]] = None

    #: Beschreibt die Verwendung der Zeitreihe
    beschreibung: Optional[str] = None
    #: Version der Zeitreihe
    version: Optional[str] = None
    #: Kennzeichnung, wie die Werte entstanden sind, z.B. durch Messung
    wertherkunft: Optional[Wertermittlungsverfahren] = None
