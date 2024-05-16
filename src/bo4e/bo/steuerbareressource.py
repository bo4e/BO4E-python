"""
Contains steuerbare Ressource class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.konfigurationsprodukt import Konfigurationsprodukt
    from ..enum.marktrolle import Marktrolle
    from ..enum.steuerkanalsleistungsbeschreibung import SteuerkanalsLeistungsbeschreibung

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class SteuerbareRessource(Geschaeftsobjekt):
    """
    Object containing information about a steuerbare Ressource

    .. raw:: html

        <object data="../_static/images/bo4e/bo/SteuerbareRessource.svg" type="image/svg+xml"></object>

    .. HINT::
        `SteuerbareRessource JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/SteuerbareRessource.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.STEUERBARERESSOURCE

    #: Id der steuerbaren Ressource
    steuerbare_ressource_id: Optional[str] = None
    #: Leistungsbeschreibung des Steuerkanals
    steuerkanal_leistungsbeschreibung: Optional["SteuerkanalLeistungsbeschreibung"] = None
    #: Angabe des Messstellenbetreibers, der der Steuerbaren Ressource zugeordnet ist.
    zugeordnete_msb_codenr: Optional[str] = None
    #: Produkt-Daten der Steuerbaren Ressource
    konfigurationsprodukte: Optional[list["Konfigurationsprodukt"]] = None
    #: Eigenschaft des Messstellenbetreibers an der Lokation
    eigenschaft_msb_lokation: Optional["Marktrolle"] = None
