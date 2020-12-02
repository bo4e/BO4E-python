import attr
import jsons

from bo4e.com.com import COM


@attr.s(auto_attribs=True, kw_only=True)
class ExterneReferenz(COM, jsons.JsonSerializable):
    """
    Viele Datenobjekte weisen in unterschiedlichen Systemen eine eindeutige ID (Kundennummer, GP-Nummer etc.) auf. Beim Austausch von Datenobjekten zwischen verschiedenen Systemen ist es daher hilfreich, sich die eindeutigen IDs der anzubindenden Systeme zu merken.
    """

    # required attributes
    ex_ref_name: str
    ex_ref_wert: str
