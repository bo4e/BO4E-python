"""
Contains Person class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

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

    typ: Annotated[Literal[Typ.PERSON], Field(alias="_typ")] = Typ.PERSON
    anrede: Optional["Anrede"] = None
    """Mögliche Anrede der Person"""
    individuelle_anrede: Optional[str] = None
    """
    Im Falle einer nicht standardisierten Anrede kann hier eine frei definierbare Anrede vorgegeben werden.
    Beispiel: "Vereinsgemeinschaft", "Pfarrer", "Hochwürdigster Herr Abt".
    """
    titel: Optional["Titel"] = None
    """Möglicher Titel der Person"""
    vorname: Optional[str] = None
    """Vorname der Person"""
    nachname: Optional[str] = None
    """Nachname (Familienname) der Person"""
    kontaktwege: Optional[list["Kontaktweg"]] = None
    """Kontaktwege der Person"""
    geburtsdatum: Optional[pydantic.AwareDatetime] = None
    """Geburtsdatum der Person"""
    kommentar: Optional[str] = None
    """Weitere Informationen zur Person"""
    zustaendigkeiten: Optional[list["Zustaendigkeit"]] = None
    """Liste der Abteilungen und Zuständigkeiten der Person"""
    adresse: Optional["Adresse"] = None
    """Adresse der Person, falls diese von der Adresse des Geschäftspartners abweicht"""
