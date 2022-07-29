"""
Contains Geschaeftspartner class
and corresponding marshmallow schema for de-/serialization
"""
# pylint: disable=too-many-instance-attributes, too-few-public-methods
from typing import List, Optional

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.adresse import Adresse
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart


class Geschaeftspartner(Geschaeftsobjekt):
    """
    Mit diesem Objekt können Geschäftspartner übertragen werden.
    Sowohl Unternehmen, als auch Privatpersonen können Geschäftspartner sein.
    Hinweis: Marktteilnehmer haben ein eigenes BO, welches sich von diesem BO ableitet.
    Hier sollte daher keine Zuordnung zu Marktrollen erfolgen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geschaeftspartner.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geschaeftspartner JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Geschaeftspartner.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.GESCHAEFTSPARTNER
    name1: str
    """
    Erster Teil des Namens.
    Hier kann der Firmenname oder bei Privatpersonen beispielsweise der Nachname dagestellt werden.
    Beispiele: Yellow Strom GmbH oder Hagen
    """
    # todo: replace name1/2/3 with something more readable. no one wants to deal with that. maybe serialize as name1/2/3
    # but resolve to readable python fields under the hood

    gewerbekennzeichnung: bool
    """
    Kennzeichnung ob es sich um einen Gewerbe/Unternehmen (gewerbeKennzeichnung = true)
    oder eine Privatperson handelt. (gewerbeKennzeichnung = false)
    """
    #: Rollen, die die Geschäftspartner inne haben (z.B. Interessent, Kunde)
    geschaeftspartnerrolle: List[Geschaeftspartnerrolle]
    # todo: rename to plural

    # optional attributes
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
    kontaktweg: Optional[List[Kontaktart]] = []
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
