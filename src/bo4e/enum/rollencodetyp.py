"""
Gibt den Codetyp einer Rolle, beispielsweise einer Marktrolle, an.
"""

from enum import Enum

_rollenrodetyp = {
    "BDEW": "BDEW",  # Bundesverband der Energie- u. Wasserwirtschaft
    "DVG": "DVG",  # Deutscher Verein des Gas- und Wasserfaches
    "GLN": "GLN"  # Global Location Number
}
Rollencodetyp = Enum("Rollencodetyp", _rollenrodetyp)
