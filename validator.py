# validator.py

def is_valid_email(email):
    """Check whether an email has a basic valid format."""
    if not isinstance(email, str):
        return False

    return "@" in email and "." in email.split("@")[-1]


def is_valid_age(age):
    """Check whether age is between 0 and 120."""
    return isinstance(age, int) and 0 <= age <= 120


def is_valid_password(password):
    """Check whether a password has at least 8 characters."""
    if not isinstance(password, str):
        return False

    return len(password) >= 8

print(is_valid_email("test@example.com"))  # True
print(is_valid_email("invalid-email"))     # False

print(is_valid_age(25))                    # True
print(is_valid_age(150))                   # False

print(is_valid_password("password123"))    # True
print(is_valid_password("abc"))            # False