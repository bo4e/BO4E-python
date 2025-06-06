"""
Contains Angebot class
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.angebotsvariante import Angebotsvariante
    from ..enum.sparte import Sparte
    from .geschaeftspartner import Geschaeftspartner
    from .person import Person


@postprocess_docstring
class Angebot(Geschaeftsobjekt):
    """
    Mit diesem BO kann ein Versorgungsangebot zur Strom- oder Gasversorgung oder die Teilnahme an einer Ausschreibung
    übertragen werden. Es können verschiedene Varianten enthalten sein (z.B. ein- und mehrjährige Laufzeit).
    Innerhalb jeder Variante können Teile enthalten sein, die jeweils für eine oder mehrere Marktlokationen erstellt
    werden.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Angebot.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebot JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Angebot.json>`_


    """

    typ: Annotated[Literal[BoTyp.ANGEBOT], Field(alias="_typ")] = BoTyp.ANGEBOT
    angebotsnummer: Optional[str] = None
    """Eindeutige Nummer des Angebotes"""
    angebotsdatum: Optional[pydantic.AwareDatetime] = None
    """Erstellungsdatum des Angebots"""
    sparte: Optional["Sparte"] = None
    """Sparte, für die das Angebot abgegeben wird (Strom/Gas)"""
    angebotsgeber: Optional["Geschaeftspartner"] = None
    """Ersteller des Angebots"""
    angebotsnehmer: Optional["Geschaeftspartner"] = None
    """Empfänger des Angebots"""

    varianten: Optional[list["Angebotsvariante"]] = None
    """
    Eine oder mehrere Varianten des Angebots mit den Angebotsteilen;
    Ein Angebot besteht mindestens aus einer Variante.
    """

    anfragereferenz: Optional[str] = None
    """
    Referenz auf eine Anfrage oder Ausschreibung;
    Kann dem Empfänger des Angebotes bei Zuordnung des Angebotes zur Anfrage bzw. Ausschreibung helfen.
    """
    bindefrist: Optional[pydantic.AwareDatetime] = None
    """Bis zu diesem Zeitpunkt (Tag/Uhrzeit) inklusive gilt das Angebot"""
    unterzeichner_angebotsnehmer: Optional["Person"] = None
    """Person, die als Angebotsnehmer das Angebot angenommen hat"""
    unterzeichner_angebotsgeber: Optional["Person"] = None
    """Person, die als Angebotsgeber das Angebots ausgestellt hat"""
