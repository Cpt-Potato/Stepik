def fib(n):
    fib_prev, fib_current = 0, 1
    for _ in range(n):
        fib_prev, fib_current = fib_current, (fib_prev + fib_current)
    return fib_prev


def main():
    print(fib(0))
    print(fib(40))
    print(fib(100))


if __name__ == "__main__":
    main()
