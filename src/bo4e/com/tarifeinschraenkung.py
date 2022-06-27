"""
Contains Tarifeinschraenkung and corresponding marshmallow schema for de-/serialization
"""
from typing import List

from bo4e.com.com import COM
from bo4e.com.geraet import Geraet
from bo4e.com.menge import Menge
from bo4e.enum.voraussetzungen import Voraussetzungen


# pylint: disable=too-few-public-methods


class Tarifeinschraenkung(COM):
    """
    Mit dieser Komponente werden Einschränkungen für die Anwendung von Tarifen modelliert.

    .. graphviz:: /api/dots/bo4e/com/Tarifeinschraenkung.dot

    """

    # optional attributes
    #: Weitere Produkte, die gemeinsam mit diesem Tarif bestellt werden können
    zusatzprodukte: List[str] = None
    #: Voraussetzungen, die erfüllt sein müssen, damit dieser Tarif zur Anwendung kommen kann
    voraussetzungen: List[Voraussetzungen] = None
    einschraenkungzaehler: List[Geraet] = None
    """ Liste der Zähler/Geräte, die erforderlich sind, damit dieser Tarif zur Anwendung gelangen kann.
    (Falls keine Zähler angegeben sind, ist der Tarif nicht an das Vorhandensein bestimmter Zähler gebunden.) """
    einschraenkungleistung: List[Menge] = None
    """ Die vereinbarte Leistung, die (näherungsweise) abgenommen wird.
    Insbesondere Gastarife können daran gebunden sein, dass die Leistung einer vereinbarten Höhe entspricht. """
