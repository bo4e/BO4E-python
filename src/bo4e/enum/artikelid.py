# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class ArtikelId(StrEnum):
    """
    Liste von Artikel-IDs, z.B. für standardisierte vom BDEW herausgegebene Artikel,
    die im Strommarkt die BDEW-Artikelnummer ablösen
    """

    # von allen enums ist das hier wohl das mit den unpassendsten Namen ;)

    Artikel2017001 = "2-01-7-001"  #: Unterbrechung der Anschlussnutzung in der regulären Arbeitszeit (€/Auftrag)
    Artikel2017002 = "2-01-7-002"  #: Wiederherstellung der Anschlussnutzung in der regulären Arbeitszeit (€/Auftrag)
    Artikel2017003 = "2-01-7-003"  #: Erfolglose Unterbrechung (€/Auftrag)
    #: Stornierung eines Auftrages zur Unterbrechung der Anschlussnutzung bis zum Vortag der Sperrung (€/Auftrag)
    Artikel2017004 = "2-01-7-004"
    #: Stornierung eines Auftrages zur Unterbrechung der Anschlussnutzung am Tag der Sperrung (€/Auftrag)
    Artikel2017005 = "2-01-7-005"
    #: Wiederherstellung der Anschlussnutzung außerhalb der regulären Arbeitszeit (€/Auftrag)
    Artikel2017006 = "2-01-7-006"
    Artikel2020001 = "2-02-0-001"  #: Verzugskosten pauschal (€/Fall)
    Artikel2020002 = "2-02-0-002"  #: Verzugskosten variabel (€)
