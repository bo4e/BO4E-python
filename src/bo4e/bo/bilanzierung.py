"""
Contains class Bilanzierung
"""

from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional

from pydantic import Field

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.lastprofil import Lastprofil
from bo4e.com.menge import Menge
from bo4e.enum.aggregationsverantwortung import Aggregationsverantwortung
from bo4e.enum.fallgruppenzuordnung import Fallgruppenzuordnung
from bo4e.enum.profiltyp import Profiltyp
from bo4e.enum.prognosegrundlage import Prognosegrundlage
from bo4e.enum.wahlrechtprognosegrundlage import WahlrechtPrognosegrundlage
from bo4e.enum.zeitreihentyp import Zeitreihentyp

from ..enum.abwicklungsmodell import Abwicklungsmodell
from ..enum.botyp import BoTyp


class Bilanzierung(Geschaeftsobjekt):
    """
    Das BO Bilanzierung erfasst alle relevanten Informationen zur Bilanzierung.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Bilanzierung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lastprofil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Bilanzierung.json>`_

    """

    typ: Annotated[Optional[BoTyp], Field(alias="_typ")] = BoTyp.BILANZIERUNG

    marktlokations_id: Optional[str] = None  #:  ID der Marktlokation
    lastprofil: Optional[list[Lastprofil]] = None  #: Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.)
    bilanzierungsbeginn: Optional[datetime] = None  #: Inklusiver Start der Bilanzierung
    bilanzierungsende: Optional[datetime] = None  #: Exklusives Ende der Bilanzierung
    bilanzkreis: Optional[str] = None  #: Bilanzkreis
    jahresverbrauchsprognose: Optional[Menge] = None  #: Jahresverbrauchsprognose
    temperatur_arbeit: Optional[Menge] = None  #: Temperatur Arbeit
    kundenwert: Optional[Menge] = None  #: Kundenwert
    verbrauchsaufteilung: Optional[Decimal] = None
    """
    Verbrauchsaufteilung in % zwischen SLP und TLP-Profil.

    1. [Gemessene Energiemenge der OBIS "nicht Schwachlast"] * [Verbrauchsaufteilung in % / 100%]
    = [zu verlagernde Energiemenge]
    2. [Gemessene Energiemenge der OBIS "Schwachlast"] - [zu verlagernde Energiemenge]
    = [Ermittelte Energiemenge für Schwachlast]
    3. [Gemessene Energiemenge der OBIS "nicht Schwachlast"] + [zu verlagernde Energiemenge]
    = [Ermittelte Energiemenge für nicht Schwachlast]
    """
    zeitreihentyp: Optional[Zeitreihentyp] = None  #: Zeitreihentyp (SLS, TLS, etc.)
    aggregationsverantwortung: Optional[Aggregationsverantwortung] = None  #: Aggregationsverantwortung
    prognosegrundlage: Optional[Prognosegrundlage] = None  #: Prognosegrundlage
    details_prognosegrundlage: Optional[list[Profiltyp]] = None
    """
    Prognosegrundlage.

    Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben,
    so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich.
    """
    wahlrecht_prognosegrundlage: Optional[WahlrechtPrognosegrundlage] = None
    """
    Wahlrecht der Prognosegrundlage.
    """
    fallgruppenzuordnung: Optional[Fallgruppenzuordnung] = None  #: Fallgruppenzuordnung (für gas RLM)
    prioritaet: Optional[int] = None  #: Priorität des Bilanzkreises (für Gas)
    grund_wahlrecht_prognosegrundlage: Optional[WahlrechtPrognosegrundlage] = None
    """
    Grund Wahlrecht der Prognosegrundlage.

    true=Wahlrecht beim Lieferanten vorhanden
    """
    abwicklungsmodell: Optional[Abwicklungsmodell] = None  #: Abwicklungsmodell
