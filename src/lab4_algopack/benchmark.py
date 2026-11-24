import csv
import statistics
import time

from .datasets import make_dataset
from .sorting import bubble_sort, merge_sort


def run_benchmark(output_file="benchmark.csv", repeats=5):
    if repeats < 5:
        raise ValueError("Для benchmark нужно не менее пяти повторов")

    algorithms = {
        "bubble": bubble_sort,
        "merge": merge_sort,
    }
    kinds = ["random", "sorted", "reverse", "nearly_sorted", "duplicates"]
    rows = []

    for kind in kinds:
        for size in [100, 1000, 10000]:
            for algorithm_name, algorithm in algorithms.items():
                # Bubble sort на 10000 элементах слишком медленный.
                if algorithm_name == "bubble" and size == 10000:
                    continue

                times = []

                for repeat in range(repeats):
                    data = make_dataset(size, kind, seed=repeat)

                    # Время создания списка не входит в измерение.
                    start = time.perf_counter()
                    algorithm(data.copy())
                    elapsed = time.perf_counter() - start
                    times.append(elapsed)

                rows.append({
                    "algorithm": algorithm_name,
                    "kind": kind,
                    "size": size,
                    "repeats": repeats,
                    "average_seconds": statistics.mean(times),
                })

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "algorithm",
                "kind",
                "size",
                "repeats",
                "average_seconds",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    return rows


if __name__ == "__main__":
    results = run_benchmark()

    for row in results:
        print(
            row["algorithm"],
            row["kind"],
            row["size"],
            f'{row["average_seconds"]:.6f} сек.',
        )

    print("Отчёт сохранён в benchmark.csv")