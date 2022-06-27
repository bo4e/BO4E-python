"""
Contains Kostenblock and corresponding marshmallow schema for de-/serialization
"""
from typing import List

from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.kostenposition import Kostenposition


# pylint: disable=too-few-public-methods


class Kostenblock(COM):
    """
    Mit dieser Komponente werden mehrere Kostenpositionen zusammengefasst.

    .. graphviz:: /api/dots/bo4e/com/Kostenblock.dot

    """

    # required attributes
    #: Bezeichnung für einen Kostenblock. Z.B. Netzkosten, Messkosten, Umlagen, etc.
    kostenblockbezeichnung: str

    # optional attributes
    #: Die Summe aller Kostenpositionen dieses Blocks
    summe_kostenblock: Betrag = None

    kostenpositionen: List[Kostenposition] = None
    """
    Hier sind die Details zu einer Kostenposition aufgeführt. Z.B.:
    Alliander Netz Heinsberg GmbH, 01.02.2018, 31.12.2018, Arbeitspreis HT, 3.660 kWh, 5,8200 ct/kWh, 213,01 €
    """
