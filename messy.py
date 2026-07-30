def search_element(arr, target):
    if type(arr) != list:
        raise TypeError("arr must be a list")
    if len(arr) == 0:
        return False
    temp = []
    for i in range(0, len(arr)):
        temp.append(arr[i])
    weird = []
    for x in temp:
        if x == target:
            weird.append(1)
        else:
            weird.append(0)
    counter = 0
    for y in weird:
        if y == 1:
            counter += 1
        else:
            counter = counter
    if counter > 0:
        return True
    else:
        return False

# Example
numbers = [10, 20, 30, 40, 50]
print(search_element(numbers, 30))
print(search_element(numbers, 99))
