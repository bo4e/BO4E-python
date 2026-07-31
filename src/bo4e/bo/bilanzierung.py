"""
Contains class Bilanzierung
"""

from datetime import datetime
from decimal import Decimal
from typing import Annotated

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

    typ: Annotated[BoTyp | None, Field(alias="_typ")] = BoTyp.BILANZIERUNG

    marktlokations_id: str | None = None  #:  ID der Marktlokation
    lastprofil: list[Lastprofil] | None = None  #: Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.)
    bilanzierungsbeginn: datetime | None = None  #: Inklusiver Start der Bilanzierung
    bilanzierungsende: datetime | None = None  #: Exklusives Ende der Bilanzierung
    bilanzkreis: str | None = None  #: Bilanzkreis
    jahresverbrauchsprognose: Menge | None = None  #: Jahresverbrauchsprognose
    temperatur_arbeit: Menge | None = None  #: Temperatur Arbeit
    kundenwert: Menge | None = None  #: Kundenwert
    verbrauchsaufteilung: Decimal | None = None
    """
    Verbrauchsaufteilung in % zwischen SLP und TLP-Profil.

    1. [Gemessene Energiemenge der OBIS "nicht Schwachlast"] * [Verbrauchsaufteilung in % / 100%]
    = [zu verlagernde Energiemenge]
    2. [Gemessene Energiemenge der OBIS "Schwachlast"] - [zu verlagernde Energiemenge]
    = [Ermittelte Energiemenge für Schwachlast]
    3. [Gemessene Energiemenge der OBIS "nicht Schwachlast"] + [zu verlagernde Energiemenge]
    = [Ermittelte Energiemenge für nicht Schwachlast]
    """
    zeitreihentyp: Zeitreihentyp | None = None  #: Zeitreihentyp (SLS, TLS, etc.)
    aggregationsverantwortung: Aggregationsverantwortung | None = None  #: Aggregationsverantwortung
    prognosegrundlage: Prognosegrundlage | None = None  #: Prognosegrundlage
    details_prognosegrundlage: list[Profiltyp] | None = None
    """
    Prognosegrundlage.

    Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben,
    so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich.
    """
    wahlrecht_prognosegrundlage: WahlrechtPrognosegrundlage | None = None
    """
    Wahlrecht der Prognosegrundlage.
    """
    fallgruppenzuordnung: Fallgruppenzuordnung | None = None  #: Fallgruppenzuordnung (für gas RLM)
    prioritaet: int | None = None  #: Priorität des Bilanzkreises (für Gas)
    grund_wahlrecht_prognosegrundlage: WahlrechtPrognosegrundlage | None = None
    """
    Grund Wahlrecht der Prognosegrundlage.

    true=Wahlrecht beim Lieferanten vorhanden
    """
    abwicklungsmodell: Abwicklungsmodell | None = None  #: Abwicklungsmodell
