"""
Contains Rechnungsposition class and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

# pylint: disable=too-few-public-methods, too-many-instance-attributes
from typing import Any, Dict, Optional

from pydantic import validator

from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.menge import Menge
from bo4e.com.preis import Preis
from bo4e.com.steuerbetrag import Steuerbetrag
from bo4e.enum.artikelid import ArtikelId
from bo4e.enum.bdewartikelnummer import BDEWArtikelnummer
from bo4e.enum.zeiteinheit import Zeiteinheit
from bo4e.validators import check_bis_is_later_than_von


class Rechnungsposition(COM):
    """
    Über Rechnungspositionen werden Rechnungen strukturiert.
    In einem Rechnungsteil wird jeweils eine in sich geschlossene Leistung abgerechnet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Rechnungsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnungsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Rechnungsposition.json>`_

    """

    # required attributes
    #: Fortlaufende Nummer für die Rechnungsposition
    positionsnummer: int

    lieferung_von: datetime  #: Start der Lieferung für die abgerechnete Leistung (inklusiv)
    lieferung_bis: datetime  #: Ende der Lieferung für die abgerechnete Leistung (exklusiv)
    _bis_check = validator("lieferung_bis", always=True, allow_reuse=True)(check_bis_is_later_than_von)

    #: Bezeichung für die abgerechnete Position
    positionstext: str

    #: Die abgerechnete Menge mit Einheit
    positions_menge: Menge
    #: Der Preis für eine Einheit der energetischen Menge
    einzelpreis: Preis

    teilsumme_netto: Betrag
    """
    Das Ergebnis der Multiplikation aus einzelpreis * positionsMenge * (Faktor aus zeitbezogeneMenge).
    Z.B. 12,60€ * 120 kW * 3/12 (für 3 Monate).
    """
    # the cross check in general doesn't work because Betrag and Preis use different enums to describe the currency
    # see https://github.com/Hochfrequenz/BO4E-python/issues/126

    #: Auf die Position entfallende Steuer, bestehend aus Steuersatz und Betrag
    teilsumme_steuer: Steuerbetrag

    # optional attributes
    #: Falls sich der Preis auf eine Zeit bezieht, steht hier die Einheit
    zeiteinheit: Optional[Zeiteinheit] = None

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
    artikel_id: Optional[ArtikelId] = None

    @staticmethod
    def _get_inclusive_start(values: Dict[str, Any]) -> datetime:
        """return the inclusive start (used in the validator)"""
        return values["lieferung_von"]

    # def _get_exclusive_end(self) -> datetime:
    #     """return the exclusive end (used in the validator)"""
    #     return self.lieferung_bis
