"""
Project Euler Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Solution approaches:
1. Brute force - iterate through all numbers
2. Inclusion-exclusion with arithmetic series formula
"""


def sum_multiples_brute_force(limit, divisors=(3, 5)):
    """
    Calculate sum of all multiples of given divisors below limit.

    Brute force approach: O(n) time complexity.

    Args:
        limit: Upper bound (exclusive)
        divisors: Tuple of divisors to check

    Returns:
        Sum of all multiples
    """
    total = 0
    for i in range(1, limit):
        if any(i % d == 0 for d in divisors):
            total += i
    return total


def arithmetic_series_sum(n, limit):
    """
    Calculate sum of multiples of n below limit using arithmetic series.

    Sum = n + 2n + 3n + ... + kn where kn < limit
    Sum = n * (1 + 2 + 3 + ... + k)
    Sum = n * k * (k + 1) / 2

    Args:
        n: The number whose multiples we're summing
        limit: Upper bound (exclusive)

    Returns:
        Sum of multiples of n below limit
    """
    k = (limit - 1) // n
    return n * k * (k + 1) // 2


def sum_multiples_formula(limit):
    """
    Calculate sum using inclusion-exclusion principle with arithmetic series.

    O(1) time complexity.

    Sum of multiples of 3 or 5 =
        Sum of multiples of 3 + Sum of multiples of 5 - Sum of multiples of 15

    (We subtract multiples of 15 because they're counted twice)

    Args:
        limit: Upper bound (exclusive)

    Returns:
        Sum of all multiples of 3 or 5 below limit
    """
    sum_3 = arithmetic_series_sum(3, limit)
    sum_5 = arithmetic_series_sum(5, limit)
    sum_15 = arithmetic_series_sum(15, limit)

    return sum_3 + sum_5 - sum_15


def sum_multiples_generalized(limit, divisors):
    """
    Generalized solution using inclusion-exclusion for any set of divisors.

    Uses the principle: |A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|

    Args:
        limit: Upper bound (exclusive)
        divisors: List of divisors

    Returns:
        Sum of all multiples of any divisor below limit
    """
    from itertools import combinations
    from math import lcm
    from functools import reduce

    total = 0
    n = len(divisors)

    for r in range(1, n + 1):
        for combo in combinations(divisors, r):
            lcm_value = reduce(lcm, combo)
            contribution = arithmetic_series_sum(lcm_value, limit)
            # Add for odd-sized sets, subtract for even-sized sets
            if r % 2 == 1:
                total += contribution
            else:
                total -= contribution

    return total


if __name__ == "__main__":
    print("=" * 60)
    print("Project Euler Problem 1: Multiples of 3 or 5")
    print("=" * 60)

    # Example: Below 10
    print("\nExample: Sum of multiples of 3 or 5 below 10")
    print(f"Multiples: 3, 5, 6, 9")
    print(f"Brute force result: {sum_multiples_brute_force(10)}")
    print(f"Formula result: {sum_multiples_formula(10)}")

    # Problem: Below 1000
    print("\n" + "-" * 60)
    print("Problem: Sum of multiples of 3 or 5 below 1000")
    print("-" * 60)

    brute_result = sum_multiples_brute_force(1000)
    formula_result = sum_multiples_formula(1000)

    print(f"Brute force result: {brute_result}")
    print(f"Formula result: {formula_result}")
    print(f"Results match: {brute_result == formula_result}")

    # Extended example
    print("\n" + "-" * 60)
    print("Extended: Sum of multiples of 3, 5, or 7 below 1000")
    print("-" * 60)

    extended_brute = sum_multiples_brute_force(1000, (3, 5, 7))
    extended_formula = sum_multiples_generalized(1000, [3, 5, 7])

    print(f"Brute force result: {extended_brute}")
    print(f"Generalized formula result: {extended_formula}")
    print(f"Results match: {extended_brute == extended_formula}")

    print("\n" + "=" * 60)
    print(f"ANSWER: {formula_result}")
    print("=" * 60)
