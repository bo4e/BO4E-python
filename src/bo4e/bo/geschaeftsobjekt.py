import attr

from bo4e.enum.botyp import BoTyp


@attr.s(auto_attribs=True, kw_only=True)
class Geschaeftsobjekt:
    """
    base class for all business objects
    """

    bo_typ: BoTyp
    versionstruktur: int = attr.ib(default=2)
