# IRP2 Python Problems

**Name:** Arjun Pundir  
**Roll No.:** 2481230

This repository contains four Python programs that read input from standard input.

## Repository structure

```text
irp2/
├── README.md
├── .gitignore
├── problems/
│   ├── p1_reverse_words.py
│   ├── p2_binary_search.py
│   ├── p3_digit_sum.py
│   └── p4_pair_count.py
└── tests/
    ├── p1_input.txt
    ├── p1_expected.txt
    ├── p2_input.txt
    ├── p2_expected.txt
    ├── p3_input.txt
    ├── p3_expected.txt
    ├── p4_input.txt
    └── p4_expected.txt
```

## Requirements

- Python 3.8 or later
- No third-party packages required

## How to run

Open a terminal in the repository folder and run:

```bash
python3 problems/p1_reverse_words.py < tests/p1_input.txt
python3 problems/p2_binary_search.py < tests/p2_input.txt
python3 problems/p3_digit_sum.py < tests/p3_input.txt
python3 problems/p4_pair_count.py < tests/p4_input.txt
```

Compare each program's output with the matching `*_expected.txt` file.

## Problem descriptions

1. **Reverse word order:** Read a line and print its words in reverse order.
2. **Binary search:** Read `n`, a sorted list of `n` integers, and a target. Print the target's 0-based index, or `-1` if it is absent. The implementation uses iterative binary search without a built-in search function.
3. **Recursive digit sum:** Read an integer and calculate the sum of its digits using recursion.
4. **Pair count:** Read `n` and `k`, then `n` integers. Count index pairs `(i, j)` where `i < j` and `a[i] + a[j] == k`. Duplicate values at different indices count as distinct pairs.

## Tests

The `tests/` directory contains sample input and expected output files for all four programs.
