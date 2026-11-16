"""Optimized Lab 9 functions; compare with baseline/profiler.py."""

import time


def slow_function():
    time.sleep(2)
    total = 0
    for i in range(10_000):
        total += i ** 2
    return total


def optimized_fast_function():
    n = 100
    return (n - 1) * n * (2 * n - 1) // 6


def memory_intensive_function():
    # The identity 0**2 + ... + (n-1)**2 = (n-1)*n*(2*n-1)//6
    n = 10_000_000
    return (n - 1) * n * (2 * n - 1) // 6


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
