"""
Contains Kosten class and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.betrag import Betrag
from bo4e.com.kostenblock import Kostenblock
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kostenklasse import Kostenklasse

# pylint: disable=too-many-instance-attributes, too-few-public-methods
# pylint: disable=no-name-in-module


class Kosten(Geschaeftsobjekt):
    """
    Dieses BO wird zur Übertagung von hierarchischen Kostenstrukturen verwendet.
    Die Kosten werden dabei in Kostenblöcke und diese wiederum in Kostenpositionen strukturiert.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Kosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Kosten.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.KOSTEN
    #: Klasse der Kosten, beispielsweise Fremdkosten
    kostenklasse: Optional[Kostenklasse] = None
    #: Für diesen Zeitraum wurden die Kosten ermittelt
    gueltigkeit: Optional[Zeitraum] = None
    #: In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc
    kostenbloecke: Optional[list[Kostenblock]] = None

    # optional attributes
    #: Die Gesamtsumme über alle Kostenblöcke und -positionen
    summe_kosten: Optional[list[Betrag]] = None
