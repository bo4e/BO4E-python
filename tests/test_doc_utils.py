from bo4e.bo.angebot import Angebot
from bo4e.utils import is_constrained_str


class TestDocUtils:
    def test_is_constrained_str(self) -> None:
        actual = is_constrained_str(Angebot.model_fields["angebotsnummer"])
        assert actual is True
