#!/usr/bin/env python3
"""
a python unit test for client files
"""
import unittest
import requests
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized



class TestGithubOrgClient(unittest.TestCase):
    """ a class to implement github or client class"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mk_obj):
        """
        test_org- function to test the github org
        Arguments:
            org_name: the given name of the organization
        Returns:
            ok if it succedd fail otherwise
        """
        tst_cls = GithubOrgClient(org_name)
        tst_cls.org()
        mk_obj.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name))

    def test_public_repos_url(self):
        """
        test_public_repos_url - functin to test the public repos url
        Arguments:
            nothing
        Returns:
            ok if it succeded fail otherwise
        """
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=PropertyMock) as mk:
            pload = {'repos_url': 'test'}
            mk.return_value = pload
            tst_cls = GithubOrgClient('test')
            rslt = tst_cls._public_repos_url
            self.assertEqual(rslt, pload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mk_jsn):
        """
        test_public_repos - function to test public repos
        Arguments:
            mk_json - the given moke object for get json
        Returns:
            ok if it succeded fail otherwise
        """
        test = {'org': 'Facebook', 'org': 'LinkedIn'}
        mk_jsn.return_value = test

        with mock.path('client.GithubOrgClient._public_repos_url',
                        new_callable=PropertyMock) as mk_repo:
            mk_repo.return_value = 'test/test123'
            tst_cls = GithubOrgClient('test')
            rslt = tst_cls.public_repos()

            jsn_rslt = [i['org'] for i in test]
            self.assertEqual(jsn_rslt, rslt)

            mk_jsn.assert_called_once()
            mk_repo.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, rslt):
        """
        test_has_license - method to test the has_license method of client cls
        Arguments:
            repo: the given repository
            license_key: the license key
        Returns:
            ok if it succeded fail otherwise
        """
        tst_cls = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(tst_cls, rslt)
