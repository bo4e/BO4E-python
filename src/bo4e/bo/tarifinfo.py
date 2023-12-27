"""
Contains Tarifinfo class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-many-instance-attributes, too-few-public-methods
# pylint: disable=no-name-in-module
from datetime import datetime
from typing import Annotated, Optional

from pydantic import Field

from ..com.energiemix import Energiemix
from ..com.vertragskonditionen import Vertragskonditionen
from ..com.zeitraum import Zeitraum
from ..enum.kundentyp import Kundentyp
from ..enum.registeranzahl import Registeranzahl
from ..enum.sparte import Sparte
from ..enum.tarifmerkmal import Tarifmerkmal
from ..enum.tariftyp import Tariftyp
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt
from .marktteilnehmer import Marktteilnehmer


@postprocess_docstring
class Tarifinfo(Geschaeftsobjekt):
    """
    Das BO Tarifinfo liefert die Merkmale, die einen Endkundentarif identifizierbar machen.
    Dieses BO dient als Basis für weitere BOs mit erweiterten Anwendungsmöglichkeiten.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarifinfo.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifinfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Tarifinfo.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.TARIFINFO
    #: Name des Tarifs
    bezeichnung: Optional[str] = None
    #: Der Name des Marktpartners, der den Tarif anbietet
    anbietername: Optional[str] = None
    #: Strom oder Gas, etc.
    sparte: Optional[Sparte] = None
    #: Kundentypen für den der Tarif gilt, z.B. Privatkunden
    kundentypen: Optional[list[Kundentyp]] = None
    #: Die Art des Tarifes, z.B. Eintarif oder Mehrtarif
    registeranzahl: Optional[Registeranzahl] = None
    #: Hinweis auf den Tariftyp, z.B. Grundversorgung oder Sondertarif
    tariftyp: Optional[Tariftyp] = None
    #: Weitere Merkmale des Tarifs, z.B. Festpreis oder Vorkasse
    tarifmerkmale: Optional[list[Tarifmerkmal]] = None
    #: Der Marktteilnehmer (Lieferant), der diesen Tarif anbietet
    anbieter: Optional[Marktteilnehmer] = None

    #: Internetseite auf dem der Tarif zu finden ist
    website: Optional[str] = None
    #: Freitext
    bemerkung: Optional[str] = None

    #: Angabe, in welchem Zeitraum der Tarif gültig ist
    zeitliche_gueltigkeit: Optional[Zeitraum] = None
    #: Der Energiemix, der für diesen Tarif gilt
    energiemix: Optional[Energiemix] = None
    #: Mindestlaufzeiten und Kündigungsfristen zusammengefasst
    vertragskonditionen: Optional[Vertragskonditionen] = None
    anwendung_von: Optional[datetime] = None
    """
    Angabe des inklusiven Zeitpunkts, ab dem der Tarif bzw. der Preis angewendet und abgerechnet wird,
    z.B. "2021-07-20T18:31:48Z"
    """
