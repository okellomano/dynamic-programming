fibonacci_cache = {}

def fibonacci(n):
    if n <= 2:
        return 1
    if n not in fibonacci_cache:
        fibonacci_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_cache[n]


if __name__ == '__main__':
    print(fibonacci(6))
    