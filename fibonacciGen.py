import sys

print(sys.version)
print(sys.executable)


# Original version, unusable for big sequences
def fibonacci1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci1(n - 1) + fibonacci1(n - 2)


for n in range(1, 11):
    print(n, ":", fibonacci1(n))

# ***************************
# Now using explicit memoization
# ***************************
print("\nNow using Memoization\n")
fibonacci_cache = {}


def fibonacci2(n):
    # If we have cached the value, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Otherwise, compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci2(n - 1) + fibonacci2(n - 2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value


for n in range(1, 101):
    print(n, ":", fibonacci2(n))

# ***************************
# Now using a built-in tool
# ***************************
print("\nNow same thing but with a built-in tool\n")

from functools import lru_cache  # Stands for "Least Recently Used Cache"


@lru_cache(maxsize=101)
def fibonacci3(n):
    # First check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive integer.")
    if n < 1:
        raise ValueError("n must be a positive integer.")

    # Compute the nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci3(n - 1) + fibonacci3(n - 2)


for n in range(1, 101):
    print(n, ":", fibonacci3(n))

# Computing the ratio between consecutive terms to see how quickly it grows
print("\nComputing ratio between terms\n")
for n in range(1, 101):
    print(fibonacci3(n + 1) / fibonacci3(n))

# Ends up converging to the golden ratio! 1.618

