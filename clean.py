def validate_list(arr):
    """Check that the input is a list."""
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")


def contains_value(arr, target):
    """Return True if target exists in arr, otherwise False."""
    if not arr:
        return False
    return any(item == target for item in arr)


def search_element(arr, target):
    """Search for a target value in a list and return a boolean result."""
    validate_list(arr)
    return contains_value(arr, target)


numbers = [10, 20, 30, 40, 50]
print(search_element(numbers, 30))
print(search_element(numbers, 99))
