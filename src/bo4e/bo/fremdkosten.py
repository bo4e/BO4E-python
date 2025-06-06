"""
Contains Fremdkosten class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.betrag import Betrag
    from ..com.fremdkostenblock import Fremdkostenblock
    from ..com.zeitraum import Zeitraum


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Fremdkosten(Geschaeftsobjekt):
    """
    Mit diesem BO werden die Fremdkosten, beispielsweise für eine Angebotserstellung oder eine Rechnungsprüfung,
    übertragen.
    Die Fremdkosten enthalten dabei alle Kostenblöcke, die von anderen Marktteilnehmern oder Instanzen erhoben werden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Fremdkosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Fremdkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Fremdkosten.json>`_

    """

    typ: Annotated[Literal[BoTyp.FREMDKOSTEN], Field(alias="_typ")] = BoTyp.FREMDKOSTEN
    gueltigkeit: Optional["Zeitraum"] = None
    """Für diesen Zeitraum wurden die Kosten ermittelt"""
    summe_kosten: Optional["Betrag"] = None
    """Die Gesamtsumme über alle Kostenblöcke und -positionen"""
    kostenbloecke: Optional[list["Fremdkostenblock"]] = None
    """In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc"""
