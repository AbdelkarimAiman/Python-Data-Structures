"""
Big O Complexity Examples
-------------------------
Description: A demonstration of various time complexity classes using Python.
This script serves as an educational reference for understanding algorithm efficiency.
"""

import time

def constant_time(items: list) -> None:
    """
    O(1) - Constant Time
    --------------------
    The execution time remains the same regardless of the input size.
    Example: Accessing an element by index.
    """
    if items:
        print(f"First element: {items[0]}") # One operation
    print("-> O(1) Complexity: Fast and predictable.")


def logarithmic_time(n: int) -> None:
    """
    O(log n) - Logarithmic Time
    ---------------------------
    The number of steps increases by 1 each time the input doubles.
    Common in Binary Search algorithms.
    """
    i = 1
    steps = 0
    while i < n:
        i = i * 2  # The problem space is cut in half (or doubled) each step
        steps += 1
    print(f"-> O(log n) Complexity: Input {n} took {steps} steps.")


def linear_time(n: int) -> None:
    """
    O(n) - Linear Time
    ------------------
    Execution time grows directly in proportion to the input size.
    Example: Simple loops.
    """
    count = 0
    for _ in range(n):
        count += 1
    print(f"-> O(n) Complexity: Processed {n} items.")


def quadratic_time(n: int) -> None:
    """
    O(n^2) - Quadratic Time
    -----------------------
    Performance is directly proportional to the square of the input size.
    Common in nested loops (e.g., Bubble Sort).
    """
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print(f"-> O(n^2) Complexity: Input {n} resulted in {count} operations.")


def cubic_time(n: int) -> None:
    """
    O(n^3) - Cubic Time
    -------------------
    Common in algorithms involving triple nested loops.
    Expensive for large inputs.
    """
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    print(f"-> O(n^3) Complexity: Input {n} resulted in {count} operations.")


def independent_variables(n: int, m: int) -> None:
    """
    O(n * m) - Independent Quadratic Time
    -------------------------------------
    Complexity depends on two different input variables.
    """
    count = 0
    for i in range(n):
        for j in range(m):
            count += 1
    print(f"-> O(n * m) Complexity: Inputs {n} and {m} resulted in {count} operations.")


def exponential_time(n: int) -> int:
    """
    O(2^n) - Exponential Time
    -------------------------
    The execution time doubles with each addition to the input data set.
    Example: Recursive Fibonacci (without memoization).
    WARNING: Very slow for large n.
    """
    if n <= 1:
        return n
    return exponential_time(n-1) + exponential_time(n-2)


# --- Main Execution ---
if __name__ == "__main__":
    print("---  Big O Complexity Examples ---\n")

    # 1. Test Constant Time O(1)
    sample_data = [10, 20, 30, 40, 50]
    print("[1] Testing Constant Time O(1):")
    constant_time(sample_data)
    print("-" * 40)

    # 2. Test Logarithmic Time O(log n)
    print("\n[2] Testing Logarithmic Time O(log n):")
    # Log2(64) should be 6 steps
    logarithmic_time(64)
    print("-" * 40)

    # 3. Test Linear Time O(n)
    print("\n[3] Testing Linear Time O(n):")
    linear_time(10)
    print("-" * 40)

    # 4. Test Quadratic Time O(n^2)
    print("\n[4] Testing Quadratic Time O(n^2):")
    # 10 * 10 should result in 100 operations
    quadratic_time(10)
    print("-" * 40)

    # 5. Test Cubic Time O(n^3)
    print("\n[5] Testing Cubic Time O(n^3):")
    # 10 * 10 * 10 should result in 1000 operations
    cubic_time(10)
    print("-" * 40)

    # 6. Test Independent Variables O(n * m)
    print("\n[6] Testing Independent Variables O(n * m):")
    independent_variables(5, 10)
    print("-" * 40)

    # 7. Test Exponential Time O(2^n)
    # WARNING: Even a small number like 30 takes time. 
    n_exp = 30
    print(f"\n[7] Testing Exponential Time O(2^n) with n={n_exp}:")
    
    start_time = time.time()
    result = exponential_time(n_exp)
    end_time = time.time()
    
    print(f"Fibonacci({n_exp}) result: {result}")
    print(f"-> O(2^n) Complexity: Calculation took {end_time - start_time:.4f} seconds.")
    print("   Notice how slow this is compared to O(n) for just input 30!")
    print("-" * 40)

    print("\n--- Demonstration Complete ---")