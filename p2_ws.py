# from collections import Counter
 
 
# def find_duplicates(items):
#     """Return elements that appear more than once, in first-seen order."""
#     counts = Counter(items)
#     seen = set()
#     result = []
#     for item in items:
#         if counts[item] > 1 and item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result
 
 
# if __name__ == "__main__":
#     print(find_duplicates([1, 2, 3, 2, 4, 1, 1]))
#     print(find_duplicates(["a", "b", "a", "c", "c"]))
#     print(find_duplicates([1, 2, 3]))
 
 
 
 
 
 
 
#  optimized version without using Counter
def find_duplicates(items):
    """Return elements that appear more than once, in first-seen order."""
    seen = set()
    dupes = set()
    result = []
    for item in items:
        if item in seen:
            if item not in dupes:
                dupes.add(item)
                result.append(item)
        else:
            seen.add(item)
    return result


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 1, 1]))
    print(find_duplicates(["a", "b", "a", "c", "c"]))
    print(find_duplicates([1, 2, 3]))
