"""
Contains Fremdkosten class and corresponding marshmallow schema for de-/serialization
"""
from typing import List

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.betrag import Betrag
from bo4e.com.fremdkostenblock import Fremdkostenblock
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.botyp import BoTyp


# pylint: disable=too-few-public-methods


class Fremdkosten(Geschaeftsobjekt):
    """
    Mit diesem BO werden die Fremdkosten, beispielsweise für eine Angebotserstellung oder eine Rechnungsprüfung,
    übertragen.
    Die Fremdkosten enthalten dabei alle Kostenblöcke, die von anderen Marktteilnehmern oder Instanzen erhoben werden.

    .. HINT::
        `Fremdkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/FremdkostenSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.FREMDKOSTEN
    #: Für diesen Zeitraum wurden die Kosten ermittelt
    gueltigkeit: Zeitraum
    # optional attributes
    #: Die Gesamtsumme über alle Kostenblöcke und -positionen
    summe_kosten: Betrag = None
    #: In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc
    kostenbloecke: List[Fremdkostenblock] = None
