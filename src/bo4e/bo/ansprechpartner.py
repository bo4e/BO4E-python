"""
Contains Ansprechpartner class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.com.rufnummer import Rufnummer
from bo4e.com.zustaendigkeit import Zustaendigkeit
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.titel import Titel


# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Ansprechpartner(Geschaeftsobjekt):
    """
    Object containing information about a Ansprechpartner

    .. graphviz:: /api/dots/bo4e/bo/Ansprechpartner.dot

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.ANSPRECHPARTNER
    nachname: str  #: Nachname (Familienname) des Ansprechpartners
    geschaeftspartner: Geschaeftspartner  #: Der Geschäftspartner, für den dieser Ansprechpartner modelliert wird

    # optional attributes
    anrede: Anrede = None  #: Mögliche Anrede des Ansprechpartners
    individuelle_anrede: str = None
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Sehr geehrte Frau Müller, sehr geehrter Herr Dr. Müller"
    """

    titel: Titel = None  #: Möglicher Titel des Ansprechpartners
    vorname: str = None  #: Vorname des Ansprechpartners
    e_mail_adresse: str = None  #: E-Mail Adresse
    kommentar: str = None  #: Weitere Informationen zum Ansprechpartner
    #: Adresse des Ansprechpartners, falls diese von der Adresse des Geschäftspartners abweicht
    adresse: Adresse = None
    #: Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist
    rufnummer: Rufnummer = None  # todo: make this a list and rename to rufnummern
    #: Liste der Abteilungen und Zuständigkeiten des Ansprechpartners
    zustaendigkeit: Zustaendigkeit = None  # todo: make this a list and rename to "zustaendigkeiten"
