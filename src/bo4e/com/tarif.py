"""
Contains Tarif class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..com.energiemix import Energiemix
    from ..com.preisgarantie import Preisgarantie
    from ..com.regionspreis import Regionspreis
    from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
    from ..com.tarifeinschraenkung import Tarifeinschraenkung
    from ..enum.registeranzahl import Registeranzahl
    from ..enum.tarifmerkmal import Tarifmerkmal
    from ..enum.tariftyp import Tariftyp

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Tarif(COM):
    """
    Abbildung eines Tarifs (Preisbestandteile eines Produkts).

    Der Tarifpreis kann regionsaufgelöst und unter Angabe von Zeitscheiben angegeben werden. So kann bspw. derselbe
    Tarif je nach Region andere Preise aufweisen. Es können auch Tarifpreise abgebildet werden, die sich ab einem
    bestimmten Zeitpunkt auf andere Regionen ausweiten, da die Regionen ebenfalls mit Zeitscheiben versehen sind.

    Ein Tarifpreis setzt sich dabei aus mehreren Preispositionen zusammen. So können z.B. auch mit
    `COM RelativePreisposition` prozentuale Auf- und Abschläge auf andere Preispositionen definiert werden.
    Alle Preispositionen hängen unter `COM Tarifpreiszeitscheibe` mit einer Ausnahme.

    Möchten Sie einen dynamischen Tarif modellieren, so gibt es das `COM DynamischePreisposition`.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Tarif.json>`_

    """

    typ: Annotated[Literal[ComTyp.TARIF], Field(alias="_typ")] = ComTyp.TARIF

    regionspreise: Optional[list["Regionspreis"]] = None
    """
    Enthält alle regions- und zeitaufgelösten Tarifpreise.
    Ausschließlich die `COM DynamischePreisposition` wird unter einem anderen Feld namens `dynamischePreisposition`
    angegeben.
    """
    dynamische_preisposition_quelle: Optional[str] = None
    """
    Gibt die Bezugsquelle (z.B. Börsenindex) für den dynamischen Tarif an.
    Dieses Feld muss genau dann gesetzt werden, wenn es sich bei diesem Tarif um einen dynamischen Tarif handelt.
    """
    energiemix: Optional[list["Energiemix"]] = None
    """Der Energiemix mit einem Eintrag pro Gültigkeitsjahr (siehe `Energiemix.gueltigkeitsjahr`)."""
    tariftyp: Optional["Tariftyp"] = None
    """Der Tariftyp. Bsp.: Grundversorgung, Ersatzversorgung, etc."""
    tarifmerkmale: Optional[list["Tarifmerkmal"]] = None
    """Eine Liste von Produktmerkmalen im Zusammenhang mit diesem Tarif."""
    registeranzahl: Optional["Registeranzahl"] = None
    """
    Hinweis zu den Registern bzw. Zählwerken.
    Bspw. benötigt ein HT-/NT-Tarif auch eine entsprechende Registeranzahl.
    """
    preisgarantie: Optional["Preisgarantie"] = None
    """Preisgarantie für diesen Tarif"""
    berechnungsparameter: Optional["Tarifberechnungsparameter"] = None
    """Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen"""
    tarifeinschraenkung: Optional["Tarifeinschraenkung"] = None
    """Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann"""
