# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class KundengruppeKA(StrEnum):
    """
    Eine Aufzählung zur Einordnung für die Höhe der Konzessionsabgabe.
    """

    S_SCHWACHLAST  #: Strom Schwachlast-Kunde
    S_TARIF_25000  #: Strom Tarifkunde Gemeindegröße bis 25000 Einwohner
    S_TARIF_100000  #: Strom Tarifkunde Gemeindegröße bis 100000 Einwohner
    S_TARIF_500000  #: Strom Tarifkunde Gemeindegröße bis 500000 Einwohner
    S_TARIF_G_500000  #: Strom Tarifkunde Gemeindegröße größer 500000 Einwohner
    S_SONDERKUNDE  #: Strom Sonderkunde
    G_KOWA_25000  #: Gas Kochen und Wasser Tarifkunde Gemeindegröße bis 25000 Einwohner
    G_KOWA_100000  #: Gas Kochen und Wasser Tarifkunde Gemeindegröße bis 100000 Einwohner
    G_KOWA_500000  #: Gas Kochen und Wasser Tarifkunde Gemeindegröße bis 500000 Einwohner
    G_KOWA_G_500000  #: Gas Kochen und Wasser Tarifkunde Gemeindegröße größer 500000 Einwohner
    G_TARIF_25000  #: GasTarifkunde Gemeindegröße bis 25000 Einwohner
    G_TARIF_100000  #: GasTarifkunde Gemeindegröße bis 100000 Einwohner
    G_TARIF_500000  #: GasTarifkunde Gemeindegröße bis 500000 Einwohner
    G_TARIF_G_500000  #: GasTarifkunde Gemeindegröße größer 500000 Einwohner
    G_SONDERKUNDE  #: Gas Sonderkunde
    SONDER_KAS  #: Sonderegelung, keine Systematik der KAV
    SONDER_SAS  #: Sondervertragskunde abweichender Preis
    SONDER_TAS  #: Tarifkunden abweichender Preis
    SONDER_TKS  #: Kochen Warmwassererzeugung abweichender Preis
    SONDER_TSS  #: Strom mit Schwachlast (NT) abweichender Preis
