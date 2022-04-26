# pip install git+https://github.com/DamnedFacts/rcviz

from rcviz import CallGraph, viz


n = int(input())
cg = CallGraph(
    filename=f"Алгоритмы - теория и практика. Методы/3.5. Практика на Python - Числа Фибоначчи/fib({n})_recursive.png"
)


@viz(cg)
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


print(fib1(n))
cg.render()
