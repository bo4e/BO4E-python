"""
Contains Regionskriterium class and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..enum.gueltigkeitstyp import Gueltigkeitstyp
from ..enum.regionskriteriumtyp import Regionskriteriumtyp
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Regionskriterium(COM):
    """
    Komponente zur Abbildung eines Regionskriteriums

    .. raw:: html

        <object data="../_static/images/bo4e/com/Regionskriterium.svg" type="image/svg+xml"></object>

    .. HINT::
        `Regionskriterium JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Regionskriterium.json>`_

    """

    gueltigkeitstyp: Optional[
        Gueltigkeitstyp
    ] = None  #: Hier wird festgelegt, ob es sich um ein einschließendes oder ausschließendes Kriterium handelt.
    regionskriteriumtyp: Optional[
        Regionskriteriumtyp
    ] = None  #: Hier wird das Kriterium selbst angegeben, z.B. Bundesland.
    wert: Optional[str] = None
    """
    Der Wert, den das Kriterium annehmen kann, z.B. NRW.
    Im Falle des Regionskriteriumstyp BUNDESWEIT spielt dieser Wert keine Rolle.
    """
