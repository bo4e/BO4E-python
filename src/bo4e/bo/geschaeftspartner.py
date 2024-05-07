"""
Contains Geschaeftspartner class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-many-instance-attributes, too-few-public-methods, disable=duplicate-code
from typing import TYPE_CHECKING, Annotated, Optional

from pydantic import Field

from ..enum.typ import Typ
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

    typ: Annotated[Optional["Typ"], Field(alias="_typ")] = Typ.GESCHAEFTSPARTNER
    #: Mögliche Anrede der Person
    anrede: Optional["Anrede"] = None
    individuelle_anrede: Optional[str] = None
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Vereinsgemeinschaft", "Pfarrer", "Hochwürdigster Herr Abt".
    """
    #: Möglicher Titel der Person
    titel: Optional["Titel"] = None
    #: Vorname der Person
    vorname: Optional[str] = None
    #: Nachname (Familienname) der Person
    nachname: Optional[str] = None

    ansprechpartner: Optional[list["Person"]] = None
    organisationstyp: Optional["Organisationstyp"] = None
    """
    Kennzeichnung ob es sich um ein Gewerbe/Unternehmen, eine Privatperson oder eine andere Art von Organisation handelt.
    """
    organisationsname: Optional[str] = None
    """
    Name der Firma, wenn Gewerbe oder andere Organisation.
    """
    #: Kontaktwege des Geschäftspartners
    kontaktwege: Optional[list["Kontaktweg"]] = None
    #: Rollen, die die Geschäftspartner inne haben (z.B. Interessent, Kunde)
    geschaeftspartnerrollen: Optional[list["Geschaeftspartnerrolle"]] = None
    #: Handelsregisternummer des Geschäftspartners
    handelsregisternummer: Optional[str] = None
    #: Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat
    amtsgericht: Optional[str] = None
    #: Die Steuer-ID des Geschäftspartners; Beispiel: "DE 813281825"
    umsatzsteuer_id: Optional[str] = None
    #: Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird; Z.B. "DE 47116789"
    glaeubiger_id: Optional[str] = None
    #: Internetseite des Marktpartners
    website: Optional[str] = None
    #: Adresse des Geschäftspartners
    adresse: Optional["Adresse"] = None
    #: Todo: Add optional connection to marktteilnehmer as discussed in workshop
    #: not clear what is the best solution here - circular import marktteilnehmer?
    #: discussed in workshop on Feb 6 2024: yes we need the bidirectional option, let's figure out a solution somehow.
