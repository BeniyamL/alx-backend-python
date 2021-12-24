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
        mk_obj.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
