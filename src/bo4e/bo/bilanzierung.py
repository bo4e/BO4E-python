"""
Bilanzierungsklasse
"""
from datetime import datetime
from typing import Optional

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.menge import Menge
from bo4e.enum.botyp import BoTyp


class Bilanzierung(Geschaeftsobjekt):
    """
    Object containing information about Bilanzierung i.e. accounting
    """


bo_typ: BoTyp = BoTyp.BILANZIERUNG  # added to botyp.py

# required attributes

# optional attributes
# Welche Marktlokation
marktlokations_id: Optional[str] = None
###
# todo: add marktlokations_id check?
# _marktlokations_id_check = field_validator("marktlokations_id")(validate_marktlokations_id)
###
# Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.)
lastprofil: list[Optional[Lastprofil]] = []  # messgroesse?
# Inklusiver Start der Bilanzierung
bilanzierungsbeginn: Optional[datetime] = None
# Exklusives Ende der Bilanzierung
bilanzierungsende: Optional[datetime] = None
# todo: add tests?

# Bilanzkreis
bilanzkreis: Optional[str] = None
# Jahresverbrauchsprognose
jahresverbrauchsprognose: Optional[Menge] = None
# Temperatur Arbeit
temperatur_arbeit: Optional[Menge] = None
# Kundenwert
kundenwert: Optional[Menge] = None
"""
   <summary>
          Verbrauchsaufteilung in % zwischen SLP und TLP-Profil
          1. [Gemessene Energiemenge der OBIS "nicht Schwachlast"] * [Verbrauchsaufteilung in % / 100%] 
             = [zu verlagernde Energiemenge]
          2. [Gemessene Energiemenge der OBIS "Schwachlast"] - [zu verlagernde Energiemenge] 
             = [Ermittelte Energiemenge für Schwachlast]
          3. [Gemessene Energiemenge der OBIS "nicht Schwachlast"] + [zu verlagernde Energiemenge] 
             = [Ermittelte Energiemenge für nicht Schwachlast]
    </summary>
"""
verbrauchsaufteilung: Optional[float] = None  # double precision in python
# Zeitreihentyp (SLS, TLS, etc.)
zeitreihentyp: Optional[Zeitreihentyp] = None  # enum
# Aggregationsverantwortung
aggregationsverantwortung: Optional[Aggregationsverantwortung] = None  # enum
# Prognosegrundlage
prognosegrundlage: Optional[Prognosegrundlage] = None  # enum
"""
     Prognosegrundlage
        Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben,
        so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich.
"""
details_prognosegrundlage: list[Optional[Profiltyp]] = []  # enum
# Wahlrecht der Prognosegrundlage (true = Wahlrecht beim Lieferanten vorhanden)
wahlrecht_prognosegrundlage: Optional[WahlrechtPrognosegrundlage] = None  # enum
# Fallgruppenzuordnung (für gas RLM)
fallgruppenzuordnung: Optional[Fallgruppenzuordnung] = None  # enum
# Priorität des Bilanzkreises (für Gas)
prioritaet: Optional[int] = None
# Grund Wahlrecht der Prognosegrundlage(true=Wahlrecht beim Lieferanten vorhanden)
grund_wahlrechts_prognosegrundlage: Optional[WahlrechtsPrognosegrundlage] = None  # enum
