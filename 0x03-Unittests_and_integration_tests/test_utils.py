#!/usr/bin/env python3
"""Unit tests for access_nested_map function in utils module.
"""
import unittest
from utils import access_nested_map
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


if __name__ == "__main__":
    unittest.main()
