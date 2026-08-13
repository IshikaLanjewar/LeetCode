import pytest

from validator import (
    is_valid_email,
    is_valid_age,
    is_valid_password,
)


def test_is_valid_email_normal_and_boundary():
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("a@b.c") is True  # minimal domain with dot


@pytest.mark.parametrize(
    "email,expected",
    [
        ("invalid-email", False),
        ("noatsymbol.com", False),
        ("@domain.com", True),  # current implementation accepts empty local part
        ("a@b@c.com", True),  # multiple @ but domain part contains a dot
        (None, False),
        (12345, False),
    ],
)
def test_is_valid_email_various(email, expected):
    assert is_valid_email(email) is expected


@pytest.mark.parametrize(
    "age,expected",
    [
        (25, True),
        (0, True),
        (120, True),
        (-1, False),
        (121, False),
        ("30", False),
        (25.0, False),
    ],
)
def test_is_valid_age_various(age, expected):
    assert is_valid_age(age) is expected


@pytest.mark.parametrize(
    "pw,expected",
    [
        ("password123", True),
        ("abcd1234", True),  # exactly 8 chars
        ("", False),
        ("short", False),
        (None, False),
        (12345678, False),
    ],
)
def test_is_valid_password_various(pw, expected):
    assert is_valid_password(pw) is expected


def test_intentional_failures_for_validator_assumptions():
    # These tests assert stricter requirements than the current implementation.
    # They are expected to fail with the current `validator.py` behavior.
    # 1) Email should not allow empty local part
    assert is_valid_email("@domain.com") is False

    # 2) Email with multiple '@' should be invalid
    assert is_valid_email("a@b@c.com") is False

    # 3) Password that is only spaces should be considered invalid
    assert is_valid_password("        ") is False

    # 4) Boolean values should not be accepted as valid ages
    assert is_valid_age(True) is False


def test_more_edge_cases():
    # Email edge-cases
    assert is_valid_email("user.name+tag+sorting@example.co.uk") is True
    assert is_valid_email("user@localhost") is False  # no dot in domain
    assert is_valid_email("user@.com") is False

    # Age edge-cases
    assert is_valid_age(1) is True
    assert is_valid_age(119) is True
    assert is_valid_age(None) is False

    # Password edge-cases
    assert is_valid_password("pässwörd123") is True
    assert is_valid_password("1234567") is False  # 7 chars
