"""
Contains Preisposition class and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from annotated_types import Len

from bo4e.com.com import COM
from bo4e.com.preisstaffel import Preisstaffel
from bo4e.enum.bdewartikelnummer import BDEWArtikelnummer
from bo4e.enum.bemessungsgroesse import Bemessungsgroesse
from bo4e.enum.kalkulationsmethode import Kalkulationsmethode
from bo4e.enum.leistungstyp import Leistungstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.tarifzeit import Tarifzeit
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.enum.zeiteinheit import Zeiteinheit

# pylint: disable=too-few-public-methods, too-many-instance-attributes


class Preisposition(COM):
    """
    Preis für eine definierte Lieferung oder Leistung innerhalb eines Preisblattes

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Preisposition.json>`_

    """

    # required attributes
    #: Das Modell, das der Preisbildung zugrunde liegt
    berechnungsmethode: Kalkulationsmethode
    #: Standardisierte Bezeichnung für die abgerechnete Leistungserbringung
    leistungstyp: Leistungstyp  #
    #: Bezeichnung für die in der Position abgebildete Leistungserbringung
    leistungsbezeichnung: str
    #: Festlegung, mit welcher Preiseinheit abgerechnet wird, z.B. Ct. oder €
    preiseinheit: Waehrungseinheit
    #: Hier wird festgelegt, auf welche Bezugsgrösse sich der Preis bezieht, z.B. kWh oder Stück
    bezugsgroesse: Mengeneinheit
    #: Preisstaffeln, die zu dieser Preisposition gehören
    preisstaffeln: Annotated[list[Preisstaffel], Len(1)]

    # optional attributes
    zeitbasis: Optional[Zeiteinheit] = None
    """
    Die Zeit(dauer) auf die sich der Preis bezieht.
    Z.B. ein Jahr für einen Leistungspreis der in €/kW/Jahr ausgegeben wird
    """
    #: Festlegung, für welche Tarifzeit der Preis hier festgelegt ist
    tarifzeit: Optional[Tarifzeit] = None
    bdew_artikelnummer: Optional[BDEWArtikelnummer] = None
    """
    Eine vom BDEW standardisierte Bezeichnug für die abgerechnete Leistungserbringung;
    Diese Artikelnummer wird auch im Rechnungsteil der INVOIC verwendet.
    """
    #: Mit der Menge der hier angegebenen Größe wird die Staffelung/Zonung durchgeführt. Z.B. Vollbenutzungsstunden
    zonungsgroesse: Optional[Bemessungsgroesse] = None
    #: Der Anteil der Menge der Blindarbeit in Prozent von der Wirkarbeit, für die keine Abrechnung erfolgt
    freimenge_blindarbeit: Optional[Decimal] = None
    freimenge_leistungsfaktor: Optional[Decimal] = None
    """
    Der cos phi (Verhältnis Wirkleistung/Scheinleistung) aus dem die Freimenge für die Blindarbeit berechnet wird als
    tan phi (Verhältnis Blindleistung/Wirkleistung)
    """
    gruppenartikel_id: Optional[str] = None
    """
    Übergeordnete Gruppen-ID, die sich ggf. auf die Artikel-ID in der Preisstaffel bezieht
    """
