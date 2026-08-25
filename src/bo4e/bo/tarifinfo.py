"""
Contains Tarifinfo class
"""

# pylint: disable=too-many-instance-attributes, too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.energiemix import Energiemix
    from ..com.vertragskonditionen import Vertragskonditionen
    from ..com.zeitraum import Zeitraum
    from ..enum.kundentyp import Kundentyp
    from ..enum.registeranzahl import Registeranzahl
    from ..enum.sparte import Sparte
    from ..enum.tarifmerkmal import Tarifmerkmal
    from ..enum.tariftyp import Tariftyp
    from .marktteilnehmer import Marktteilnehmer


@postprocess_docstring
class Tarifinfo(Geschaeftsobjekt):
    """
    Das BO Tarifinfo liefert die Merkmale, die einen Endkundentarif identifizierbar machen.
    Dieses BO dient als Basis für weitere BOs mit erweiterten Anwendungsmöglichkeiten.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarifinfo.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifinfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Tarifinfo.json>`_

    """

    typ: Annotated[Literal[BoTyp.TARIFINFO], Field(alias="_typ")] = BoTyp.TARIFINFO
    bezeichnung: str | None = None
    """Name des Tarifs"""
    anbietername: str | None = None
    """Der Name des Marktpartners, der den Tarif anbietet"""
    sparte: Optional["Sparte"] = None
    """Strom oder Gas, etc."""
    kundentypen: list["Kundentyp"] | None = None
    """Kundentypen für den der Tarif gilt, z.B. Privatkunden"""
    registeranzahl: Optional["Registeranzahl"] = None
    """Die Art des Tarifes, z.B. Eintarif oder Mehrtarif"""
    tariftyp: Optional["Tariftyp"] = None
    """Hinweis auf den Tariftyp, z.B. Grundversorgung oder Sondertarif"""
    tarifmerkmale: list["Tarifmerkmal"] | None = None
    """Weitere Merkmale des Tarifs, z.B. Festpreis oder Vorkasse"""
    anbieter: Optional["Marktteilnehmer"] = None
    """Der Marktteilnehmer (Lieferant), der diesen Tarif anbietet"""

    website: str | None = None
    """Internetseite auf dem der Tarif zu finden ist"""
    bemerkung: str | None = None
    """Freitext"""

    zeitliche_gueltigkeit: Optional["Zeitraum"] = None
    """Angabe, in welchem Zeitraum der Tarif gültig ist"""
    energiemix: Optional["Energiemix"] = None
    """Der Energiemix, der für diesen Tarif gilt"""
    vertragskonditionen: Optional["Vertragskonditionen"] = None
    """Mindestlaufzeiten und Kündigungsfristen zusammengefasst"""
    anwendung_von: pydantic.AwareDatetime | None = None
    """
    Angabe des inklusiven Zeitpunkts, ab dem der Tarif bzw. der Preis angewendet und abgerechnet wird,
    z.B. "2021-07-20T18:31:48Z"
    """
