import inspect
import re
from pathlib import Path
from typing import List, Optional, TypeVar

import pytest  # type:ignore[import]

from bo4e.enum import anrede
from bo4e.enum.anrede import Anrede
from bo4e.enum.strenum import StrEnum


class TestEnums:
    """
    A test class that checks the enum construction.
    """

    starts_with_whitespace_pattern = re.compile(r"^[\s\n]+")
    ends_with_whitespace_pattern = re.compile(r"[\s\n]+$")

    TEnum = TypeVar("TEnum", bound=StrEnum)

    @staticmethod
    def _get_all_enum_classes() -> List[TEnum]:
        """
        returns a list of all bo4e.enum classes
        """
        arbitrary_enum_module_path = Path(anrede.__file__)
        result = []
        for python_file in arbitrary_enum_module_path.parent.glob("*.py"):
            # don't ask me why. but it works.
            enum_module = __import__("bo4e.enum." + python_file.name.split(".")[0])
            for _, member in inspect.getmembers(enum_module.enum):
                if inspect.ismodule(member):
                    candidate = inspect.getmembers(member)[0][1]
                    if inspect.isclass(candidate):
                        result.append(candidate)
        return result

    @staticmethod
    def _get_class_doc(enum_class: TEnum) -> Optional[str]:
        """
        asserts that enum class is a class and returns the class' docstring
        """
        assert inspect.isclass(enum_class)
        return inspect.getdoc(enum_class)

    def test_enum_classes_docstrings(self):
        """
        Tests that the docstrings of the enum classes do not start with whitespace or blank lines.
        """
        all_enums = TestEnums._get_all_enum_classes()
        assert len(all_enums) > 100  # just to be sure we're not using the wrong directory or path
        for enum_class in all_enums:
            docstring = TestEnums._get_class_doc(enum_class)
            assert docstring is not None
            assert not TestEnums.starts_with_whitespace_pattern.match(docstring)
            assert not TestEnums.ends_with_whitespace_pattern.match(docstring)

    @pytest.mark.parametrize(
        "enum_member, expected_docstring",
        [
            pytest.param(Anrede.HERR, "Herr"),
            pytest.param(Anrede.INDIVIDUELL, 'Individuell (z.B. "Profx")'),
        ],
    )
    def test_enum_member_docstrings_explicitly(self, enum_member: TEnum, expected_docstring: Optional[str]):
        """
        Test the docstrings of the enum members explicitly.
        if the general approach (using DocumentedStrEnum) works for single members, it will also work for all enums,
        which are constructed similarly.
        """
        assert inspect.getdoc(enum_member) == expected_docstring

    def test_enum_members_are_all_documented(self):
        """
        The class docstrings are enforced using pylint but the docstrings of enum members are not covered by pylint.
        """
        all_enums = self._get_all_enum_classes()
        for enum_class in all_enums:
            class_docstring = TestEnums._get_class_doc(enum_class)
            for enum_member in enum_class:
                member_docstring = inspect.getdoc(enum_member)
                assert (
                    member_docstring != class_docstring
                ), f"Docstring of Enum member {enum_member} must not be the same as the class docstring"
                assert member_docstring is not None
                assert member_docstring != ""
                assert not TestEnums.starts_with_whitespace_pattern.match(member_docstring)
                assert not TestEnums.ends_with_whitespace_pattern.match(member_docstring)
            break  # proof this works just for the wip anrede
