"""
Contains Geschaeftspartner class
and corresponding marshmallow schema for de-/serialization
"""
# pylint: disable=too-many-instance-attributes, too-few-public-methods
from typing import Annotated, Optional

from pydantic import Field

from ..com.adresse import Adresse
from ..enum.anrede import Anrede
from ..enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from ..enum.kontaktart import Kontaktart
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt


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
    name1: Optional[str] = None
    """
    Erster Teil des Namens.
    Hier kann der Firmenname oder bei Privatpersonen beispielsweise der Nachname dagestellt werden.
    Beispiele: Yellow Strom GmbH oder Hagen
    """
    # todo: replace name1/2/3 with something more readable. no one wants to deal with that. maybe serialize as name1/2/3
    # but resolve to readable python fields under the hood

    ist_gewerbe: Optional[bool] = None
    """
    Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (istGewerbe = true)
    oder eine Privatperson handelt. (istGewerbe = false)
    """
    #: Rollen, die die Geschäftspartner inne haben (z.B. Interessent, Kunde)
    geschaeftspartnerrolle: Optional[list[Geschaeftspartnerrolle]] = None
    # todo: rename to plural

    #: Die Anrede für den GePa, Z.B. "Herr"
    anrede: Optional[Anrede] = None
    name2: Optional[str] = None
    """
    Zweiter Teil des Namens.
    Hier kann der eine Erweiterung zum Firmennamen oder bei Privatpersonen beispielsweise der Vorname dagestellt werden.
    Beispiele: Bereich Süd oder Nina
    """

    name3: Optional[str] = None
    """
    Dritter Teil des Namens.
    Hier können weitere Ergänzungen zum Firmennamen oder bei Privatpersonen Zusätze zum Namen dagestellt werden.
    Beispiele: und Afrika oder Sängerin
    """
    #: Handelsregisternummer des Geschäftspartners
    hrnummer: Optional[str] = None
    #: Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat
    amtsgericht: Optional[str] = None
    #: Bevorzugte Kontaktwege des Geschäftspartners
    kontaktweg: Optional[list[Kontaktart]] = None
    #: Die Steuer-ID des Geschäftspartners; Beispiel: "DE 813281825"
    umsatzsteuer_id: Optional[str] = None
    #: Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird; Z.B. "DE 47116789"
    glaeubiger_id: Optional[str] = None
    #: E-Mail-Adresse des Ansprechpartners. Z.B. "info@hochfrequenz.de"
    e_mail_adresse: Optional[str] = None
    #: Internetseite des Marktpartners
    website: Optional[str] = None
    #: Adressen der Geschäftspartner, an denen sich der Hauptsitz befindet
    partneradresse: Optional[Adresse] = None  # todo: is it plural or not? the docs are bad
    #: Todo: Add optional connection to marktteilnehmer as discussed in workshop
