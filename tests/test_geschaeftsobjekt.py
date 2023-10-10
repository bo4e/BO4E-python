from typing import List, Optional

import pytest
from pydantic import ValidationError

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.enum.typ import Typ
from bo4e.zusatzattribut import ZusatzAttribut


class TestGeschaeftsobjekt:
    @pytest.mark.parametrize(
        "typ, versionstruktur, externe_referenzen",
        [
            (
                Typ.ENERGIEMENGE,
                "2",
                [
                    ZusatzAttribut(name="HOCHFREQUENZ_HFSAP_100", wert="12345"),
                    ZusatzAttribut(name="Schufa-ID", wert="aksdlakoeuhn"),
                ],
            ),
            (
                Typ.ENERGIEMENGE,
                "2",
                [ZusatzAttribut(name="HOCHFREQUENZ_HFSAP_100", wert="12345")],
            ),
            (Typ.ENERGIEMENGE, "2", []),
        ],
    )
    def test_serialisation(
        self, typ: Typ, versionstruktur: str, externe_referenzen: Optional[List[ZusatzAttribut]]
    ) -> None:
        go = Geschaeftsobjekt(
            typ=typ,
            versionstruktur=versionstruktur,
            externe_referenzen=externe_referenzen,
        )
        assert isinstance(go, Geschaeftsobjekt)

        go_json = go.model_dump_json(by_alias=True)

        assert str(versionstruktur) in go_json

        go_deserialized = Geschaeftsobjekt.model_validate_json(go_json)

        assert go_deserialized.typ is typ
        assert go_deserialized.versionstruktur == versionstruktur
        assert go_deserialized.zusatz_attribute == externe_referenzen

    def test_initialization_with_minimal_attributs(self) -> None:
        go = Geschaeftsobjekt(typ=Typ.ANSPRECHPARTNER)

        assert go.zusatz_attribute is None
        assert go.versionstruktur == "2"

    def test_no_list_in_externen_referenzen(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Geschaeftsobjekt(
                typ=Typ.ENERGIEMENGE,
                externe_referenzen=ZusatzAttribut(name="Schufa-ID", wert="aksdlakoeuhn"),  # type: ignore[arg-type]
            )
        assert "3 validation error" in str(excinfo.value)
        assert "type=model_type" in str(excinfo.value)
