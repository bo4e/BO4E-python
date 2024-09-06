# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class FernsteuerbarkeitStatus(StrEnum):
    """
    Enum zur Abbildung des Status der Fernsteuerbarkeit

    Marktlokation ist technisch fernsteuerbar. Der NB bestätigt mit der Anmeldung einer erzeugenden Marktlokation zur
    Direktvermarktung, dass die Marktlokation mit einer Fernsteuerung ausgestattet, aber dem NB keine Information
    darüber vorliegt, dass der LF die Marktlokation fernsteuern kann. Die Voraussetzung zur Zahlung der
    Managementprämie für fernsteuerbare Marktlokation ist nicht gegeben.
    """

    NICHT_FERNSTEUERBAR = "NICHT_FERNSTEUERBAR"  #: nicht fernsteuerbar
    TECHNISCH_FERNSTEUERBAR = "TECHNISCH_FERNSTEUERBAR"  #: technisch fernsteuerbar
    LIEFERANT_FERNSTEUERBAR = "LIEFERANT_FERNSTEUERBAR"  #: lieferantenseitig fernsteuerbar
    #
