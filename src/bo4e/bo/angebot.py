"""
Contains Angebot class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import List, Optional


from bo4e.bo.ansprechpartner import Ansprechpartner
from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.angebotsvariante import Angebotsvariante
from bo4e.enum.botyp import BoTyp
from bo4e.enum.sparte import Sparte


# pylint: disable=too-few-public-methods, too-many-instance-attributes
from pydantic import constr, conlist, StrictStr


class Angebot(Geschaeftsobjekt):
    """
    Mit diesem BO kann ein Versorgungsangebot zur Strom- oder Gasversorgung oder die Teilnahme an einer Ausschreibung
    übertragen werden. Es können verschiedene Varianten enthalten sein (z.B. ein- und mehrjährige Laufzeit).
    Innerhalb jeder Variante können Teile enthalten sein, die jeweils für eine oder mehrere Marktlokationen erstellt
    werden.

    .. HINT::
        `Angebot JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/AngebotSchema.json>`_

    """

    bo_typ: BoTyp = BoTyp.ANGEBOT
    # required attributes
    #: Eindeutige Nummer des Angebotes
    angebotsnummer: constr(strict=True, regex=r"^\d+$")
    #: Erstellungsdatum des Angebots
    angebotsdatum: datetime
    #: Sparte, für die das Angebot abgegeben wird (Strom/Gas)
    sparte: Sparte
    #: Ersteller des Angebots
    angebotsgeber: Geschaeftspartner
    #: Empfänger des Angebots
    angebotsnehmer: Geschaeftspartner

    varianten: conlist(Angebotsvariante, min_items=1)
    """ Eine oder mehrere Varianten des Angebots mit den Angebotsteilen;
    Ein Angebot besteht mindestens aus einer Variante."""

    # optional attributes
    anfragereferenz: str = None
    """	Referenz auf eine Anfrage oder Ausschreibung;
    Kann dem Empfänger des Angebotes bei Zuordnung des Angebotes zur Anfrage bzw. Ausschreibung helfen."""
    #: Bis zu diesem Zeitpunkt (Tag/Uhrzeit) inklusive gilt das Angebot
    bindefrist: datetime = None
    #: Person, die als Angebotsnehmer das Angebot angenommen hat
    unterzeichner_angebotsnehmer: Ansprechpartner = None
    #: Person, die als Angebotsgeber das Angebots ausgestellt hat
    unterzeichner_angebotsgeber: Ansprechpartner = None
