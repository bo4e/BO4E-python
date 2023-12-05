# pylint: disable=missing-module-docstring
from decimal import Decimal
from typing import Annotated, Optional

from humps.main import camelize

# pylint: disable=no-name-in-module
from pydantic import BaseModel, ConfigDict, Field

from bo4e.version import __version__
from bo4e.zusatzattribut import ZusatzAttribut

from ..enum.typ import Typ
from ..utils import postprocess_docstring

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Geschaeftsobjekt(BaseModel):
    """
    Das BO Geschäftsobjekt ist der Master für alle Geschäftsobjekte.
    Alle Attribute, die hier in diesem BO enthalten sind, werden an alle BOs vererbt.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geschaeftsobjekt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geschaeftsobjekt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Geschaeftsobjekt.json>`_

    """

    # required attributes
    version: Annotated[
        Optional[str], Field(alias="_version")
    ] = __version__  #: Version der BO-Struktur aka "fachliche Versionierung"
    # src/_bo4e_python_version.py
    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.GESCHAEFTSOBJEKT  #: Der Typ des Geschäftsobjektes
    # bo_typ is used as discriminator f.e. for databases or deserialization

    zusatz_attribute: Optional[list[ZusatzAttribut]] = None
    # zusatz_attribute is a list of ZusatzAttribut objects which are used to store additional information

    # Python internal: The field is not named '_id' because leading underscores are not allowed in pydantic field names.
    # NameError: Fields must not use names with leading underscores; e.g., use 'id' instead of '_id'.
    id: Annotated[Optional[str], Field(alias="_id")] = None
    """
    Eine generische ID, die für eigene Zwecke genutzt werden kann.
    Z.B. könnten hier UUIDs aus einer Datenbank stehen oder URLs zu einem Backend-System.
    """

    #: Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)
    # pylint: disable=duplicate-code
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        extra="allow",
        # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create
        # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.
        # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375
        json_encoders={Decimal: str},
    )
    """
    basic configuration for pydantic's behaviour
    """
