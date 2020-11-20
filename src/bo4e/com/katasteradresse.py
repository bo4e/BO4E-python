import attr
import jsons

from bo4e.com.com import COM


@attr.s(auto_attribs=True, kw_only=True)
class Katasteradresse(COM, jsons.JsonSerializable):
    """
    Dient der Adressierung über die Liegenschafts-Information.
    """

    gemarkung_flur: str
    flurstueck: str
