def binary_search(array, value):
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == value:
            return middle + 1
        elif array[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def main():
    n, *array = list(map(int, input().split()))
    k, *values_to_find = list(map(int, input().split()))

    for value in values_to_find:
        print(binary_search(array, value), end=" ")


main()


def test():
    array = [1, 5, 8, 12, 13]
    values_to_find = [8, 1, 23, 1, 11]
    result = []
    for value in values_to_find:
        result.append(binary_search(array, value))
    assert result == [3, 1, -1, 1, -1]


# test()
