
from ast import arg


def cached(f):
    """
    A cache decorator for the fibonacci function.
    """
    cache = {}

    def worker(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return worker


@cached
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(6))
