# n = int(input())


def main(n):
    res = []
    total = 0
    for i in range(1, n + 1):
        total += i
        res.append(i)
        if total > n:
            res.pop()
            candidate_number = n - sum(res)
            if candidate_number <= res[-1]:
                res.pop()
            res.append(n - sum(res))
            break
    return res


print("4", main(4))
print("5", main(5))
print("6", main(6))
print("7", main(7))
print("8", main(8))
# print(main(10**9))
