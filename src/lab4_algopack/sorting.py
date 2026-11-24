def _check_list(values):
    if not isinstance(values, list):
        raise TypeError("Ожидался список чисел")


def bubble_sort(values):
    _check_list(values)
    result = values.copy()

    for end in range(len(result) - 1, 0, -1):
        swapped = False

        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = (
                    result[index + 1],
                    result[index],
                )
                swapped = True

        if not swapped:
            break

    return result


def merge_sort(values):
    _check_list(values)

    if len(values) <= 1:
        return values.copy()

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result