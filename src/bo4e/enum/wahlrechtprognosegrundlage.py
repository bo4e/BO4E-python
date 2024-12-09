"""
Contains Enums for Wahlrechtsprognosgrundlage.
"""

from bo4e.enum.strenum import StrEnum


class WahlrechtPrognosegrundlage(StrEnum):
    """
    Wahlrecht der Prognosegrundlage der Marktlokation.
    """

    DURCH_LF = "DURCH_LF"  #: Wahlrecht durch LF gegeben, remark: SG10 CAV
    DURCH_LF_NICHT_GEGEBEN = "DURCH_LF_NICHT_GEGEBEN"  #: Wahlrecht durch LF nicht gegeben, remark: CAV + ZE2
    NICHT_WEGEN_GROSSEN_VERBRAUCHS = "NICHT_WEGEN_GROSSEN_VERBRAUCHS"  # : kein WR, Verbrauch>10k, CAV+ Z55
    NICHT_WEGEN_EIGENVERBRAUCH = "NICHT_WEGEN_EIGENVERBRAUCH"  #: kein WR, Eigenverbrauch, CAV + ZC1
    NICHT_WEGEN_TAGES_VERBRAUCH = "NICHT_WEGEN_TAGES_VERBRAUCH"  # : kein WR, tagesparam.abh. Verbrauch, CAV + ZD2
    NICHT_WEGEN_ENWG = "NICHT_WEGEN_ENWG"  #: WR nicht wegen $14a EnWG, CAV + ZE3
