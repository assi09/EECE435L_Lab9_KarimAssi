#!/bin/zsh
# Run this in Terminal to capture the eight real Terminal screenshots requested by the handout.
set -e

lab9_root="${0:A:h}"
mkdir -p "$lab9_root/evidence"

capture_screen() {
  local label="$1"
  local output="$lab9_root/evidence/${label}.png"
  printf '\nCapturing the full screen to %s ...\n' "$output"
  if screencapture -x "$output" && [[ -s "$output" ]]; then
    printf 'Saved %s\n' "$output"
    return 0
  fi
  printf '\nAutomatic capture failed. Use Command-Shift-4 to save a screenshot as:\n%s\n' "$output"
  printf 'Press Return after saving it.\n'
  read -r
  if [[ ! -s "$output" ]]; then
    printf 'Screenshot is still missing: %s\n' "$output" >&2
    return 1
  fi
}

run_and_capture() {
  local label="$1"
  local folder="$2"
  shift 2
  cd "$folder"
  clear
  printf 'Project: %s\n\n' "$PWD"
  printf '$ %s\n\n' "$*"
  "$@"
  capture_screen "$label"
}

run_coverage_and_capture() {
  local label="$1"
  local folder="$2"
  local python_bin="$3"
  cd "$folder"
  clear
  printf 'Project: %s\n\n' "$PWD"
  printf '$ %s -m coverage run --source=profiler -m unittest discover -v\n\n' "$python_bin"
  "$python_bin" -m coverage run --source=profiler -m unittest discover -v
  printf '\n$ %s -m coverage report -m\n\n' "$python_bin"
  "$python_bin" -m coverage report -m
  capture_screen "$label"
}

run_and_capture baseline_cprofile_terminal "$lab9_root/baseline" ../.venv/bin/python -m cProfile -s time profiler.py
run_and_capture optimized_cprofile_terminal "$lab9_root" .venv/bin/python -m cProfile -s time profiler.py
run_and_capture baseline_line_terminal "$lab9_root/baseline" ../.venv/bin/python profiler_lineprofiler.py
run_and_capture optimized_line_terminal "$lab9_root" .venv/bin/python profiler_lineprofiler.py
run_and_capture baseline_memory_terminal "$lab9_root/baseline" ../.venv/bin/python -m memory_profiler profiler_memoryprofiler.py
run_and_capture optimized_memory_terminal "$lab9_root" .venv/bin/python -m memory_profiler profiler_memoryprofiler.py
run_coverage_and_capture baseline_tests_terminal "$lab9_root/baseline" ../.venv/bin/python
run_coverage_and_capture optimized_tests_terminal "$lab9_root" .venv/bin/python

printf '\nAll eight screenshots are in %s/evidence.\n' "$lab9_root"
