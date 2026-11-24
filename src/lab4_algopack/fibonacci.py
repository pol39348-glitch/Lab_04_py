def _check_n(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n должно быть целым числом")
    if n < 0:
        raise ValueError("n не должно быть отрицательным")


def fibonacci_iterative(n):
    _check_n(n)

    previous = 0
    current = 1

    for _ in range(n):
        previous, current = current, previous + current

    return previous


def fibonacci_recursive(n):
    _check_n(n)

    memo = {0: 0, 1: 1}

    def calculate(number):
        if number not in memo:
            memo[number] = calculate(number - 1) + calculate(number - 2)
        return memo[number]

    return calculate(n)