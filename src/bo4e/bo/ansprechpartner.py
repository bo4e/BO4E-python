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
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt
from .geschaeftspartner import Geschaeftspartner

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Ansprechpartner(Geschaeftsobjekt):
    """
    Object containing information about a Ansprechpartner

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Ansprechpartner.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ansprechpartner JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Ansprechpartner.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.ANSPRECHPARTNER

    individuelle_anrede: Optional[str] = None
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Sehr geehrte Frau Müller, sehr geehrter Herr Dr. Müller"
    """
    anrede: Optional[Anrede] = None  #: Mögliche Anrede des Ansprechpartners
    titel: Optional[Titel] = None  #: Möglicher Titel des Ansprechpartners
    vorname: Optional[str] = None  #: Vorname des Ansprechpartners
    nachname: Optional[str] = None  #: Nachname (Familienname) des Ansprechpartners

    e_mail_adresse: Optional[str] = None  #: E-Mail Adresse

    geschaeftspartner: Optional[
        Geschaeftspartner
    ] = None  #: Der Geschäftspartner, für den dieser Ansprechpartner modelliert wird

    #: Adresse des Ansprechpartners, falls diese von der Adresse des Geschäftspartners abweicht
    adresse: Optional[Adresse] = None

    #: Liste der Telefonnummern, unter denen der Ansprechpartner erreichbar ist
    rufnummer: Optional[Rufnummer] = None  # todo: make this a list and rename to rufnummern

    kommentar: Optional[str] = None  #: Weitere Informationen zum Ansprechpartner

    #: Liste der Abteilungen und Zuständigkeiten des Ansprechpartners
    zustaendigkeit: Optional[Zustaendigkeit] = None  # todo: make this a list and rename to "zustaendigkeiten"
