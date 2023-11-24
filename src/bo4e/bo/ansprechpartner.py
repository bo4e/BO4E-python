"""
Contains Ansprechpartner class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..com.adresse import Adresse
from ..com.rufnummer import Rufnummer
from ..com.zustaendigkeit import Zustaendigkeit
from ..enum.anrede import Anrede
from ..enum.titel import Titel
from ..enum.typ import Typ
from .geschaeftsobjekt import Geschaeftsobjekt
from .geschaeftspartner import Geschaeftspartner

# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Ansprechpartner(Geschaeftsobjekt):
    """
    Object containing information about a Ansprechpartner

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Ansprechpartner.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ansprechpartner JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Ansprechpartner.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.ANSPRECHPARTNER
    nachname: Optional[str] = None  #: Nachname (Familienname) des Ansprechpartners
    geschaeftspartner: Optional[
        Geschaeftspartner
    ] = None  #: Der Geschäftspartner, für den dieser Ansprechpartner modelliert wird

    anrede: Optional[Anrede] = None  #: Mögliche Anrede des Ansprechpartners
    individuelle_anrede: Optional[str] = None
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Sehr geehrte Frau Müller, sehr geehrter Herr Dr. Müller"
    """

    titel: Optional[Titel] = None  #: Möglicher Titel des Ansprechpartners
    vorname: Optional[str] = None  #: Vorname des Ansprechpartners
    e_mail_adresse: Optional[str] = None  #: E-Mail Adresse
    kommentar: Optional[str] = None  #: Weitere Informationen zum Ansprechpartner
    #: Adresse des Ansprechpartners, falls diese von der Adresse des Geschäftspartners abweicht
    adresse: Optional[Adresse] = None
    #: Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist
    rufnummer: Optional[Rufnummer] = None  # todo: make this a list and rename to rufnummern
    #: Liste der Abteilungen und Zuständigkeiten des Ansprechpartners
    zustaendigkeit: Optional[Zustaendigkeit] = None  # todo: make this a list and rename to "zustaendigkeiten"
