import unittest

from lab4_algopack import (
    Stack,
    bubble_sort,
    fibonacci_iterative,
    fibonacci_recursive,
    make_dataset,
    merge_sort,
)


class FibonacciTests(unittest.TestCase):
    def test_both_versions(self):
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_iterative(10), 55)
        self.assertEqual(fibonacci_recursive(10), 55)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)


class SortingTests(unittest.TestCase):
    def test_sorting_examples(self):
        examples = [
            [],
            [1],
            [1, 2, 3],
            [3, 2, 1],
            [4, 1, 4, -2, 0],
        ]

        for values in examples:
            expected = sorted(values)
            original = values.copy()

            self.assertEqual(bubble_sort(values), expected)
            self.assertEqual(merge_sort(values), expected)
            self.assertEqual(values, original)

    def test_random_lists(self):
        for seed in range(10):
            values = make_dataset(50, "random", seed=seed)
            expected = sorted(values)

            self.assertEqual(bubble_sort(values), expected)
            self.assertEqual(merge_sort(values), expected)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            merge_sort((3, 2, 1))


class StackTests(unittest.TestCase):
    def test_stack_operations(self):
        stack = Stack()

        self.assertFalse(stack)
        self.assertEqual(len(stack), 0)

        stack.push(10)
        stack.push(20)

        self.assertTrue(stack)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertFalse(stack)

    def test_empty_stack(self):
        stack = Stack()

        with self.assertRaises(IndexError):
            stack.pop()

        with self.assertRaises(IndexError):
            stack.peek()


class DatasetTests(unittest.TestCase):
    def test_same_seed_gives_same_data(self):
        first = make_dataset(20, "random", seed=42)
        second = make_dataset(20, "random", seed=42)
        self.assertEqual(first, second)

    def test_different_seeds_usually_differ(self):
        first = make_dataset(20, "random", seed=1)
        second = make_dataset(20, "random", seed=2)
        self.assertNotEqual(first, second)


if __name__ == "__main__":
    unittest.main()