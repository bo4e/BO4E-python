"""
Contains Rechnungsposition class and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

# pylint: disable=too-few-public-methods, too-many-instance-attributes
from typing import Optional

from ..enum.bdewartikelnummer import BDEWArtikelnummer
from ..enum.mengeneinheit import Mengeneinheit
from ..utils import postprocess_docstring
from .betrag import Betrag
from .com import COM
from .menge import Menge
from .preis import Preis
from .steuerbetrag import Steuerbetrag


@postprocess_docstring
class Rechnungsposition(COM):
    """
    Über Rechnungspositionen werden Rechnungen strukturiert.
    In einem Rechnungsteil wird jeweils eine in sich geschlossene Leistung abgerechnet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Rechnungsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnungsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Rechnungsposition.json>`_

    """

    #: Fortlaufende Nummer für die Rechnungsposition
    positionsnummer: Optional[int] = None

    lieferung_von: Optional[datetime] = None  #: Start der Lieferung für die abgerechnete Leistung (inklusiv)
    lieferung_bis: Optional[datetime] = None  #: Ende der Lieferung für die abgerechnete Leistung (exklusiv)

    #: Bezeichung für die abgerechnete Position
    positionstext: Optional[str] = None

    #: Die abgerechnete Menge mit Einheit
    positions_menge: Optional[Menge] = None
    #: Der Preis für eine Einheit der energetischen Menge
    einzelpreis: Optional[Preis] = None

    teilsumme_netto: Optional[Betrag] = None
    """
    Das Ergebnis der Multiplikation aus einzelpreis * positionsMenge * (Faktor aus zeitbezogeneMenge).
    Z.B. 12,60€ * 120 kW * 3/12 (für 3 Monate).
    """
    # the cross check in general doesn't work because Betrag and Preis use different enums to describe the currency
    # see https://github.com/Hochfrequenz/BO4E-python/issues/126

    #: Auf die Position entfallende Steuer, bestehend aus Steuersatz und Betrag
    teilsumme_steuer: Optional[Steuerbetrag] = None

    #: Falls sich der Preis auf eine Zeit bezieht, steht hier die Einheit
    zeiteinheit: Optional[Mengeneinheit] = None

    #: Kennzeichnung der Rechnungsposition mit der Standard-Artikelnummer des BDEW
    artikelnummer: Optional[BDEWArtikelnummer] = None
    #: Marktlokation, die zu dieser Position gehört
    lokations_id: Optional[str] = None

    zeitbezogene_menge: Optional[Menge] = None
    """
    Eine auf die Zeiteinheit bezogene Untermenge.
    Z.B. bei einem Jahrespreis, 3 Monate oder 146 Tage.
    Basierend darauf wird der Preis aufgeteilt.
    """
    #: Nettobetrag für den Rabatt dieser Position
    teilrabatt_netto: Optional[Betrag] = None

    #: Standardisierte vom BDEW herausgegebene Liste, welche im Strommarkt die BDEW-Artikelnummer ablöst
    artikel_id: Optional[str] = None
