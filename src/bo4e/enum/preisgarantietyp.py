# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Preisgarantietyp(StrEnum):
    """
    Aufzählung der Möglichkeiten für die Vergabe von Preisgarantien
    """

    ALLE_PREISBESTANDTEILE_BRUTTO  #: Der Versorger gewährt eine Preisgarantie auf alle Preisbestandteile
    ALLE_PREISBESTANDTEILE_NETTO  #: Der Versorger gewährt eine Preisgarantie auf alle Preisbestandteile ohne die Umsatzsteuer
    PREISBESTANDTEILE_OHNE_ABGABEN  #: Der Versorger gewährt eine Preisgarantie auf alle Preisbestandteile ohne Abgaben (Energiesteuern, Umlagen, Abgaben)
    NUR_ENERGIEPREIS  #: Der Versorger garantiert ausschließlich den Energiepreis
