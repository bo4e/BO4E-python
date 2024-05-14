"""
Contains Konfigurationsprodukt class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..bo.marktteilnehmer import Marktteilnehmer


# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Konfigurationsprodukt(COM):
    """
    Object containing information about a Konfigurationsprodukt

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Konfigurationsprodukt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Konfigurationsprodukt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Konfigurationsprodukt.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.KONFIGURATIONSPRODUKT

    produktcode: Optional[str]
    leistungskurvendefinition: Optional[str]
    schaltzeitdefinition: Optional[str]
    marktpartner: Optional["Marktteilnehmer"]
