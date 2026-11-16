# Lab 9 Python Profiling

Karim Assi — EECE435L. The original implementation is in `baseline/`; the optimized implementation is in this folder. Both calculate the same results. The Word report compares the measured runs and includes captured command output. Full command output is in `results/`. Each version has an HTML coverage report.

## Set up

```sh
cd "/Users/karimassi/Desktop/All/AUB/EECE435L/Lab 9/lab9_Karim_Assi"
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Reproduce the baseline

```sh
cd baseline
../.venv/bin/python -m cProfile -s time profiler.py
../.venv/bin/python profiler_lineprofiler.py
../.venv/bin/python -m memory_profiler profiler_memoryprofiler.py
../.venv/bin/python -m coverage run --source=profiler -m unittest discover -v
../.venv/bin/python -m coverage report -m
../.venv/bin/python -m coverage html -d htmlcov
```

The baseline memory profiler traces the ten-million-iteration loop line by line and can take several minutes. The normal cProfile run is much faster.

## Reproduce the optimized version

```sh
cd ..
.venv/bin/python -m cProfile -s time profiler.py
.venv/bin/python profiler_lineprofiler.py
.venv/bin/python -m memory_profiler profiler_memoryprofiler.py
.venv/bin/python -m coverage run --source=profiler -m unittest discover -v
.venv/bin/python -m coverage report -m
.venv/bin/python -m coverage html -d htmlcov
```

Open `baseline/htmlcov/index.html` and `htmlcov/index.html` to inspect unexecuted lines. The only missing line in each version is the call under the direct-execution guard; the tests import `profiler.py` and exercise the functions and `main()` directly.

## File map

- `profiler.py`, `profiler_lineprofiler.py`, `profiler_memoryprofiler.py`, and `test_profiler.py`: optimized version.
- `baseline/`: corresponding original version of all four code files.
- `htmlcov/index.html` and `baseline/htmlcov/index.html`: HTML coverage entry points.
- `results/`: full tool output from an earlier run. Its timings can differ slightly from the screenshot run.
- `evidence/`: eight original Terminal screenshots of the baseline and optimized profiling and test runs used in the report.
- `lab9_Karim_Assi.docx`: comparative report.

The baseline and optimized `memory_intensive_function()` use constant space. The improvement is CPU time; separate memory-profiler runs did not show a meaningful RSS reduction. The code tests the numerical outputs and avoids relying on an increase in RSS, which is not guaranteed by Python's allocator.
