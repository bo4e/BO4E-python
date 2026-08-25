"""
Contains steuerbare Ressource class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..bo.lokationszuordnung import Lokationszuordnung
    from ..com.konfigurationsprodukt import Konfigurationsprodukt
    from ..enum.marktrolle import Marktrolle
    from ..enum.steuerkanalleistungsbeschreibung import SteuerkanalLeistungsbeschreibung

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

    typ: Annotated[Literal[BoTyp.STEUERBARERESSOURCE], Field(alias="_typ")] = BoTyp.STEUERBARERESSOURCE

    steuerbare_ressource_id: str | None = None
    """Id der steuerbaren Ressource"""
    steuerkanal_leistungsbeschreibung: Optional["SteuerkanalLeistungsbeschreibung"] = None
    """Leistungsbeschreibung des Steuerkanals"""
    zugeordnete_msb_codenummer: str | None = None
    """Angabe des Messstellenbetreibers, der der Steuerbaren Ressource zugeordnet ist."""
    konfigurationsprodukte: list["Konfigurationsprodukt"] | None = None
    """Produkt-Daten der Steuerbaren Ressource"""
    eigenschaft_msb_lokation: Optional["Marktrolle"] = None
    """Eigenschaft des Messstellenbetreibers an der Lokation"""
    lokationszuordnungen: list["Lokationszuordnung"] | None = None
    """Lokationszuordnung, um bspw. die zugehörigen Messlokationen anzugeben"""
    lokationsbuendel_objektcode: str | None = None
    """Lokationsbuendel Code, der die Funktion dieses BOs an der Lokationsbuendelstruktur beschreibt."""
