"""
Project Euler Problem 6: Sum Square Difference

The sum of the squares of the first ten natural numbers is:
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the square of the sum and the sum of the squares
is 3025 - 385 = 2640.

Find the difference between the square of the sum of the first one hundred
natural numbers and the sum of their squares.

Solution approaches:
1. Brute force - iterate and compute
2. Closed-form formulas:
   - Sum of first n numbers: n(n+1)/2
   - Sum of squares of first n numbers: n(n+1)(2n+1)/6
"""


def sum_square_difference_brute(n):
    """
    Calculate the difference using brute force iteration.

    Args:
        n: Upper bound (inclusive)

    Returns:
        square_of_sum - sum_of_squares
    """
    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2

    return square_of_sum - sum_of_squares


def sum_of_n(n):
    """
    Calculate sum of first n natural numbers using Gauss formula.

    1 + 2 + 3 + ... + n = n(n+1)/2

    Args:
        n: Number of terms

    Returns:
        Sum of 1 to n
    """
    return n * (n + 1) // 2


def sum_of_squares(n):
    """
    Calculate sum of squares of first n natural numbers.

    1^2 + 2^2 + 3^2 + ... + n^2 = n(n+1)(2n+1)/6

    Derivation: Can be proven using telescoping series or induction.

    Args:
        n: Number of terms

    Returns:
        Sum of squares from 1^2 to n^2
    """
    return n * (n + 1) * (2 * n + 1) // 6


def sum_of_cubes(n):
    """
    Calculate sum of cubes of first n natural numbers.

    1^3 + 2^3 + 3^3 + ... + n^3 = [n(n+1)/2]^2

    Interesting fact: Sum of cubes equals the square of the sum!

    Args:
        n: Number of terms

    Returns:
        Sum of cubes from 1^3 to n^3
    """
    return (n * (n + 1) // 2) ** 2


def sum_square_difference_formula(n):
    """
    Calculate the difference using closed-form formulas.

    Let S = sum of 1 to n = n(n+1)/2
    Let Q = sum of squares = n(n+1)(2n+1)/6

    Difference = S^2 - Q

    This can be simplified to:
    Difference = [n(n+1)/2]^2 - n(n+1)(2n+1)/6
               = n(n+1)/2 * [n(n+1)/2 - (2n+1)/3]
               = n(n+1)/2 * [3n(n+1) - 2(2n+1)] / 6
               = n(n+1)/2 * [3n^2 + 3n - 4n - 2] / 6
               = n(n+1)/2 * [3n^2 - n - 2] / 6
               = n(n+1)(3n^2 - n - 2) / 12
               = n(n+1)(n-1)(3n+2) / 12

    Args:
        n: Upper bound (inclusive)

    Returns:
        square_of_sum - sum_of_squares
    """
    square_of_sum = sum_of_n(n) ** 2
    sum_sq = sum_of_squares(n)

    return square_of_sum - sum_sq


def sum_square_difference_direct(n):
    """
    Calculate using the most simplified direct formula.

    Difference = n(n+1)(n-1)(3n+2) / 12

    Args:
        n: Upper bound (inclusive)

    Returns:
        square_of_sum - sum_of_squares
    """
    return n * (n + 1) * (n - 1) * (3 * n + 2) // 12


if __name__ == "__main__":
    print("=" * 60)
    print("Project Euler Problem 6: Sum Square Difference")
    print("=" * 60)

    # Example: n = 10
    print("\nExample with n = 10:")
    print("-" * 60)

    n = 10
    print(f"Sum of 1 to {n}: {sum_of_n(n)}")
    print(f"Sum of squares (1^2 to {n}^2): {sum_of_squares(n)}")
    print(f"Square of sum: {sum_of_n(n) ** 2}")

    brute_10 = sum_square_difference_brute(10)
    formula_10 = sum_square_difference_formula(10)
    direct_10 = sum_square_difference_direct(10)

    print(f"\nDifference (brute force): {brute_10}")
    print(f"Difference (formula): {formula_10}")
    print(f"Difference (direct): {direct_10}")

    # Problem: n = 100
    print("\n" + "=" * 60)
    print("Problem with n = 100:")
    print("=" * 60)

    n = 100
    print(f"\nSum of 1 to {n}: {sum_of_n(n)}")
    print(f"Sum of squares (1^2 to {n}^2): {sum_of_squares(n)}")
    print(f"Square of sum: {sum_of_n(n) ** 2}")

    brute_100 = sum_square_difference_brute(100)
    formula_100 = sum_square_difference_formula(100)
    direct_100 = sum_square_difference_direct(100)

    print(f"\nDifference (brute force): {brute_100}")
    print(f"Difference (formula): {formula_100}")
    print(f"Difference (direct): {direct_100}")
    print(f"All methods match: {brute_100 == formula_100 == direct_100}")

    # Bonus: Interesting relationship
    print("\n" + "=" * 60)
    print("Bonus: Sum of Cubes = Square of Sum!")
    print("=" * 60)

    for n in [5, 10, 15]:
        cube_sum = sum_of_cubes(n)
        sum_squared = sum_of_n(n) ** 2
        print(f"n={n}: Sum of cubes = {cube_sum}, (Sum of n)^2 = {sum_squared}")

    print("\n" + "=" * 60)
    print(f"ANSWER: {formula_100}")
    print("=" * 60)
