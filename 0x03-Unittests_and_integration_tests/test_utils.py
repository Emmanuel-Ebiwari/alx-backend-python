#!/usr/bin/env python3
"""Unit tests for access_nested_map function in utils module.
"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_value: Any
    ) -> None:
        """
        Test that access_nested_map returns the correct value
        when provided with a valid nested map and path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_value)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_value: Any
    ) -> None:
        """
        Test that access_nested_map returns the correct value
        when provided with a valid nested map and path.
        """
        with self.assertRaises(expected_value):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test suite for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, expected_value: dict) -> None:
        """
        Test that get_json returns a dictionary when provided with a valid URL.
        """
        # Using `with patch` to avoid issues with
        # argument order in @parameterized.expand
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = expected_value
            mock_get.return_value = mock_response

            result = get_json(test_url)
            self.assertEqual(result, expected_value)

            # Assert that requests.get was called once with the correct URL
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test suite for the memoize function."""

    def test_memoize(self) -> None:
        """
        Test that memoize caches the result of a function call.
        """
        class TestClass:

            def a_method(self) -> int:
                """A method that returns a fixed value."""
                print("a_method called")
                return 42

            @memoize
            def a_property(self) -> int:
                """A property that calls a_method and caches the result."""
                return self.a_method()

        with patch.object(
            TestClass,
            "a_method",
            return_value=42
        ) as mock_method:
            instance = TestClass()

            # First call: should trigger a_method
            result1 = instance.a_property
            # Second call: should use cached value
            result2 = instance.a_property
            print("First call result:", result1)
            print("Second call result:", result2)

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method was called only once due to memoization
            mock_method.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
