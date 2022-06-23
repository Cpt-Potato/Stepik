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


assert sum(main(4)) == 4
assert sum(main(5)) == 5
assert sum(main(6)) == 6
assert sum(main(7)) == 7
assert sum(main(8)) == 8
# assert sum(main(10**9))
