"""
Contains Fremdkostenblock class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

from pydantic import StrictStr

from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.fremdkostenposition import Fremdkostenposition


# pylint: disable=too-few-public-methods


class Fremdkostenblock(COM):
    """
    Komponente zur Abbildung eines Kostenblocks in den Fremdkosten

    .. HINT::
        `Fremdkostenblock JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/FremdkostenblockSchema.json>`_

    """

    # required attributes
    #: Bezeichnung für einen Kostenblock. Z.B. Netzkosten, Messkosten, Umlagen, etc.
    kostenblockbezeichnung: str

    # optional attributes
    kostenpositionen: List[Fremdkostenposition] = None
    """
    Hier sind die Details zu einer Kostenposition aufgeführt. Z.B.:
    Alliander Netz Heinsberg GmbH, 2018-02-01, 2019-01-01, Arbeitspreis HT, 3.660 kWh,
    5,8200 ct/kWh, 213,01 €
    """

    #: Die Summe aller Kostenpositionen dieses Blocks
    summe_kostenblock: Betrag = None
    # todo: write validator fo this sum, see https://github.com/Hochfrequenz/BO4E-python/issues/324
