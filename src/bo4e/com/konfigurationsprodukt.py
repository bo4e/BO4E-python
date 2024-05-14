"""
Contains Konfigurationsprodukt class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

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

    produktcode: Optional[str] = None
    leistungskurvendefinition: Optional[str] = None
    schaltzeitdefinition: Optional[str] = None
    marktpartner: Optional["Marktteilnehmer"] = None
