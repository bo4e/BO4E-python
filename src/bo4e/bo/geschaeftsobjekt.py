from typing import List, Optional

import attr

from bo4e.com.externereferenz import ExterneReferenz
from bo4e.enum.botyp import BoTyp


@attr.s(auto_attribs=True, kw_only=True)
class Geschaeftsobjekt:
    """
    base class for all business objects
    """

    versionstruktur: int = attr.ib(default=2)
    bo_typ: BoTyp
    externe_referenzen: Optional[List[ExterneReferenz]] = attr.ib(
        default=None, validator=attr.validators.instance_of((type(None), List))
    )
