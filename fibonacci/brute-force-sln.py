"""
Brute force solution for the fibonacci sequence.
Has a time complexity of O(2^n)
"""

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(6))
