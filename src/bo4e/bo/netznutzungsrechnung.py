"""
Contains Netznutzungsrechnung class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from pydantic import Field

from bo4e.bo.rechnung import Rechnung
from bo4e.enum.botyp import BoTyp
from bo4e.enum.nnrechnungsart import NNRechnungsart
from bo4e.enum.nnrechnungstyp import NNRechnungstyp
from bo4e.enum.sparte import Sparte


class Netznutzungsrechnung(Rechnung):
    """
    Modell für die Abbildung von Netznutzungsrechnungen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Netznutzungsrechnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Netznutzungsrechnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Netznutzungsrechnung.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.NETZNUTZUNGSRECHNUNG
    #: Sparte (Strom, Gas ...) für die die Rechnung ausgestellt ist
    sparte: Sparte
    absendercodenummer: Annotated[str, Field(strict=True, pattern=r"^\d{13}$")]
    """
    Die Rollencodenummer des Absenders (siehe :class:`Marktteilnehmer`).
    Über die Nummer können weitere Informationen zum Marktteilnehmer ermittelt werden.
    """
    empfaengercodenummer: Annotated[str, Field(strict=True, pattern=r"^\d{13}$")]
    """
    Die Rollencodenummer des Empfängers (siehe :class:`Marktteilnehmer`).
    Über die Nummer können weitere Informationen zum Marktteilnehmer ermittelt werden.
    """
    #: Aus der INVOIC entnommen
    nnrechnungsart: NNRechnungsart
    #: Aus der INVOIC entnommen
    nnrechnungstyp: NNRechnungstyp

    #: Kennzeichen, ob es sich um ein Original (true) oder eine Kopie handelt (false)
    original: bool
    #: Kennzeichen, ob es sich um eine simulierte Rechnung, z.B. zur Rechnungsprüfung handelt
    simuliert: bool

    # optional attributes
    lokations_id: Optional[str] = None
    """
    Die Markt- oder Messlokations-Identifikation (als Malo/Melo-Id) der Lokation, auf die sich die Rechnung bezieht
    """
