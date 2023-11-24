from typing import List, Optional

import pytest
from pydantic import ValidationError

from bo4e import ExterneReferenz, Geschaeftsobjekt, Typ


class TestGeschaeftsobjekt:
    @pytest.mark.parametrize(
        "typ, version, externe_referenzen",
        [
            (
                Typ.ENERGIEMENGE,
                "2",
                [
                    ExterneReferenz(ex_ref_name="HOCHFREQUENZ_HFSAP_100", ex_ref_wert="12345"),
                    ExterneReferenz(ex_ref_name="Schufa-ID", ex_ref_wert="aksdlakoeuhn"),
                ],
            ),
            (
                Typ.ENERGIEMENGE,
                "2",
                [ExterneReferenz(ex_ref_name="HOCHFREQUENZ_HFSAP_100", ex_ref_wert="12345")],
            ),
            (Typ.ENERGIEMENGE, "2", []),
        ],
    )
    def test_serialisation(self, typ: Typ, version: str, externe_referenzen: Optional[List[ExterneReferenz]]) -> None:
        go = Geschaeftsobjekt(
            typ=typ,
            version=version,
            externe_referenzen=externe_referenzen,
        )
        assert isinstance(go, Geschaeftsobjekt)

        go_json = go.model_dump_json(by_alias=True)

        assert str(version) in go_json

        go_deserialized = Geschaeftsobjekt.model_validate_json(go_json)

        assert go_deserialized.typ is typ
        assert go_deserialized.version == version
        assert go_deserialized.externe_referenzen == externe_referenzen

    def test_initialization_with_minimal_attributs(self) -> None:
        go = Geschaeftsobjekt(typ=Typ.ANSPRECHPARTNER)

        assert go.externe_referenzen is None
        assert go.version is not None

    def test_no_list_in_externen_referenzen(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Geschaeftsobjekt(
                typ=Typ.ENERGIEMENGE,
                externe_referenzen=ExterneReferenz(ex_ref_name="Schufa-ID", ex_ref_wert="aksdlakoeuhn"),  # type: ignore[arg-type]
            )
        # The error message is completely broken, but who cares
        assert "4 validation error" in str(excinfo.value)
        assert "type=model_type" in str(excinfo.value)
