import inspect

import pytest
from pydantic import ValidationError

from bo4e.bo.marktlokation import Marktlokation
from bo4e.com.adresse import Adresse
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.sparte import Sparte


class TestValidationBypass:
    """
    test cases that shows how to instantiate objects even without required fields
    """

    def test_instantiation_with_missing_required_attributes(self) -> None:
        # Assuming you'd like to instantiate a Marktlokation but have no value for e.g. the netzebene.
        # Then you could try the usual constructor:
        def instantiate_with_constructor() -> Marktlokation:
            malo = Marktlokation(  # type:ignore[call-arg] # silence mypy complaints about the missing netzebene
                marktlokations_id="51238696781",
                sparte=Sparte.GAS,
                lokationsadresse=Adresse(
                    postleitzahl="04109", ort="Leipzig", hausnummer="15", strasse="Thomaskirchhof"
                ),
                energierichtung=Energierichtung.EINSP,
                bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
                # note that netzebene is required but not given!
                # netzebene=Netzebene.NSP,
            )
            return malo

        # now, instantiation will fail:
        with pytest.raises(ValidationError) as validation_error:
            instantiate_with_constructor()
        error_msg = str(validation_error.value).replace("\n", " ").replace("\r", " ").replace("  ", " ")
        assert "1 validation error for Marktlokation netzebene  Field required" in error_msg

        # You're in a dilemma:
        # - either you cannot instantiate the BO, although you'd like to use BO4E
        # - or you have to guess values/enter dummy data which you cannot distinguish from real data later on.
        # The workaround is to use construct:
        def instantiate_with_construct() -> Marktlokation:
            malo = Marktlokation.model_construct(  # type:ignore[call-arg] # silence mypy complaints about the netzebene
                marktlokations_id="51238696781",
                sparte=Sparte.GAS,
                lokationsadresse=Adresse(
                    postleitzahl="04109", ort="Leipzig", hausnummer="15", strasse="Thomaskirchhof"
                ),
                energierichtung=Energierichtung.EINSP,
                bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
                # note that netzebene is required but not given!
                # netzebene=Netzebene.NSP,
            )
            return malo

        marktlokation = instantiate_with_construct()  # does _not_ raise an error
        assert isinstance(marktlokation, Marktlokation)  # Now the object is still a Marktlokation
        # but it has no member netzebene
        assert not any(m for m in inspect.getmembers(marktlokation) if m[0] == "netzebene")
        # and trying to access the missing netzebene raises an AttributeError:
        with pytest.raises(AttributeError):
            _ = marktlokation.netzebene
        # you can still serialize the invalid malo
        malo_json_str = marktlokation.model_dump_json()  # works
        assert malo_json_str is not None
        # but deserializing raises an error:
        with pytest.raises(ValidationError):
            Marktlokation.model_validate_json(malo_json_str)
