"""Checks the original calculations and observes their runtime and memory."""

import time
import unittest
from unittest.mock import patch

import memory_profiler

from profiler import fast_function, main, memory_intensive_function, slow_function


EXPECTED_LARGE_SUM = 9_999_999 * 10_000_000 * 19_999_999 // 6


class TestProfiler(unittest.TestCase):
    def time_function(self, function):
        start = time.perf_counter()
        result = function()
        return result, time.perf_counter() - start

    def test_slow_function(self):
        result, duration = self.time_function(slow_function)
        print(f"slow_function: {duration:.3f} s")
        self.assertEqual(result, sum(i ** 2 for i in range(10_000)))
        self.assertGreaterEqual(duration, 2)

    def test_fast_function(self):
        result, duration = self.time_function(fast_function)
        print(f"fast_function: {duration:.6f} s")
        self.assertEqual(result, 328_350)
        self.assertLess(duration, 1)

    def test_memory_intensive_function(self):
        before = memory_profiler.memory_usage(-1, interval=0.01, timeout=0.01)[0]
        result, duration = self.time_function(memory_intensive_function)
        after = memory_profiler.memory_usage(-1, interval=0.01, timeout=0.01)[0]
        print(f"memory_intensive_function: {duration:.3f} s; RSS: {before:.2f} -> {after:.2f} MiB")
        self.assertEqual(result, EXPECTED_LARGE_SUM)
        self.assertLess(duration, 5)

    def test_main_calls_all_functions(self):
        with patch("profiler.slow_function") as slow, patch("profiler.fast_function") as fast, patch(
            "profiler.memory_intensive_function"
        ) as memory:
            main()
        slow.assert_called_once_with()
        fast.assert_called_once_with()
        memory.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
