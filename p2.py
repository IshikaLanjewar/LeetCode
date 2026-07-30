def find_duplicates(lst):
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1

    return [num for num, c in count.items() if c > 1]

numbers = [1, 2, 2, 3, 4, 4, 5]
print(find_duplicates(numbers))
