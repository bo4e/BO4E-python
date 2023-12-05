"""
Contains Rechnung class
and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import Annotated, Optional

from pydantic import Field

from ..com.betrag import Betrag
from ..com.rechnungsposition import Rechnungsposition
from ..com.steuerbetrag import Steuerbetrag
from ..com.zeitraum import Zeitraum
from ..enum.netznutzungrechnungsart import NetznutzungRechnungsart
from ..enum.netznutzungrechnungstyp import NetznutzungRechnungstyp
from ..enum.rechnungsstatus import Rechnungsstatus
from ..enum.rechnungstyp import Rechnungstyp
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt
from .geschaeftspartner import Geschaeftspartner
from .marktlokation import Marktlokation
from .messlokation import Messlokation

# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class Rechnung(Geschaeftsobjekt):
    """
    Modell für die Abbildung von Rechnungen und Netznutzungsrechnungen im Kontext der Energiewirtschaft;

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Rechnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Rechnung.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.RECHNUNG
    ist_storno: Optional[bool] = None
    """
    Kennzeichnung, ob es sich um eine Stornorechnung handelt;
    im Falle "true" findet sich im Attribut "originalrechnungsnummer" die Nummer der Originalrechnung.
    """
    #: Eine im Verwendungskontext eindeutige Nummer für die Rechnung
    rechnungsnummer: Optional[str] = None
    #: Ausstellungsdatum der Rechnung
    rechnungsdatum: Optional[datetime] = None
    #: Zu diesem Datum ist die Zahlung fällig
    faelligkeitsdatum: Optional[datetime] = None
    #: Ein kontextbezogender Rechnungstyp, z.B. Netznutzungsrechnung
    rechnungstyp: Optional[Rechnungstyp] = None
    #: Der Zeitraum der zugrunde liegenden Lieferung zur Rechnung
    rechnungsperiode: Optional[Zeitraum] = None
    #: Der Aussteller der Rechnung, die Rollencodenummer kennt man über den im Geschäftspartner verlinkten Marktteilnehmer
    rechnungsersteller: Optional[Geschaeftspartner] = None
    #: Der Aussteller der Rechnung, die Rollencodenummer kennt man über den im Geschäftspartner verlinkten Marktteilnehmer
    rechnungsempfaenger: Optional[Geschaeftspartner] = None
    #: Die Summe der Nettobeträge der Rechnungsteile
    gesamtnetto: Optional[Betrag] = None
    #: Die Summe der Steuerbeträge der Rechnungsteile
    gesamtsteuer: Optional[Betrag] = None
    #: Die Summe aus Netto- und Steuerbetrag
    gesamtbrutto: Optional[Betrag] = None
    #: Der zu zahlende Betrag, der sich aus (gesamtbrutto - vorausbezahlt - rabattBrutto) ergibt
    zu_zahlen: Optional[Betrag] = None
    #: Die Rechnungspositionen
    rechnungspositionen: Optional[list[Rechnungsposition]] = None
    #: Bezeichnung für die vorliegende Rechnung
    rechnungstitel: Optional[str] = None
    #: Status der Rechnung zur Kennzeichnung des Bearbeitungsstandes
    rechnungsstatus: Optional[Rechnungsstatus] = None
    #: Im Falle einer Stornorechnung (storno = true) steht hier die Rechnungsnummer der stornierten Rechnung
    original_rechnungsnummer: Optional[str] = None
    #: Die Summe evtl. vorausgezahlter Beträge, z.B. Abschläge. Angabe als Bruttowert
    vorausgezahlt: Optional[Betrag] = None
    #: Gesamtrabatt auf den Bruttobetrag
    rabatt_brutto: Optional[Betrag] = None
    steuerbetraege: Optional[list[Steuerbetrag]] = None
    """
    Eine Liste mit Steuerbeträgen pro Steuerkennzeichen/Steuersatz;
    die Summe dieser Beträge ergibt den Wert für gesamtsteuer.
    """
    #: Sparte (Strom, Gas ...) für die die Rechnung ausgestellt ist
    sparte: Optional[Sparte] = None
    #: Aus der INVOIC entnommen, befüllt wenn es sich um eine Netznutzungsrechnung handelt
    netznutzungrechnungsart: Optional[NetznutzungRechnungsart] = None
    #: Aus der INVOIC entnommen, befüllt wenn es sich um eine Netznutzungsrechnung handelt
    netznutzungrechnungstyp: Optional[NetznutzungRechnungstyp] = None
    #: Kennzeichen, ob es sich um ein Original (true) oder eine Kopie handelt (false)
    ist_original: Optional[bool] = None
    #: Kennzeichen, ob es sich um eine simulierte Rechnung, z.B. zur Rechnungsprüfung handelt
    ist_simuliert: Optional[bool] = None
    #: Marktlokation, auf die sich die Rechnung bezieht
    marktlokation: Optional[Marktlokation] = None
    #: Messlokation, auf die sich die Rechnung bezieht
    messlokation: Optional[Messlokation] = None
