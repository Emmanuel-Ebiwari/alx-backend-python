#!/usr/bin/env python3
"""Unit tests for access_nested_map function in utils module.
"""
import unittest
from unittest.mock import patch, PropertyMock
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
        ("google", {"repos_url": "https://api.github.com/orgs/google"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc"}),
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

    def test_public_repos_url(self) -> None:
        """
        Test that the _public_repos_url property returns the correct URL.
        """
        with patch.object(
            GithubOrgClient,
            'org',
            new_callable=PropertyMock
        ) as mock_org:

            expected_url = "https://api.github.com/orgs/google"
            mock_org.return_value = {
                "repos_url": expected_url}

            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """
        Test that public_repos returns the correct list of repository names.
        """
        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repo_url:

            expected_url = 'https://api.github.com/orgs/microsoft'
            mock_public_repo_url.return_value = expected_url
            mock_get_json.return_value = [
                {"name": "repo1", "license": {"key": "MIT"}},
                {"name": "repo2", "license": {"key": "GPL"}},
                {"name": "repo3", "license": None},
            ]

            client = GithubOrgClient("microsoft")
            result = client.public_repos(license="MIT")
            expected_result = ["repo1"]
            self.assertEqual(result, expected_result)

            mock_get_json.assert_called_once_with(expected_url)
            mock_public_repo_url.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
