"""
Contains Tarifeinschraenkung and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

from bo4e.com.com import COM
from bo4e.com.geraet import Geraet
from bo4e.com.menge import Menge
from bo4e.enum.voraussetzungen import Voraussetzungen

# pylint: disable=too-few-public-methods


class Tarifeinschraenkung(COM):
    """
    Mit dieser Komponente werden Einschränkungen für die Anwendung von Tarifen modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifeinschraenkung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifeinschraenkung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Tarifeinschraenkung.json>`_

    """

    # optional attributes
    #: Weitere Produkte, die gemeinsam mit diesem Tarif bestellt werden können
    zusatzprodukte: Optional[List[str]] = None
    #: Voraussetzungen, die erfüllt sein müssen, damit dieser Tarif zur Anwendung kommen kann
    voraussetzungen: Optional[List[Voraussetzungen]] = None
    einschraenkungzaehler: Optional[List[Geraet]] = None
    """ Liste der Zähler/Geräte, die erforderlich sind, damit dieser Tarif zur Anwendung gelangen kann.
    (Falls keine Zähler angegeben sind, ist der Tarif nicht an das Vorhandensein bestimmter Zähler gebunden.) """
    einschraenkungleistung: Optional[List[Menge]] = None
    """ Die vereinbarte Leistung, die (näherungsweise) abgenommen wird.
    Insbesondere Gastarife können daran gebunden sein, dass die Leistung einer vereinbarten Höhe entspricht. """
