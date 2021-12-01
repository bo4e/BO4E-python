# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Messpreistyp(StrEnum):
    """
    Festlegung, welcher Typ von Messung mit einem Preis belegt wird
    """

    MESSPREIS_G2_5  #: Gas
    MESSPREIS_G4  #: Gas
    MESSPREIS_G6  #: Gas
    MESSPREIS_G10  #: Gas
    MESSPREIS_G16  #: Gas
    MESSPREIS_G25  #: Gas
    MESSPREIS_G40  #: Gas
    ELEKTRONISCHER_AUFSATZ  #: Gas
    SMART_METER_MESSPREIS_G2_5  #: Gas
    SMART_METER_MESSPREIS_G4  #: Gas
    SMART_METER_MESSPREIS_G6  #: Gas
    SMART_METER_MESSPREIS_G10  #: Gas
    SMART_METER_MESSPREIS_G16  #: Gas
    SMART_METER_MESSPREIS_G25  #: Gas
    SMART_METER_MESSPREIS_G40  #: Gas
    VERRECHNUNGSPREIS_ET_WECHSEL  #: Strom
    VERRECHNUNGSPREIS_ET_DREH  #: Strom
    VERRECHNUNGSPREIS_ZT_WECHSEL  #: Strom
    VERRECHNUNGSPREIS_ZT_DREH  #: Strom
    VERRECHNUNGSPREIS_L_ET  #: Strom
    VERRECHNUNGSPREIS_L_ZT  #: Strom
    VERRECHNUNGSPREIS_SM  #: Strom
    AUFSCHLAG_WANDLER  #: Strom
    AUFSCHLAG_TARIFSCHALTUNG  #: Strom
