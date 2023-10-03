import unittest

from src.app import example


class TestCaseExampleApp(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_example_happy_path(self) -> None:
        number_a = 1
        number_b = 2
        expected_result = number_a + number_b
        result = example(number_a, number_b)
        self.assertEqual(expected_result, result)

    def test_example_boolean_argument(self) -> None:
        number_a = True
        number_b = False
        expected_result = number_a + number_b
        result = example(number_a, number_b)
        self.assertEqual(expected_result, result)

    def test_example_string_argument(self) -> None:
        number_a = "1"
        number_b = 2

        with self.assertRaises(TypeError):
            example(number_a, number_b)  # type: ignore[arg-type]
