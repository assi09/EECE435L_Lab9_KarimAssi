"""Memory profile of the optimized constant-space calculation."""

from memory_profiler import profile
from profiler import optimized_fast_function, slow_function


@profile
def memory_intensive_function():
    n = 10_000_000
    return (n - 1) * n * (2 * n - 1) // 6


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
