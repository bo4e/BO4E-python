"""
Contains RegionaleTarifpreisposition class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Optional

from ..enum.mengeneinheit import Mengeneinheit
from ..enum.preistyp import Preistyp
from ..enum.waehrungseinheit import Waehrungseinheit
from ..utils import postprocess_docstring
from .com import COM
from .regionalepreisstaffel import RegionalePreisstaffel


@postprocess_docstring
class RegionaleTarifpreisposition(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen im Zusammenhang mit regionalen Gültigkeiten abgebildet
    werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionaleTarifpreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionaleTarifpreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/RegionaleTarifpreisposition.json>`_

    """

    #: Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Optional[Preistyp] = None
    #: Einheit des Preises (z.B. EURO)
    einheit: Optional[Waehrungseinheit] = None
    #: Größe, auf die sich die Einheit bezieht, beispielsweise kWh, Jahr
    bezugseinheit: Optional[Mengeneinheit] = None
    #: Hier sind die Staffeln mit ihren Preisangaben und regionalen Gültigkeiten definiert
    preisstaffeln: Optional[list[RegionalePreisstaffel]] = None

    #: Gibt an, nach welcher Menge die vorgenannte Einschränkung erfolgt (z.B. Jahresstromverbrauch in kWh)
    mengeneinheitstaffel: Optional[Mengeneinheit] = None
