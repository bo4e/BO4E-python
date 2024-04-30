"""
Contains steuerbare Ressource class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Annotated, Optional

from pydantic import Field

from ..com.konfigurationsprodukt import Konfigurationsprodukt
from ..enum.marktrolle import Marktrolle
from ..enum.steuerkanalsleistungsbeschreibung import SteuerkanalsLeistungsbeschreibung
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class SteuerbareRessource(Geschaeftsobjekt):
    """
    Object containing information about a steuerbare Ressource

    .. raw:: html

        <object data="../_static/images/bo4e/bo/SteuerbareRessource.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/SteuerbareRessource.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.STEUERBARERESSOURCE

    steuerbare_ressource_id: Optional[str] = None
    steuerkanals_leistungsbeschreibung: Optional[SteuerkanalsLeistungsbeschreibung] = None
    zugeordnete_msb_codenr: Optional[str] = None
    konfigurationsprodukte: Optional[list[Konfigurationsprodukt]] = None
    eigenschaft_msb_lokation: Optional[Marktrolle] = None
