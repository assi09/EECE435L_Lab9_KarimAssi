"""Line-by-line timing for the optimized functions."""

from line_profiler import LineProfiler
from profiler import (
    main,
    memory_intensive_function,
    optimized_fast_function,
    slow_function,
)


def profile_main():
    profiler = LineProfiler()
    for function in (slow_function, optimized_fast_function, memory_intensive_function):
        profiler.add_function(function)
    profiler.runcall(main)
    profiler.print_stats()


if __name__ == "__main__":
    profile_main()
