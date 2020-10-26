from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass
class _GeschaeftsobjektBase:
    pass
    # bo_typ: str


@dataclass
class _GeschaeftsobjektDefaultBase:
    versionstruktur = 1


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Geschaeftsobjekt(_GeschaeftsobjektDefaultBase, _GeschaeftsobjektBase):
    """
    base class for all business objects
    """

    # why all the boilerplate?
    # https://bugs.python.org/issue39300
    # https://stackoverflow.com/a/53085935/10009545
