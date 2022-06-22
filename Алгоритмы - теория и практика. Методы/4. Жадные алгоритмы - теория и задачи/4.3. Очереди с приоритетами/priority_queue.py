import heapq


def main(operations):
    heap = []
    result = []

    for operation in operations:
        data = operation.split()
        if data[0] == "Insert":
            operation, arg = data
            heapq.heappush(heap, -int(arg))
        else:
            result.append(-heapq.heappop(heap))
    return result


operations_number = int(input())
operations = [input() for _ in range(operations_number)]

for item in main(operations):
    print(item)


def test_heap():
    operations = [
        "Insert 200",
        "Insert 10",
        "ExtractMax",
        "Insert 5",
        "Insert 500",
        "ExtractMax",
    ]
    assert main(operations) == [200, 500]

    operations = [
        "Insert 2",
        "Insert 3",
        "Insert 18",
        "Insert 15",
        "Insert 18",
        "Insert 12",
        "Insert 12",
        "Insert 2",
        "ExtractMax",
        "ExtractMax",
        "ExtractMax",
    ]
    assert main(operations) == [18, 18, 15]


test_heap()
