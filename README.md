Solutions to common math problems through algorithmic approach.

## Project Euler Solutions

Located in `euler_problems/`:

| Problem | Description | Key Concepts |
|---------|-------------|--------------|
| [Stirling's Factorial](euler_problems/stirlings_factorial.py) | Factorial approximation using Stirling's formula | `n! ≈ sqrt(2πn) * (n/e)^n`, digit counting |
| [Problem 1](euler_problems/problem_001_multiples.py) | Multiples of 3 or 5 | Inclusion-exclusion principle, arithmetic series |
| [Problem 2](euler_problems/problem_002_fibonacci.py) | Even Fibonacci numbers | Optimized recurrence `E(n) = 4*E(n-1) + E(n-2)` |
| [Problem 6](euler_problems/problem_006_sum_square_difference.py) | Sum square difference | Closed-form formulas, sum of cubes identity |

## Other Solutions

- [army_game.py](army_game.py) - Minimum packages to supply grid cells (HackerRank)

## Running Solutions

```bash
python euler_problems/stirlings_factorial.py
python euler_problems/problem_001_multiples.py
python euler_problems/problem_002_fibonacci.py
python euler_problems/problem_006_sum_square_difference.py
```
