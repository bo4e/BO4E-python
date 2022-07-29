from typing import List, Optional

import pytest
from pydantic import ValidationError

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.externereferenz import ExterneReferenz
from bo4e.enum.botyp import BoTyp


class TestGeschaeftsobjekt:
    @pytest.mark.parametrize(
        "bo_typ, versionstruktur, externe_referenzen",
        [
            (
                BoTyp.ENERGIEMENGE,
                "2",
                [
                    ExterneReferenz(ex_ref_name="HOCHFREQUENZ_HFSAP_100", ex_ref_wert="12345"),
                    ExterneReferenz(ex_ref_name="Schufa-ID", ex_ref_wert="aksdlakoeuhn"),
                ],
            ),
            (
                BoTyp.ENERGIEMENGE,
                "2",
                [ExterneReferenz(ex_ref_name="HOCHFREQUENZ_HFSAP_100", ex_ref_wert="12345")],
            ),
            (BoTyp.ENERGIEMENGE, "2", []),
        ],
    )
    def test_serialisation(
        self, bo_typ: BoTyp, versionstruktur: str, externe_referenzen: Optional[List[ExterneReferenz]]
    ) -> None:
        go = Geschaeftsobjekt(
            bo_typ=bo_typ,
            versionstruktur=versionstruktur,
            externe_referenzen=externe_referenzen,
        )
        assert isinstance(go, Geschaeftsobjekt)

        go_json = go.json(by_alias=True, ensure_ascii=False)

        assert str(versionstruktur) in go_json

        go_deserialized = Geschaeftsobjekt.parse_raw(go_json)

        assert go_deserialized.bo_typ is bo_typ
        assert go_deserialized.versionstruktur == versionstruktur
        assert go_deserialized.externe_referenzen == externe_referenzen

    def test_initialization_with_minimal_attributs(self) -> None:
        go = Geschaeftsobjekt(bo_typ=BoTyp.ANSPRECHPARTNER)

        assert go.externe_referenzen == []
        assert go.versionstruktur == "2"

    def test_no_list_in_externen_referenzen(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Geschaeftsobjekt(
                bo_typ=BoTyp.ENERGIEMENGE,
                externe_referenzen=ExterneReferenz(ex_ref_name="Schufa-ID", ex_ref_wert="aksdlakoeuhn"),  # type: ignore[arg-type]
            )
        assert "1 validation error" in str(excinfo.value)
        assert "value is not a valid list" in str(excinfo.value)
