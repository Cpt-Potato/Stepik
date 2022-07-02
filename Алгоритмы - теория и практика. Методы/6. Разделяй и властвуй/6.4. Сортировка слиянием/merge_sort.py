inversions_counter = 0


def merge(left, right):
    global inversions_counter
    array_merged = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            array_merged.append(left[left_pointer])
            left_pointer += 1
        else:
            array_merged.append(right[right_pointer])
            right_pointer += 1
            inversions_counter += len(left) - left_pointer
    return array_merged + left[left_pointer:] + right[right_pointer:]


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left, right = array[:middle], array[middle:]
        return merge(merge_sort(left), merge_sort(right))
    return array


def test_merge_sort():
    array = [2, 3, 9, 2, 9]
    assert merge_sort(array) == [2, 2, 3, 9, 9]
    assert inversions_counter == 2

    array = [7, 6, 5, 4, 3, 2, 1]
    assert merge_sort(array) == [1, 2, 3, 4, 5, 6, 7]
    assert inversions_counter - 2 == 21

    array = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
    assert merge_sort(array) == [3, 4, 6, 8, 13, 16, 19, 27, 27, 34, 39, 41, 41, 52, 78]


def main():
    n = int(input())
    array = [int(number) for number in input().split()]
    merge_sort(array)
    print(inversions_counter)


test_merge_sort()
# main()
