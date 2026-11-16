"""Memory profile of the original 10-million-iteration calculation."""

from memory_profiler import profile
from profiler import fast_function, slow_function


@profile
def memory_intensive_function():
    total = 0
    for i in range(10_000_000):
        total += i ** 2
    return total


def main():
    slow_function()
    fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
