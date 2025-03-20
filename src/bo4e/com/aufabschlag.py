"""
Contains AufAbschlag class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.aufabschlagstyp import AufAbschlagstyp
    from ..enum.aufabschlagsziel import AufAbschlagsziel
    from ..enum.waehrungseinheit import Waehrungseinheit
    from .preisstaffel import Preisstaffel
    from .zeitraum import Zeitraum

# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class AufAbschlag(COM):
    """
    Modell für die preiserhöhenden (Aufschlag) bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen wurden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/AufAbschlag.json>`_

    """

    bezeichnung: Optional[str] = None
    """Bezeichnung des Auf-/Abschlags"""
    staffeln: Optional[list["Preisstaffel"]] = None
    """Werte für die gestaffelten Auf/Abschläge."""

    beschreibung: Optional[str] = None
    """Beschreibung zum Auf-/Abschlag"""
    auf_abschlagstyp: Optional["AufAbschlagstyp"] = None
    """Typ des Aufabschlages (z.B. absolut oder prozentual)."""
    auf_abschlagsziel: Optional["AufAbschlagsziel"] = None
    """Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc.."""
    einheit: Optional["Waehrungseinheit"] = None
    """ Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird. Euro oder Ct..
    (Nur im Falle absoluter Aufschlagstypen). """
    website: Optional[str] = None
    """Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind."""
    gueltigkeitszeitraum: Optional["Zeitraum"] = None
    """Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind."""
