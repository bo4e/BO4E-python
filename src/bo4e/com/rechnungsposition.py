"""
Contains Rechnungsposition class
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..com.steuerbetrag import Steuerbetrag
    from ..com.zeitraum import Zeitraum
    from ..enum.bdewartikelnummer import BDEWArtikelnummer
    from ..enum.mengeneinheit import Mengeneinheit
    from .betrag import Betrag
    from .menge import Menge
    from .preis import Preis


@postprocess_docstring
class Rechnungsposition(COM):
    """
    Über Rechnungspositionen werden Rechnungen strukturiert.
    In einem Rechnungsteil wird jeweils eine in sich geschlossene Leistung abgerechnet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Rechnungsposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rechnungsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Rechnungsposition.json>`_

    """

    typ: Annotated[Literal[ComTyp.RECHNUNGSPOSITION], Field(alias="_typ")] = ComTyp.RECHNUNGSPOSITION

    positionsnummer: Optional[int] = None
    """Fortlaufende Nummer für die Rechnungsposition"""

    lieferungszeitraum: Optional["Zeitraum"] = None
    """Zeitraum der Lieferung für die abgerechnete Leistung"""

    positionstext: Optional[str] = None
    """Bezeichung für die abgerechnete Position"""

    positions_menge: Optional["Menge"] = None
    """Die abgerechnete Menge mit Einheit"""
    einzelpreis: Optional["Preis"] = None
    """Der Preis für eine Einheit der energetischen Menge"""
    gesamtpreis: Optional["Betrag"] = None
    """
    Das Ergebnis der Multiplikation aus einzelpreis * positionsMenge * (Faktor aus zeitbezogeneMenge).
    Z.B. 12,60€ * 120 kW * 3/12 (für 3 Monate).
    """

    # the cross check in general doesn't work because Betrag and Preis use different enums to describe the currency
    # see https://github.com/Hochfrequenz/BO4E-python/issues/126

    artikelnummer: Optional["BDEWArtikelnummer"] = None
    """Kennzeichnung der Rechnungsposition mit der Standard-Artikelnummer des BDEW"""
    artikel_id: Optional[str] = None
    """Standardisierte vom BDEW herausgegebene Liste, welche im Strommarkt die BDEW-Artikelnummer ablöst"""
    steuerbetrag: Optional["Steuerbetrag"] = None
    """Auf die Position entfallende Steuer, bestehend aus Steuersatz und Betrag"""
    zeiteinheit: Optional["Mengeneinheit"] = None
    """Falls sich der Preis auf eine Zeit bezieht, steht hier die Einheit"""
    zeitbezogene_menge: Optional["Menge"] = None
    """
    Eine auf die Zeiteinheit bezogene Untermenge.
    Z.B. bei einem Jahrespreis, 3 Monate oder 146 Tage.
    Basierend darauf wird der Preis aufgeteilt.
    """
