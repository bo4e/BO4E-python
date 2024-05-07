"""
Contains Person class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Optional

import pydantic
from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.adresse import Adresse
    from ..com.kontaktweg import Kontaktweg
    from ..com.zustaendigkeit import Zustaendigkeit
    from ..enum.anrede import Anrede
    from ..enum.titel import Titel


# pylint: disable=too-many-instance-attributes, too-few-public-methods, disable=duplicate-code


@postprocess_docstring
class Person(Geschaeftsobjekt):
    """
    Object containing information about a Person

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Person.svg" type="image/svg+xml"></object>

    .. HINT::
        `Person JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Person.json>`_

    """

    typ: Annotated[Optional["Typ"], Field(alias="_typ")] = Typ.PERSON
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
    #: Kontaktwege der Person
    kontaktwege: Optional[list["Kontaktweg"]] = None
    #: Geburtsdatum der Person
    geburtsdatum: Optional[pydantic.AwareDatetime] = None
    #: Weitere Informationen zur Person
    kommentar: Optional[str] = None
    #: Liste der Abteilungen und Zuständigkeiten der Person
    zustaendigkeiten: Optional[list["Zustaendigkeit"]] = None
    #: Adresse der Person, falls diese von der Adresse des Geschäftspartners abweicht
    adresse: Optional["Adresse"] = None
