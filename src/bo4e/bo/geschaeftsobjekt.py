from decimal import Decimal

from decimal import Decimal
from typing import List, Optional

from bo4e.enum.botyp import BoTyp
from pydantic import BaseModel, StrictStr
from bo4e.com.externereferenz import ExterneReferenz
from humps.main import camelize


class Geschaeftsobjekt(BaseModel):
    """
    Das BO Geschäftsobjekt ist der Master für alle Geschäftsobjekte.
    Alle Attribute, die hier in diesem BO enthalten sind, werden an alle BOs vererbt.
    """

    # required attributes
    versionstruktur: str = "2"  #: Version der BO-Struktur aka "fachliche Versionierung"
    bo_typ: BoTyp = BoTyp.GESCHAEFTSOBJEKT  #: Der Typ des Geschäftsobjektes
    # bo_typ is used as discriminator f.e. for databases or deserialization

    # optional attributes
    externe_referenzen: List[ExterneReferenz] = []
    #: Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
        json_encoders = {Decimal: str}
        use_enum_values = True  # Otherwise the dictionaries by obj.dict() would contain Enum-objects instead of strings
