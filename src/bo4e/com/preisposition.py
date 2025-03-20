"""
Contains Preisposition class and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.bdewartikelnummer import BDEWArtikelnummer
    from ..enum.bemessungsgroesse import Bemessungsgroesse
    from ..enum.kalkulationsmethode import Kalkulationsmethode
    from ..enum.leistungstyp import Leistungstyp
    from ..enum.mengeneinheit import Mengeneinheit
    from ..enum.tarifzeit import Tarifzeit
    from ..enum.waehrungseinheit import Waehrungseinheit
    from .preisstaffel import Preisstaffel

# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class Preisposition(COM):
    """
    Preis für eine definierte Lieferung oder Leistung innerhalb eines Preisblattes

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preisposition.json>`_

    """

    berechnungsmethode: Optional["Kalkulationsmethode"] = None
    """Das Modell, das der Preisbildung zugrunde liegt"""
    leistungstyp: Optional["Leistungstyp"] = None
    """Standardisierte Bezeichnung für die abgerechnete Leistungserbringung"""  #
    leistungsbezeichnung: Optional[str] = None
    """Bezeichnung für die in der Position abgebildete Leistungserbringung"""
    preiseinheit: Optional["Waehrungseinheit"] = None
    """Festlegung, mit welcher Preiseinheit abgerechnet wird, z.B. Ct. oder €"""
    bezugsgroesse: Optional["Mengeneinheit"] = None
    """Hier wird festgelegt, auf welche Bezugsgrösse sich der Preis bezieht, z.B. kWh oder Stück"""
    preisstaffeln: Optional[list["Preisstaffel"]] = None
    """Preisstaffeln, die zu dieser Preisposition gehören"""

    zeitbasis: Optional["Mengeneinheit"] = None
    """
    Die Zeit(dauer) auf die sich der Preis bezieht.
    Z.B. ein Jahr für einen Leistungspreis der in €/kW/Jahr ausgegeben wird
    """
    tarifzeit: Optional["Tarifzeit"] = None
    """Festlegung, für welche Tarifzeit der Preis hier festgelegt ist"""
    bdew_artikelnummer: Optional["BDEWArtikelnummer"] = None
    """
    Eine vom BDEW standardisierte Bezeichnug für die abgerechnete Leistungserbringung;
    Diese Artikelnummer wird auch im Rechnungsteil der INVOIC verwendet.
    """
    zonungsgroesse: Optional["Bemessungsgroesse"] = None
    """Mit der Menge der hier angegebenen Größe wird die Staffelung/Zonung durchgeführt. Z.B. Vollbenutzungsstunden"""
    freimenge_blindarbeit: Optional[Decimal] = None
    """Der Anteil der Menge der Blindarbeit in Prozent von der Wirkarbeit, für die keine Abrechnung erfolgt"""
    freimenge_leistungsfaktor: Optional[Decimal] = None
    """
    Der cos phi (Verhältnis Wirkleistung/Scheinleistung) aus dem die Freimenge für die Blindarbeit berechnet wird als
    tan phi (Verhältnis Blindleistung/Wirkleistung)
    """
    gruppenartikel_id: Optional[str] = None
    """
    Übergeordnete Gruppen-ID, die sich ggf. auf die Artikel-ID in der Preisstaffel bezieht
    """
