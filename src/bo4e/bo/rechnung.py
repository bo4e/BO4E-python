"""
Contains Rechnung class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.betrag import Betrag
    from ..com.rechnungsposition import Rechnungsposition
    from ..com.steuerbetrag import Steuerbetrag
    from ..com.vorauszahlung import Vorauszahlung
    from ..com.zahlungsinformation import Zahlungsinformation
    from ..com.zeitraum import Zeitraum
    from ..enum.netznutzungrechnungsart import NetznutzungRechnungsart
    from ..enum.netznutzungrechnungstyp import NetznutzungRechnungstyp
    from ..enum.rechnungsstatus import Rechnungsstatus
    from ..enum.rechnungstyp import Rechnungstyp
    from ..enum.sparte import Sparte
    from .energiemenge import Energiemenge
    from .fremdkosten import Fremdkosten
    from .geschaeftspartner import Geschaeftspartner
    from .marktlokation import Marktlokation
    from .marktteilnehmer import Marktteilnehmer
    from .messlokation import Messlokation
    from .vertrag import Vertrag
    from .zaehler import Zaehler

# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class Rechnung(Geschaeftsobjekt):
    """
    Modell für die Abbildung von Rechnungen und Netznutzungsrechnungen im Kontext der Energiewirtschaft;

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Rechnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Rechnung.json>`_

    """

    typ: Annotated[Literal[BoTyp.RECHNUNG], Field(alias="_typ")] = BoTyp.RECHNUNG

    rechnungsnummer: Optional[str] = None
    """Eine im Verwendungskontext eindeutige Nummer für die Rechnung"""
    rechnungsdatum: Optional[pydantic.AwareDatetime] = None
    """Ausstellungsdatum der Rechnung"""
    faelligkeitsdatum: Optional[pydantic.AwareDatetime] = None
    """Zu diesem Datum ist die Zahlung fällig"""
    rechnungstyp: Optional["Rechnungstyp"] = None
    """Ein kontextbezogender Rechnungstyp, z.B. Netznutzungsrechnung"""
    rechnungsperiode: Optional["Zeitraum"] = None
    """Der Zeitraum der zugrunde liegenden Lieferung zur Rechnung"""
    rechnungsersteller: Optional["Geschaeftspartner"] = None
    """
    Der Aussteller der Rechnung. Die Rollencodenummer kennt man über den im Geschäftspartner verlinkten Marktteilnehmer.
    """
    rechnungsempfaenger: Optional["Geschaeftspartner"] = None
    """
    Der Aussteller der Rechnung. Die Rollencodenummer kennt man über den im Geschäftspartner verlinkten Marktteilnehmer.
    """
    gesamtnetto: Optional["Betrag"] = None
    """Die Summe der Nettobeträge der Rechnungsteile"""
    gesamtsteuer: Optional["Betrag"] = None
    """Die Summe der Steuerbeträge der Rechnungsteile"""
    gesamtbrutto: Optional["Betrag"] = None
    """Die Summe aus Netto- und Steuerbetrag"""
    zu_zahlen: Optional["Betrag"] = None
    """Der zu zahlende Betrag, der sich aus (gesamtbrutto - vorausbezahlt - rabattBrutto) ergibt"""
    zaehler: Optional[list["Zaehler"]] = None
    zukuenftiger_abschlag: Optional["Betrag"] = None
    kaeuferreferenz: Optional[str] = None

    rechnungspositionen: Optional[list["Rechnungsposition"]] = None
    """Die Rechnungspositionen"""
    rechnungstitel: Optional[str] = None
    """Bezeichnung für die vorliegende Rechnung"""
    rechnungsstatus: Optional["Rechnungsstatus"] = None
    """Status der Rechnung zur Kennzeichnung des Bearbeitungsstandes"""
    original_rechnungsnummer: Optional[str] = None
    """Im Falle einer Stornorechnung (storno = true) steht hier die Rechnungsnummer der stornierten Rechnung"""
    vorauszahlungen: Optional[list["Vorauszahlung"]] = None
    """Die Summe evtl. vorausgezahlter Beträge, z.B. Abschläge. Angabe als Bruttowert"""
    rabatt_netto: Optional["Betrag"] = None
    """Gesamtrabatt auf den Nettobetrag"""
    steuerbetraege: Optional[list["Steuerbetrag"]] = None
    """
    Eine Liste mit Steuerbeträgen pro Steuerkennzeichen/Steuersatz;
    die Summe dieser Beträge ergibt den Wert für gesamtsteuer.
    """
    sparte: Optional["Sparte"] = None
    """Sparte (Strom, Gas ...) für die die Rechnung ausgestellt ist"""
    netznutzungrechnungsart: Optional["NetznutzungRechnungsart"] = None
    """Aus der INVOIC entnommen, befüllt wenn es sich um eine Netznutzungsrechnung handelt"""
    netznutzungrechnungstyp: Optional["NetznutzungRechnungstyp"] = None
    """Aus der INVOIC entnommen, befüllt wenn es sich um eine Netznutzungsrechnung handelt"""
    ist_original: Optional[bool] = None
    """Kennzeichen, ob es sich um ein Original (true) oder eine Kopie handelt (false)"""
    ist_simuliert: Optional[bool] = None
    """Kennzeichen, ob es sich um eine simulierte Rechnung, z.B. zur Rechnungsprüfung handelt"""
    ist_storno: Optional[bool] = None
    """
    Kennzeichnung, ob es sich um eine Stornorechnung handelt;
    im Falle "true" findet sich im Attribut "originalrechnungsnummer" die Nummer der Originalrechnung.
    """
    marktlokation: Optional["Marktlokation"] = None
    """Marktlokation, auf die sich die Rechnung bezieht"""
    messlokation: Optional["Messlokation"] = None
    """Messlokation, auf die sich die Rechnung bezieht"""
    teilrechnungen: Optional[list["Rechnung"]] = None
    """Rechnungen, die durch diese Rechnung zusammengefasst werden"""
    zahlungsinformationen: Optional[list["Zahlungsinformation"]] = None
    """Informationen wie eine Rechnung bezahlt werden soll"""
    vertrag: Optional["Vertrag"] = None
    """enthält Informationen über den der Rechnung zugrundeliegenden Vertrag für Rechnungen nach EnWG § 40"""
    messstellenbetreiber: Optional["Marktteilnehmer"] = None
    """der Messtellenbetreiber an der Lieferstelle, relevant für Rechnungen gemäß EnWG § 40"""
    netzbetreiber: Optional["Marktteilnehmer"] = None
    """der Netzbetreiber an der Lieferstelle, relevant für Rechnungen gemäß EnWG § 40"""
    anfangszaehlerstand: Optional["Energiemenge"] = None
    """Für Verbrauchsbasierte Rechnungen der Zählerstand zur Beginn des abgerechneten Zeitraums, Pflicht für Rechnungen gemäß EnWG § 40"""
    endzaehlerstand: Optional["Energiemenge"] = None
    """Für Verbrauchsbasierte Rechnungen der Zählerstand zum Ende des abgerechneten Zeitraums, Pflicht für Rechnungen gemäß EnWG § 40"""
    aktueller_verbrauch: Optional["Energiemenge"] = None
    """Verbrauch des abgerechneten Zeitraums, Pflicht für Rechnungen gemäß EnWG § 40"""
    jahresverbrauch: Optional["Energiemenge"] = None
    """ggf. auf einen Vergleichszeitraum hochgerechneter Verbrauch des abgerechneten Zeitraums zu Vergleichszwecken mit dem Vorjahr, gemäß EnWG § 40"""
    vorjahresverbrauch: Optional["Energiemenge"] = None
    """ggf. auf einen Vergleichszeitraum hochgerechneter Verbrauch des vorherigen Jahres zu Vergleichszwecken mit dem aktuellen Jahr, gemäß EnWG § 40"""
    fremdkosten: Optional["Fremdkosten"] = None
    """Zur Ausweisung der in die Kalkulation eingeflossenen Preise gemäß EnWG § 40"""
    referenzverbraeuche: Optional[list["Energiemenge"]] = None
    """Verbräuche von Referenzkundengruppen gemäß EnWG § 40"""
