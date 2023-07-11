"""
Contains Zeitreihe class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from annotated_types import Len

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.zeitreihenwert import Zeitreihenwert
from bo4e.enum.botyp import BoTyp
from bo4e.enum.medium import Medium
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.messart import Messart
from bo4e.enum.messgroesse import Messgroesse
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren


class Zeitreihe(Geschaeftsobjekt):
    """
    Abbildung einer allgemeinen Zeitreihe mit einem Wertvektor.
    Die Werte können mit wahlfreier zeitlicher Distanz im Vektor abgelegt sein.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zeitreihe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Zeitreihe.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.ZEITREIHE
    #: Bezeichnung für die Zeitreihe
    bezeichnung: str
    #: Beschreibt, was gemessen wurde (z.B. Strom, Spannung, Wirkleistung, Scheinleistung)
    messgroesse: Messgroesse
    #: Beschreibt die Art der Messung (z.B. aktueller Wert, mittlerer Wert, maximaler Wert)
    messart: Messart
    #: Medium, das gemessen wurde (z.B. Wasser, Dampf, Strom, Gas)
    medium: Medium
    #: Alle Werte in der Tabelle haben die Einheit, die hier angegeben ist
    einheit: Mengeneinheit
    #: Hier liegen jeweils die Werte
    werte: Annotated[list[Zeitreihenwert], Len(1)]

    # optional attributes
    #: Beschreibt die Verwendung der Zeitreihe
    beschreibung: Optional[str] = None
    #: Version der Zeitreihe
    version: Optional[str] = None
    #: Kennzeichnung, wie die Werte entstanden sind, z.B. durch Messung
    wertherkunft: Optional[Wertermittlungsverfahren] = None
