#!/usr/bin/env python3
""" Parameterize and patch as decorators """

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient class """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mock_get_json):
        """ Test org method """
        test_class = GithubOrgClient(test_org_name)
        test_class.org()
        mock_get_json.assert_called_once_with
        (f'https://api.github.com/orgs/{test_org_name}')

    def test_public_repos_url(self):
        """ Test _public_repos_url method """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = TEST_PAYLOAD
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class._public_repos_url,
                             mock_public_repos_url.return_value)
            mock_public_repos_url.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test public_repos method """
        mock_get_json.return_value = {
                "repo1": {"name": "repo1", "license": {"key": "my_license"}},
                "repo2": {"name": "repo2", "license": {"key": "other_license"}}
            }
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class.public_repos(),
                             mock_get_json.return_value)
            mock_get_json.assert_called_once_with
            (mock_public_repos_url.return_value)
            mock_public_repos_url.assert_called_once()

    def test_public_repos_with_license(self):
        """ Test public_repos method with license """
        repo = {'license': {'key': 'my_license'}}
        with patch('client.GithubOrgClient.public_repos',
                   new_callable=PropertyMock) as mock_public_repos:
            mock_public_repos.return_value = [repo]
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class.public_repos('my_license'),
                             [repo])
            mock_public_repos.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test has_license method """
        test_class = GithubOrgClient('test')
        self.assertEqual(test_class.has_license(repo, license_key), expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ TestIntegrationGithubOrgClient class """

    @classmethod
    def setUpClass(cls):
        """" Set up class """
        cls.get_patcher = patch('requests.get',
                                side_effect=[cls.org_payload,
                                             cls.repos_payload])
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test public_repos method """
        test_class = GithubOrgClient('test')
        self.assertEqual(test_class.public_repos(), self.expected_repos)
