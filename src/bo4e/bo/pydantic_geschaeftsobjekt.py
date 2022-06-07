from typing import List, Optional

from bo4e.enum.botyp import BoTyp
from pydantic import BaseModel
from bo4e.com.pydantic_externereferenz import ExterneReferenz


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
