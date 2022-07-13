"""
Contains Fremdkosten class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

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

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Fremdkosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Fremdkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Fremdkosten.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.FREMDKOSTEN
    #: Für diesen Zeitraum wurden die Kosten ermittelt
    gueltigkeit: Zeitraum
    # optional attributes
    #: Die Gesamtsumme über alle Kostenblöcke und -positionen
    summe_kosten: Optional[Betrag] = None
    #: In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc
    kostenbloecke: Optional[List[Fremdkostenblock]] = None
