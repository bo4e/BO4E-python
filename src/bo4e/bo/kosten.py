"""
Contains Kosten class and corresponding marshmallow schema for de-/serialization
"""
from typing import List

# pylint: disable=too-many-instance-attributes, too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.betrag import Betrag
from bo4e.com.kostenblock import Kostenblock
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kostenklasse import Kostenklasse


class Kosten(Geschaeftsobjekt):
    """
    Dieses BO wird zur Übertagung von hierarchischen Kostenstrukturen verwendet.
    Die Kosten werden dabei in Kostenblöcke und diese wiederum in Kostenpositionen strukturiert.

    .. graphviz:: /api/dots/bo4e/bo/Kosten.dot

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.KOSTEN
    #: Klasse der Kosten, beispielsweise Fremdkosten
    kostenklasse: Kostenklasse
    #: Für diesen Zeitraum wurden die Kosten ermittelt
    gueltigkeit: Zeitraum
    #: In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc
    kostenbloecke: conlist(Kostenblock, min_items=1)

    # optional attributes
    #: Die Gesamtsumme über alle Kostenblöcke und -positionen
    summe_kosten: List[Betrag] = None
