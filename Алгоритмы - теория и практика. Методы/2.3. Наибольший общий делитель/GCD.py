def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        while a != 0 and b != 0:
            a, b = max(a, b), min(a, b)
            a, b = (a % b), b
    return a or b


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


def main():
    # a, b = map(int, input().split())
    print(gcd(18, 35))
    print(gcd(14159572, 63967072))


if __name__ == "__main__":
    main()
