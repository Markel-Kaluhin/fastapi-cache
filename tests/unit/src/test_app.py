import unittest

from src.app import Cache


class TestCaseCacheApp(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_example_happy_path(self) -> None:
        cache = Cache()
        self.assertIsInstance(cache, Cache)
