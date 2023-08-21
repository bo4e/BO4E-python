"""
Contains class Bilanzierung
"""
from datetime import datetime
from typing import Optional

from pydantic import field_validator

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.lastprofil import Lastprofil
from bo4e.com.menge import Menge
from bo4e.enum.aggregationsverantwortung import Aggregationsverantwortung
from bo4e.enum.botyp import BoTyp
from bo4e.enum.fallgruppenzuordnung import Fallgruppenzuordnung
from bo4e.enum.profiltyp import Profiltyp
from bo4e.enum.prognosegrundlage import Prognosegrundlage
from bo4e.enum.wahlrechtprognosegrundlage import WahlrechtPrognosegrundlage
from bo4e.enum.zeitreihentyp import Zeitreihentyp
from bo4e.validators import validate_marktlokations_id


class Bilanzierung(Geschaeftsobjekt):
    """
    Bilanzierungs BO
    """

    bo_typ: BoTyp = BoTyp.BILANZIERUNG  # added to botyp.py

    # optional attributes
    #:  Welche Marktlokation
    marktlokations_id: Optional[str] = None

    # todo: optional/add marktlokations_id check?
    # _marktlokations_id_check = field_validator("marktlokations_id")(validate_marktlokations_id)

    #: Eine Liste der verwendeten Lastprofile (SLP, SLP/TLP, ALP etc.)
    lastprofil: list[Optional[Lastprofil]] = []
    #: Inklusiver Start der Bilanzierung
    bilanzierungsbeginn: Optional[datetime] = None
    #: Exklusives Ende der Bilanzierung
    bilanzierungsende: Optional[datetime] = None
    # todo: add tests?

    #: Bilanzkreis
    bilanzkreis: Optional[str] = None
    #: Jahresverbrauchsprognose
    jahresverbrauchsprognose: Optional[Menge] = None
    #: Temperatur Arbeit
    temperatur_arbeit: Optional[Menge] = None
    #: Kundenwert
    kundenwert: Optional[Menge] = None
    """
          Verbrauchsaufteilung in % zwischen SLP und TLP-Profil.
          
          1. [Gemessene Energiemenge der OBIS "nicht Schwachlast"] * [Verbrauchsaufteilung in % / 100%] 
             = [zu verlagernde Energiemenge]
          2. [Gemessene Energiemenge der OBIS "Schwachlast"] - [zu verlagernde Energiemenge] 
             = [Ermittelte Energiemenge für Schwachlast]
          3. [Gemessene Energiemenge der OBIS "nicht Schwachlast"] + [zu verlagernde Energiemenge] 
             = [Ermittelte Energiemenge für nicht Schwachlast]
    
    """
    verbrauchsaufteilung: Optional[float] = None
    #: Zeitreihentyp (SLS, TLS, etc.)
    zeitreihentyp: Optional[Zeitreihentyp] = None
    #: Aggregationsverantwortung
    aggregationsverantwortung: Optional[Aggregationsverantwortung] = None
    #: Prognosegrundlage
    prognosegrundlage: Optional[Prognosegrundlage] = None
    """
         Prognosegrundlage.
         
            Besteht der Bedarf ein tagesparameteräbhängiges Lastprofil mit gemeinsamer Messung anzugeben,
            so ist dies über die 2 -malige Wiederholung des CAV Segments mit der Angabe der Codes E02 und E14 möglich.
    """
    details_prognosegrundlage: list[Optional[Profiltyp]] = []
    #: Wahlrecht der Prognosegrundlage (true = Wahlrecht beim Lieferanten vorhanden)
    wahlrecht_prognosegrundlage: Optional[WahlrechtPrognosegrundlage] = None
    #: Fallgruppenzuordnung (für gas RLM)
    fallgruppenzuordnung: Optional[Fallgruppenzuordnung] = None
    #: Priorität des Bilanzkreises (für Gas)
    prioritaet: Optional[int] = None
    #: Grund Wahlrecht der Prognosegrundlage(true=Wahlrecht beim Lieferanten vorhanden)
    grund_wahlrecht_prognosegrundlage: Optional[WahlrechtPrognosegrundlage] = None

    @field_validator("marktlokations_id")
    @classmethod
    def _validate_malo_if_given(cls, marktlokations_id: Optional[str]) -> Optional[str]:
        if marktlokations_id is None:
            return marktlokations_id
        return validate_marktlokations_id(cls, marktlokations_id)
