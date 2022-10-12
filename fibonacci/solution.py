
def fibonacci(n):
    if n <= 2:
        return 1
    if not hasattr(fibonacci, 'cache'):
        fibonacci.cache = {}
    if n not in fibonacci.cache:
        fibonacci.cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci.cache[n]


if __name__ == '__main__':
    print(fibonacci(6))
