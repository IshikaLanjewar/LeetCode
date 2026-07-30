def find_duplicates_in_list(data):
    """
    Find all duplicate elements in a given list of integers or strings.
    
    Args:
        data (list): A list to check for duplicates
        
    Returns:
        tuple: (count, found_elements) where count is the number of unique 
               occurrences and found_elements contains the actual duplicated values.
        
    Raises:
        ValueError: If input is not a list or empty
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    
    # Check for duplicates using set() to find unique elements first
    seen = set()
    count_map = {}  # Track how many times each element appears
    
    found_duplicates = []
    
    for item in data:
        if isinstance(item, (int, float)):
            key = str(item)  # Convert all items to strings for comparison
        else:
            key = str(item)
        
        count_map[key] += 1
        
        if count_map[key] > 1:
            found_duplicates.append(key)
    
    return len(found_duplicates), found_duplicates

# Example usage:
if __name__ == "__main__":
    test_list = [3, 2, 4, 5, 6, 7, 8, 9]
    count, duplicates = find_duplicates_in_list(test_list)
    
    print(f"List: {test_list}")
    print(f"Duplicates found: {duplicates}")
    print(f"Count of unique elements: {count}")

# Alternative version for strings only (if needed):
def find_duplicate_strings(data):
    """Find duplicate string values in a list."""
    if not isinstance(data, str) or len(data) == 0:
        raise TypeError("Input must be a non-empty string")
    
    seen = set()
    duplicates = []
    
    for item in data:
        key = str(item).lower()
        
        if key in seen:
            duplicates.append(key)
        else:
            seen.add(key)
            
    return len(duplicates), duplicates

# Example usage with strings:
if __name__ == "__main__":
    test_strings = ["apple", "banana", "cherry"] + ["apple", "orange", "grape"]
    count, duplicates = find_duplicate_strings(test_strings)
    
    print(f"Strings: {test_strings}")
    print(f"Duplicates found: {duplicates}")