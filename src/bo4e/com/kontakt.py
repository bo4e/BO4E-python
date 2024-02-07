"""
Contains Kontakt class
"""

from typing import Optional

from ..com.adresse import Adresse
from ..com.rufnummer import Rufnummer
from ..enum.kontaktart import Kontaktart
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Kontakt(COM):
    """
    Die Komponente wird dazu verwendet, die Kontaktwege innerhalb des BOs Person darzustellen

    .. raw:: html

        <object data="../_static/images/bo4e/com/Kontakt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kontakt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Kontakt.json>`_

    """

    #: Gibt die Kontaktart des Kontaktes an.
    kontaktart: Optional[Kontaktart] = None
    #: E-Mail-Adresse des  bzw der Person an. Z.B. "info@hochfrequenz.de"
    e_mail_adresse: Optional[str] = None
    #: Liste der Telefonnummern, unter denen der Person erreichbar ist
    rufnummern: Optional[list[Rufnummer]] = None
    #: Adresse des Kontakts
    adresse: Optional[Adresse] = None
