"""
Contains technische Ressource class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..bo.lokationszuordnung import Lokationszuordnung
    from ..com.menge import Menge
    from ..enum.emobilitaetsart import EMobilitaetsart
    from ..enum.erzeugungsart import Erzeugungsart
    from ..enum.speicherart import Speicherart
    from ..enum.technischeressourcenutzung import TechnischeRessourceNutzung
    from ..enum.technischeressourceverbrauchsart import TechnischeRessourceVerbrauchsart
    from ..enum.waermenutzung import Waermenutzung

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class TechnischeRessource(Geschaeftsobjekt):
    """
    Object containing information about a technische Ressource

    .. raw:: html

        <object data="../_static/images/bo4e/bo/TechnischeRessource.svg" type="image/svg+xml"></object>

    .. HINT::
        `TechnischeRessource JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/TechnischeRessource.json>`_

    """

    typ: Annotated[Literal[Typ.TECHNISCHERESSOURCE], Field(alias="_typ")] = Typ.TECHNISCHERESSOURCE

    technische_ressource_id: Optional[str] = None
    """Identifikationsnummer einer technischen Ressource"""
    vorgelagerte_messlokation_id: Optional[str] = None
    """Vorgelagerte Messlokation ID"""
    zugeordnete_marktlokation_id: Optional[str] = None
    """Referenz auf die der technischen Ressource zugeordneten Marktlokation"""
    zugeordnete_steuerbare_ressource_id: Optional[str] = None
    """Referenz auf die der technischen Ressource zugeordneten Steuerbaren Ressource"""
    nennleistungaufnahme: Optional["Menge"] = None
    """Nennleistung (Aufnahme)"""
    nennleistungabgabe: Optional["Menge"] = None
    """Nennleistung (Abgabe)"""
    speicherkapazitaet: Optional["Menge"] = None
    """Speicherkapazität"""
    technische_ressource_nutzung: Optional["TechnischeRessourceNutzung"] = None
    """Art und Nutzung der technischen Ressource"""
    technische_ressource_verbrauchsart: Optional["TechnischeRessourceVerbrauchsart"] = None
    """Verbrauchsart der technischen Ressource"""
    waermenutzung: Optional["Waermenutzung"] = None
    """Wärmenutzung"""
    emobilitaetsart: Optional["EMobilitaetsart"] = None
    """Art der E-Mobilität"""
    erzeugungsart: Optional["Erzeugungsart"] = None
    """Art der Erzeugung der Energie"""
    speicherart: Optional["Speicherart"] = None
    """Art des Speichers"""
    lokationszuordnungen: Optional[list["Lokationszuordnung"]] = None
    """Lokationszuordnung, um bspw. die zugehörigen Messlokationen anzugeben"""
    lokationsbuendel_objektcode: Optional[str] = None
    """Lokationsbuendel Code, der die Funktion dieses BOs an der Lokationsbuendelstruktur beschreibt."""
