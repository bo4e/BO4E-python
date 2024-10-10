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

    #: Identifikationsnummer einer technischen Ressource
    technische_ressource_id: Optional[str] = None
    #: Vorgelagerte Messlokation ID
    vorgelagerte_messlokation_id: Optional[str] = None
    #: Referenz auf die der technischen Ressource zugeordneten Marktlokation
    zugeordnete_marktlokation_id: Optional[str] = None
    #: Referenz auf die der technischen Ressource zugeordneten Steuerbaren Ressource
    zugeordnete_steuerbare_ressource_id: Optional[str] = None
    #: Nennleistung (Aufnahme)
    nennleistungaufnahme: Optional["Menge"] = None
    #: Nennleistung (Abgabe)
    nennleistungabgabe: Optional["Menge"] = None
    #: Speicherkapazität
    speicherkapazitaet: Optional["Menge"] = None
    #: Art und Nutzung der technischen Ressource
    technische_ressource_nutzung: Optional["TechnischeRessourceNutzung"] = None
    #: Verbrauchsart der technischen Ressource
    technische_ressource_verbrauchsart: Optional["TechnischeRessourceVerbrauchsart"] = None
    #: Wärmenutzung
    waermenutzung: Optional["Waermenutzung"] = None
    #: Art der E-Mobilität
    emobilitaetsart: Optional["EMobilitaetsart"] = None
    #: Art der Erzeugung der Energie
    erzeugungsart: Optional["Erzeugungsart"] = None
    #: Art des Speichers
    speicherart: Optional["Speicherart"] = None
    #: Lokationszuordnung, um bspw. die zugehörigen Messlokationen anzugeben
    lokationszuordnungen: Optional[list["Lokationszuordnung"]] = None
    #: Lokationsbuendel Code, der die Funktion dieses BOs an der Lokationsbuendelstruktur beschreibt.
    lokationsbuendel_objektcode: Optional[str] = None
