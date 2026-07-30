from collections import Counter


def find_duplicates(data):
    """
    Return the number of duplicate elements and a list of duplicates.

    Args:
        data (list): Input list.

    Returns:
        tuple: (duplicate_count, duplicate_list)

    Raises:
        TypeError: If input is not a non-empty list.
    """
    if not isinstance(data, list) or not data:
        raise TypeError("Input must be a non-empty list.")

    counter = Counter(data)
    duplicates = [item for item in data if counter[item] > 1]

    return len(duplicates), duplicates


if __name__ == "__main__":
    test_cases = [
        [3, 2, 4, 5, 6, 7, 8, 9],
        ["apple", "banana", "cherry", "apple", "orange", "grape"],
        [3, "apple", 4.5, "banana", "banana"],
    ]

    for test in test_cases:
        count, duplicates = find_duplicates(test)
        print(f"Input      : {test}")
        print(f"Count      : {count}")
        print(f"Duplicates : {duplicates}")
        print("-" * 40)

    # Example of handling invalid input
    try:
        find_duplicates([])
    except TypeError as e:
        print(f"Error: {e}")