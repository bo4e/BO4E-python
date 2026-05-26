"""
Contains Zaehlzeittagtyp class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.wiederholungstyp import Wiederholungstyp
    from .umschaltzeit import Umschaltzeit


@postprocess_docstring
class Zaehlzeittagtyp(COM):
    """
    Beschreibt das Schaltschema eines Tagtyps innerhalb einer `Zaehlzeitsaison`: welcher Tagtyp
    gemeint ist und zu welchen Uhrzeiten welches Register an diesem Tagtyp aktiv ist.

    Der Tagtyp wird über einen `Wiederholungstyp` ausgedrückt (z.B. `WERKTAGS`, `MONTAGS`,
    `FEIERTAGS`).

    Die `umschaltzeiten` füllen einen ganzen Tag vollständig und überlappungsfrei aus.
    Die jeweilige Umschaltzeit definiert (wenn der Größe nach sortiert) die untere Grenze (inklusiv);
    der Beginn des Tages (00:00 Uhr) und das Ende des Tages (24:00 Uhr) bilden die äußeren Grenzen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlzeittagtyp.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlzeittagtyp JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zaehlzeittagtyp.json>`_

    """

    typ: Annotated[Literal[ComTyp.ZAEHLZEITTAGTYP], Field(alias="_typ")] = ComTyp.ZAEHLZEITTAGTYP

    tagtyp: Optional["Wiederholungstyp"] = None
    """An welchen Tagen das Schaltschema dieses Tagtyps gilt (z.B. `WERKTAGS`, `MONTAGS`, `FEIERTAGS`)."""
    umschaltzeiten: Optional[list["Umschaltzeit"]] = None
    """Die Umschaltzeiten dieses Tagtyps. Sortiert ergibt sich daraus das Schaltschema für einen Tag."""
