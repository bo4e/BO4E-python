"""
Contains Geschaeftspartner class
and corresponding marshmallow schema for de-/serialization
"""
# pylint: disable=too-many-instance-attributes, too-few-public-methods
from typing import Annotated, Optional

from pydantic import Field

from ..com.adresse import Adresse
from ..com.kontakt import Kontakt
from ..enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt
from .person import Person


@postprocess_docstring
class Geschaeftspartner(Geschaeftsobjekt):
    """
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein.
    Hinweis: Marktteilnehmer haben ein eigenes BO, welches sich von diesem BO ableitet.
    Hier sollte daher keine Zuordnung zu Marktrollen erfolgen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geschaeftspartner.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geschaeftspartner JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Geschaeftspartner.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.GESCHAEFTSPARTNER
    ansprechpartner: Optional[list[Person]] = None
    ist_gewerbe: Optional[bool] = None
    """
    Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (istGewerbe = true)
    oder eine Privatperson handelt. (istGewerbe = false)
    """
    #: Name der Firma, wenn Gewerbe
    firmenname: Optional[str] = None
    #: Bevorzugte Kontaktwege des Geschäftspartners
    kontaktwege: Optional[list[Kontakt]] = None
    #: Rollen, die die Geschäftspartner inne haben (z.B. Interessent, Kunde)
    geschaeftspartnerrollen: Optional[list[Geschaeftspartnerrolle]] = None
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
    #: Adressen der Geschäftspartner, an denen sich der Hauptsitz befindet
    partneradresse: Optional[Adresse] = None  # todo: is it plural or not? the docs are bad
    #: Todo: Add optional connection to marktteilnehmer as discussed in workshop
    #: not clear what is the best solution here - circular import marktteilnehmer or adresse in kontakt?
