"""
Contains Tarif class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .tarifinfo import Tarifinfo

if TYPE_CHECKING:
    from ..bo.marktteilnehmer import Marktteilnehmer
    from ..com.dynamischepreisposition import DynamischePreisposition
    from ..com.energiemix import Energiemix
    from ..com.preisgarantie import Preisgarantie
    from ..com.regionspreis import Regionspreis
    from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
    from ..com.vertragskonditionen import Vertragskonditionen
    from ..com.zeitraum import Zeitraum
    from ..enum.kundentyp import Kundentyp
    from ..enum.registeranzahl import Registeranzahl
    from ..enum.sparte import Sparte
    from ..enum.tarifmerkmal import Tarifmerkmal
    from ..enum.tariftyp import Tariftyp


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Tarif(Tarifinfo):
    """
    Abbildung eines Tarifs.

    Der Tarifpreis kann regionsaufgelöst und unter Angabe von Zeitscheiben angegeben werden. So kann bspw. derselbe
    Tarif je nach Region andere Preise aufweisen. Es können auch Tarifpreise abgebildet werden, die sich ab einem
    bestimmten Zeitpunkt auf andere Regionen ausweiten, da die Regionen ebenfalls mit Zeitscheiben versehen sind.

    Ein Tarifpreis setzt sich dabei aus mehreren Preispositionen zusammen. So können z.B. auch mit
    `COM RelativePreisposition` prozentuale Auf- und Abschläge auf andere Preispositionen definiert werden.
    Alle Preispositionen hängen unter `COM Tarifpreiszeitscheibe` mit einer Ausnahme.

    Möchten Sie einen dynamischen Tarif modellieren, so gibt es das `COM DynamischePreisposition`. Da diese
    Preisposition weder orts- noch zeitabhängig ist, hängt diese direkt unter dem `BO Tarif`. Eine zeitabhängige
    Änderung einer dynamischen Tarifpreisposition ist unsinnig, da es sich (unserer Ansicht nach) dann um einen
    völlig neuen Tarif handelt. Davon unabhängig können (und müssen) natürlich weiterhin zusätzlich alle anderen
    Preispositionen orts- und zeitabhängig angegeben werden.

    > Hinweis: Das Vorhandensein einer `COM DynamischePreisposition` dient gleichzeitig auch als "Flag" dafür, ob
    > es sich bei diesem Tarif um einen dynamischen handelt.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Tarif.json>`_

    """

    typ: Annotated[Literal[BoTyp.TARIF], Field(alias="_typ")] = BoTyp.TARIF

    regionspreise: Optional[list["Regionspreis"]] = None
    """
    Enthält alle regions- und zeitaufgelösten Tarifpreise.
    Ausschließlich die `COM DynamischePreisposition` wird unter einem anderen Feld namens `dynamischePreisposition`
    angegeben.
    """
    dynamische_preisposition: Optional["DynamischePreisposition"] = None
    """
    Dieses Feld muss genau dann gesetzt werden, wenn es sich bei diesem Tarif um einen dynamischen Tarif handelt.
    Die dynamische Preisposition enthält im wesentlichen eine Referenz zum entsprechenden Börsenindex.
    """

    bezeichnung: Optional[str] = None
    """Eine (beliebige) Bezeichnung für den Tarif."""
    beschreibung: Optional[str] = None
    """Eine (beliebige) Beschreibung für den Tarif."""
    anbieter: Optional["Marktteilnehmer"] = None
    """Der Marktteilnehmer, der diesen Tarif anbietet, angeboten hat oder anbieten wird."""

    zeitraum_vermarktung: Optional["Zeitraum"] = None
    """Der Zeitraum, in dem der Tarif beim Anbieter vertraglich abschließbar ist."""
    zeitraum_belieferbarkeit: Optional["Zeitraum"] = None
    """Der Zeitraum, in dem eine Belieferung (für diesen Tarif) möglich ist."""
    vertragskonditionen: Optional["Vertragskonditionen"]
    """Vertragskonditionen für diesen Tarif."""
    vertriebskanal: Optional[str] = None
    """TODO: Create a COM for this."""
    website: Optional[str]
    """Internetseite, auf der der Tarif veröffentlicht ist."""
    energiemix: Optional[list["Energiemix"]]
    """TODO: Write meaningful doc-string"""
    kundentypen: Optional[list["Kundentyp"]]
    """Eine Liste an Kundentypen, für die dieser Tarif vorgesehen ist."""
    tariftyp: Optional["Tariftyp"]
    """Der Tariftyp. Bsp.: Grundversorgung, Ersatzversorgung, etc."""
    tarifmerkmale: Optional[list["Tarifmerkmal"]]
    """Eine Liste von Produktmerkmalen im Zusammenhang mit diesem Tarif."""
    sparte: Optional["Sparte"]
    """Strom / Gas"""
    registeranzahl: Optional["Registeranzahl"]
    """
    Hinweis zu den Registern bzw. Zählwerken.
    Bspw. benötigt ein HT-/NT-Tarif auch eine entsprechende Registeranzahl.
    """
    preisgarantie: Optional["Preisgarantie"]
    """Preisgarantie für diesen Tarif"""
    berechnungsparameter: Optional["Tarifberechnungsparameter"]
    """Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen"""
