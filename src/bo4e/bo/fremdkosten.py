"""
Contains Fremdkosten class and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..com.betrag import Betrag
from ..com.fremdkostenblock import Fremdkostenblock
from ..com.zeitraum import Zeitraum
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

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
        `Fremdkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Fremdkosten.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.FREMDKOSTEN
    #: Für diesen Zeitraum wurden die Kosten ermittelt
    gueltigkeit: Optional[Zeitraum] = None
    #: Die Gesamtsumme über alle Kostenblöcke und -positionen
    summe_kosten: Optional[Betrag] = None
    #: In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc
    kostenbloecke: Optional[list[Fremdkostenblock]] = None
