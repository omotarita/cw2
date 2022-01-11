import pytest
from user import User

@pytest.fixture(scope='function')
def Musk():
    Musk = User("X Æ A-Xii ", "  Musk ", "xae-xii_musk@yahoomail.com", "12345678", (2020,5,4))
    yield Musk

@pytest.fixture(scope='function')
def Sacha():
    Sacha = User("Sacha", "Baron Cohen", "sachabaroncohen@yahoomail.com", "my77password33", (1971,10,13))
    yield Sacha


def test_for_internal_whitespace(Sacha):
    """
    GIVEN first/last name contains whitespace that isn't leading or trailing
    WHEN full name is created
    THEN it should return a fullname without the whitespace removed
    """
    assert Sacha.create_full_name() == "Sacha Baron Cohen", "Internal whitespace is stripped"


def test_for_trailing_whitespace(Musk):
    """
    GIVEN first/last name containing trailing whitespace
    WHEN full name is created
    THEN it should return a fullname with the whitespace stripped
    """
    clean_Musk = User(Musk.first_name.strip(), Musk.last_name.strip(), Musk.email, "87654321", Musk.dob)
    assert Musk.create_full_name() == clean_Musk.create_full_name(), "Trailing whitespace isn't stripped"
