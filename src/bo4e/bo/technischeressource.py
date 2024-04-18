"""
Contains technische Ressource class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Annotated, Optional

from pydantic import Field

from ..com.menge import Menge
from ..enum.emobilitaetsart import EMobilitaetsart
from ..enum.erzeugungsart import Erzeugungsart
from ..enum.speicherart import Speicherart
from ..enum.technischeressourcenutzung import TechnischeRessourceNutzung
from ..enum.technischeressourceverbrauchsart import TechnischeRessourceVerbrauchsart
from ..enum.typ import Typ
from ..enum.waermenutzung import Waermenutzung
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class TechnischeRessource(Geschaeftsobjekt):
    """
    Object containing information about a technische Ressource

    .. raw:: html

        <object data="../_static/images/bo4e/bo/TechnischeRessource.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/TechnischeRessource.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.TECHNISCHERESSOURCE

    id: Optional[str] = None
    vorgelagerte_messlokation_id: Optional[str] = None
    zugeordnete_marktlokation_id: Optional[str] = None
    nennleistungaufnahme: Optional[Menge] = None
    nennleistungabgabe: Optional[Menge] = None
    speicherkapazitaet: Optional[Menge] = None
    technische_ressource_nutzung: Optional[TechnischeRessourceNutzung] = None
    technische_ressource_verbrauchsart: Optional[TechnischeRessourceVerbrauchsart] = None
    waermenutzung: Optional[Waermenutzung] = None
    emobilitaetsart: Optional[EMobilitaetsart] = None
    erzeugungsart: Optional[Erzeugungsart] = None
    speicherart: Optional[Speicherart] = None
