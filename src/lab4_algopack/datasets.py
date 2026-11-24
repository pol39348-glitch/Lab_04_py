import random


def make_dataset(size, kind="random", seed=None):

    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size должно быть целым числом")
    
    if size < 0:
        raise ValueError("size не должно быть отрицательным")

    allowed_kinds = {
        "random",
        "sorted",
        "reverse",
        "nearly_sorted",
        "duplicates",
    }
    if kind not in allowed_kinds:
        raise ValueError("Неизвестный вид набора данных")

    generator = random.Random(seed)

    if kind == "random":
        return [generator.randint(-10000, 10000) for _ in range(size)]

    if kind == "sorted":
        return list(range(size))

    if kind == "reverse":
        return list(range(size - 1, -1, -1))

    if kind == "nearly_sorted":
        values = list(range(size))
        swaps = max(1, size // 20)

        for _ in range(swaps):
            if size > 1:
                first = generator.randrange(size)
                second = generator.randrange(size)
                values[first], values[second] = values[second], values[first]

        return values

    return [generator.randint(-5, 5) for _ in range(size)]