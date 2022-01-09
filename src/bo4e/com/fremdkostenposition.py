"""
Contains Fremdkostenposition and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

import attr
from marshmallow import fields

from bo4e.com.kostenposition import Kostenposition, KostenpositionSchema


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class Fremdkostenposition(Kostenposition):
    """
    Eine Kostenposition im Bereich der Fremdkosten
    """

    # optional attributes (additional to those from Kostenposition)
    #: Der Name des Marktpartners, der die Preise festlegt, bzw. die Kosten in Rechnung stellt
    marktpartnername: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )

    #: Die Codenummer (z.B. BDEW-Codenummer) des Marktpartners, der die Preise festlegt / die Kosten in Rechnung stellt
    marktpartnercode: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )

    #: EIC-Code des Regel- oder Marktgebietes eingetragen. Z.B. '10YDE-EON------1' für die Regelzone TenneT
    gebietcode_eic: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    # todo: see issue https://github.com/Hochfrequenz/BO4E-python/issues/147 for EIC validation

    #: Link zum veröffentlichten Preisblatt
    link_preisblatt: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )


class FremdkostenpositionSchema(KostenpositionSchema):
    """
    Schema for de-/serialization of Fremdkostenposition
    """

    # optional attributes (additional to those from Kostenposition)
    class_name = Fremdkostenposition  # type:ignore[assignment]
    marktpartnername = fields.Str(allow_none=True)
    marktpartnercode = fields.Str(allow_none=True)
    gebietcode_eic = fields.Str(allow_none=True)
    link_preisblatt = fields.Str(allow_none=True)
