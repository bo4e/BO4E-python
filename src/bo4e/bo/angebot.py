"""
Contains Angebot class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from annotated_types import Len
from pydantic import Field

from bo4e.bo.ansprechpartner import Ansprechpartner
from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.angebotsvariante import Angebotsvariante
from bo4e.enum.botyp import BoTyp
from bo4e.enum.sparte import Sparte


class Angebot(Geschaeftsobjekt):
    """
    Mit diesem BO kann ein Versorgungsangebot zur Strom- oder Gasversorgung oder die Teilnahme an einer Ausschreibung
    übertragen werden. Es können verschiedene Varianten enthalten sein (z.B. ein- und mehrjährige Laufzeit).
    Innerhalb jeder Variante können Teile enthalten sein, die jeweils für eine oder mehrere Marktlokationen erstellt
    werden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Angebot.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebot JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Angebot.json>`_


    """

    bo_typ: BoTyp = BoTyp.ANGEBOT
    # required attributes
    #: Eindeutige Nummer des Angebotes
    angebotsnummer: Annotated[str, Field(strict=True, pattern=r"^\d+$")]
    #: Erstellungsdatum des Angebots
    angebotsdatum: datetime
    #: Sparte, für die das Angebot abgegeben wird (Strom/Gas)
    sparte: Sparte
    #: Ersteller des Angebots
    angebotsgeber: Geschaeftspartner
    #: Empfänger des Angebots
    angebotsnehmer: Geschaeftspartner

    varianten: Annotated[list[Angebotsvariante], Len(1)]
    """ Eine oder mehrere Varianten des Angebots mit den Angebotsteilen;
    Ein Angebot besteht mindestens aus einer Variante."""

    # optional attributes
    anfragereferenz: Optional[str] = None
    """	Referenz auf eine Anfrage oder Ausschreibung;
    Kann dem Empfänger des Angebotes bei Zuordnung des Angebotes zur Anfrage bzw. Ausschreibung helfen."""
    #: Bis zu diesem Zeitpunkt (Tag/Uhrzeit) inklusive gilt das Angebot
    bindefrist: Optional[datetime] = None
    #: Person, die als Angebotsnehmer das Angebot angenommen hat
    unterzeichner_angebotsnehmer: Optional[Ansprechpartner] = None
    #: Person, die als Angebotsgeber das Angebots ausgestellt hat
    unterzeichner_angebotsgeber: Optional[Ansprechpartner] = None
