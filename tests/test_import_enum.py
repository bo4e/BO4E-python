class TestImport:
    def test_importing_an_enum(self) -> None:
        """
        checks that importing an enum works
        """
        from bo4e import Vertragsstatus  # pylint: disable=import-outside-toplevel,unused-import

        assert True
