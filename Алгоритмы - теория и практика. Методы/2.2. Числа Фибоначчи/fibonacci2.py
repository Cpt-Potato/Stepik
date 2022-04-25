def fib_digit(n):
    digit_current, digit_next = 0, 1
    for _ in range(n):
        digit_current, digit_next = digit_next, (digit_current + digit_next) % 10
    return digit_current


def main():
    # n = int(input())
    print(fib_digit(10**7))


if __name__ == "__main__":
    main()
