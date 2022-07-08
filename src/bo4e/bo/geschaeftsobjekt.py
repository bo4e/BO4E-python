# pylint: disable=missing-module-docstring
from decimal import Decimal
from typing import List, Optional

from humps.main import camelize

# pylint: disable=no-name-in-module
from pydantic import BaseModel

from bo4e.com.externereferenz import ExterneReferenz
from bo4e.enum.botyp import BoTyp

# pylint: disable=too-few-public-methods


class Geschaeftsobjekt(BaseModel):
    """
    Das BO Geschäftsobjekt ist der Master für alle Geschäftsobjekte.
    Alle Attribute, die hier in diesem BO enthalten sind, werden an alle BOs vererbt.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geschaeftsobjekt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geschaeftsobjekt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Geschaeftsobjekt.json>`_

    """

    # required attributes
    versionstruktur: str = "2"  #: Version der BO-Struktur aka "fachliche Versionierung"
    bo_typ: BoTyp = BoTyp.GESCHAEFTSOBJEKT  #: Der Typ des Geschäftsobjektes
    # bo_typ is used as discriminator f.e. for databases or deserialization

    # optional attributes
    externe_referenzen: Optional[List[ExterneReferenz]] = []
    #: Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)

    class Config:
        """
        basic configuration for pydantic's behaviour
        """

        alias_generator = camelize
        allow_population_by_field_name = True
        json_encoders = {Decimal: str}
