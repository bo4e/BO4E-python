"""
Contains Zeitreihe class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional


from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.zeitreihenwert import Zeitreihenwert
from bo4e.enum.botyp import BoTyp
from bo4e.enum.medium import Medium
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.messart import Messart
from bo4e.enum.messgroesse import Messgroesse
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren


# pylint: disable=too-few-public-methods, too-many-instance-attributes
from pydantic import conlist, StrictStr


class Zeitreihe(Geschaeftsobjekt):
    """
    Abbildung einer allgemeinen Zeitreihe mit einem Wertvektor.
    Die Werte können mit wahlfreier zeitlicher Distanz im Vektor abgelegt sein.

    .. HINT::
        `Zeitreihe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/ZeitreiheSchema.json>`_

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
    werte: conlist(Zeitreihenwert, min_items=1)

    # optional attributes
    #: Beschreibt die Verwendung der Zeitreihe
    beschreibung: str = None
    #: Version der Zeitreihe
    version: str = None
    #: Kennzeichnung, wie die Werte entstanden sind, z.B. durch Messung
    wertherkunft: Wertermittlungsverfahren = None
