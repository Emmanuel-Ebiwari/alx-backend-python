#!/usr/bin/env python3
"""Unit tests for access_nested_map function in utils module.
"""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
)


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"org_url": "https://api.github.com/orgs/google"}),
        ("abc", {"org_url": "https://api.github.com/orgs/abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org, mocked_payload, mock_get_json) -> None:
        """
        Test that GithubOrgClient.org returns the correct value and
        that get_json is called once with the expected URL.
        """
        mock_get_json.return_value = mocked_payload
        client = GithubOrgClient(org)
        result = client.org

        expected_url = f"https://api.github.com/orgs/{org}"
        mock_get_json.assert_called_once_with(expected_url)

        mock_get_json.return_value = mocked_payload
        self.assertEqual(result, mocked_payload)


if __name__ == "__main__":
    unittest.main()
