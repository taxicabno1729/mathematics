"""
Stirling's Approximation for Factorials

Stirling's approximation provides an estimate for n! (n factorial):
    n! ≈ sqrt(2 * pi * n) * (n/e)^n

This is particularly useful for:
- Project Euler Problem 20: Factorial digit sum
- Project Euler Problem 25: Large number calculations
- Any problem requiring factorial approximations for large numbers

The approximation becomes more accurate as n increases.
"""

import math


def stirling_approximation(n):
    """
    Calculate an approximation of n! using Stirling's formula.

    Stirling's formula: n! ≈ sqrt(2 * pi * n) * (n/e)^n

    Args:
        n: A positive integer

    Returns:
        Approximate value of n!
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    return math.sqrt(2 * math.pi * n) * ((n / math.e) ** n)


def stirling_log_factorial(n):
    """
    Calculate log(n!) using Stirling's approximation.

    This is useful when n! is too large to represent directly.
    log(n!) ≈ n*log(n) - n + 0.5*log(2*pi*n)

    Args:
        n: A positive integer

    Returns:
        Approximate value of log(n!)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 0

    return n * math.log(n) - n + 0.5 * math.log(2 * math.pi * n)


def exact_factorial(n):
    """Calculate exact factorial using Python's arbitrary precision integers."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def count_digits_in_factorial(n):
    """
    Count the number of digits in n! using Stirling's approximation.

    Number of digits = floor(log10(n!)) + 1
    Using log10(n!) = log(n!) / log(10)

    Args:
        n: A positive integer

    Returns:
        Number of digits in n!
    """
    if n == 0 or n == 1:
        return 1

    log_factorial = stirling_log_factorial(n)
    log10_factorial = log_factorial / math.log(10)
    return int(log10_factorial) + 1


def compare_accuracy(n):
    """
    Compare Stirling's approximation with exact factorial.

    Args:
        n: A positive integer

    Returns:
        Dictionary with exact value, approximation, and error percentage
    """
    exact = exact_factorial(n)
    approx = stirling_approximation(n)
    error_percent = abs(exact - approx) / exact * 100

    return {
        'n': n,
        'exact': exact,
        'stirling_approx': approx,
        'error_percent': error_percent
    }


if __name__ == "__main__":
    print("=" * 60)
    print("Stirling's Approximation for Factorials")
    print("=" * 60)
    print("\nFormula: n! ≈ sqrt(2*pi*n) * (n/e)^n")
    print("\nComparing accuracy for various values of n:\n")

    print(f"{'n':>5} | {'Exact':>20} | {'Stirling':>20} | {'Error %':>10}")
    print("-" * 60)

    for n in [5, 10, 15, 20, 25, 50]:
        result = compare_accuracy(n)
        print(f"{n:>5} | {result['exact']:>20} | {result['stirling_approx']:>20.0f} | {result['error_percent']:>9.4f}%")

    print("\n" + "=" * 60)
    print("Estimating digits in large factorials:")
    print("=" * 60)

    for n in [100, 1000, 10000]:
        digits = count_digits_in_factorial(n)
        print(f"{n}! has approximately {digits} digits")

    print("\n" + "=" * 60)
    print("Project Euler Problem 20: Sum of digits in 100!")
    print("=" * 60)

    factorial_100 = exact_factorial(100)
    digit_sum = sum(int(d) for d in str(factorial_100))
    print(f"\n100! = {factorial_100}")
    print(f"\nSum of digits in 100! = {digit_sum}")
