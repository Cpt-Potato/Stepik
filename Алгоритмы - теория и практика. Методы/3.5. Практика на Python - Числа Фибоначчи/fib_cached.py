# pip install git+https://github.com/DamnedFacts/rcviz

from rcviz import CallGraph, viz
from functools import lru_cache


n = int(input())
cg = CallGraph(
    filename=f"Алгоритмы - теория и практика. Методы/3.5. Практика на Python - Числа Фибоначчи/fib({n})_cached.png"
)


@viz(cg)
@lru_cache(maxsize=128)
def fib(n):
    assert n >= 0
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


print(fib(n))
cg.render()
