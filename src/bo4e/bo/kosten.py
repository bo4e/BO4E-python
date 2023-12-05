"""
Contains Kosten class and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..com.betrag import Betrag
from ..com.kostenblock import Kostenblock
from ..com.zeitraum import Zeitraum
from ..enum.kostenklasse import Kostenklasse
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

# pylint: disable=too-many-instance-attributes, too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Kosten(Geschaeftsobjekt):
    """
    Dieses BO wird zur Übertagung von hierarchischen Kostenstrukturen verwendet.
    Die Kosten werden dabei in Kostenblöcke und diese wiederum in Kostenpositionen strukturiert.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Kosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Kosten.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.KOSTEN
    #: Klasse der Kosten, beispielsweise Fremdkosten
    kostenklasse: Optional[Kostenklasse] = None
    #: Für diesen Zeitraum wurden die Kosten ermittelt
    gueltigkeit: Optional[Zeitraum] = None
    #: In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc
    kostenbloecke: Optional[list[Kostenblock]] = None

    #: Die Gesamtsumme über alle Kostenblöcke und -positionen
    summe_kosten: Optional[list[Betrag]] = None
