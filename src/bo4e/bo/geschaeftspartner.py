"""
Contains Geschaeftspartner class
"""

# pylint: disable=too-many-instance-attributes, too-few-public-methods, disable=duplicate-code
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.adresse import Adresse
    from ..com.kontaktweg import Kontaktweg
    from ..enum.anrede import Anrede
    from ..enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
    from ..enum.organisationstyp import Organisationstyp
    from ..enum.titel import Titel
    from .person import Person


@postprocess_docstring
class Geschaeftspartner(Geschaeftsobjekt):
    """
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein.
    Hinweis: "Marktteilnehmer" haben ein eigenes BO, welches sich von diesem BO ableitet.
    Hier sollte daher keine Zuordnung zu Marktrollen erfolgen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geschaeftspartner.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geschaeftspartner JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Geschaeftspartner.json>`_

    """

    typ: Annotated[Literal[BoTyp.GESCHAEFTSPARTNER], Field(alias="_typ")] = BoTyp.GESCHAEFTSPARTNER
    anrede: Optional["Anrede"] = None
    """Mögliche Anrede der Person"""
    individuelle_anrede: str | None = None
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Vereinsgemeinschaft", "Pfarrer", "Hochwürdigster Herr Abt".
    """
    titel: Optional["Titel"] = None
    """Möglicher Titel der Person"""
    vorname: str | None = None
    """Vorname der Person"""
    nachname: str | None = None
    """Nachname (Familienname) der Person"""

    ansprechpartner: list["Person"] | None = None
    organisationstyp: Optional["Organisationstyp"] = None
    """
    Kennzeichnung ob es sich um ein Gewerbe/Unternehmen, eine Privatperson oder eine andere Art von Organisation handelt.
    """
    organisationsname: str | None = None
    """
    Name der Firma, wenn Gewerbe oder andere Organisation.
    """
    kontaktwege: list["Kontaktweg"] | None = None
    """Kontaktwege des Geschäftspartners"""
    geschaeftspartnerrollen: list["Geschaeftspartnerrolle"] | None = None
    """Rollen, die die Geschäftspartner inne haben (z.B. Interessent, Kunde)"""
    handelsregisternummer: str | None = None
    """Handelsregisternummer des Geschäftspartners"""
    amtsgericht: str | None = None
    """Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat"""
    umsatzsteuer_id: str | None = None
    """
    Die Steuer-ID des Geschäftspartners; Beispiel: "DE 813281825"
    """
    glaeubiger_id: str | None = None
    """
    Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird; Z.B. "DE 47116789"
    """
    website: str | None = None
    """Internetseite des Marktpartners"""
    adresse: Optional["Adresse"] = None
    """Adresse des Geschäftspartners"""
    # Todo: Add optional connection to marktteilnehmer as discussed in workshop
    # not clear what is the best solution here - circular import marktteilnehmer?
    # discussed in workshop on Feb 6 2024: yes we need the bidirectional option, let's figure out a solution somehow.
