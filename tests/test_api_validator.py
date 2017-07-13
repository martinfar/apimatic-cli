import os
import mock
import time
import unittest

from apimaticcli.api_validator import APIValidator
from apimaticcli.argument_parser import ArgumentParser
from apimaticcli.apimatic.models.validation_summary import ValidationSummary

class TestAPIValidator(unittest.TestCase):
    def test_validate_from_key(self):
        args = [
            'validate', 'fromapikey',
            '--api-key', os.environ['APIMATIC_ERROR_KEY']
        ]
        arguments = ArgumentParser.parse(args)
        with mock.patch('apimaticcli.api_validator.APIValidator.process_summary') as p_sum:
            APIValidator.from_key(arguments)
            args, kwargs = p_sum.call_args
            self.assertTrue(isinstance(args[0], ValidationSummary))
            self.assertEqual(args[0].success, False)
            self.assertGreater(len(args[0].errors), 0)

    def test_from_user_url(self):
        args = [
            'validate', 'fromuser',
            '--email', os.environ['APIMATIC_EMAIL'],
            '--password', os.environ['APIMATIC_PASSWORD'],
            '--url', 'https://raw.githubusercontent.com/DudeSolutions/CoreApi/master/apiary.apib'
        ]
        arguments = ArgumentParser.parse(args)
        with mock.patch('apimaticcli.api_validator.APIValidator.process_summary') as p_sum:
            APIValidator.from_user(arguments)
            args, kwargs = p_sum.call_args
            self.assertTrue(isinstance(args[0], ValidationSummary))
            self.assertTrue(isinstance(args[0].success, bool))

    def test_from_user_file(self):
        args = [
            'validate', 'fromuser',
            '--email', os.environ['APIMATIC_EMAIL'],
            '--password', os.environ['APIMATIC_PASSWORD'],
            '--file', './tests/data/calculator.json'
        ]
        arguments = ArgumentParser.parse(args)
        with mock.patch('apimaticcli.api_validator.APIValidator.process_summary') as p_sum:
            APIValidator.from_user(arguments)
            args, kwargs = p_sum.call_args
            self.assertTrue(isinstance(args[0], ValidationSummary))
            self.assertEqual(args[0].success, True)
            self.assertEqual(len(args[0].errors), 0)

    def test_from_auth_url(self):
        args = [
            'validate', 'fromauthkey',
            '--auth-key', os.environ['APIMATIC_AUTH_KEY'],
            '--url', 'https://raw.githubusercontent.com/DudeSolutions/CoreApi/master/apiary.apib'
        ]
        arguments = ArgumentParser.parse(args)
        with mock.patch('apimaticcli.api_validator.APIValidator.process_summary') as p_sum:
            APIValidator.from_user(arguments)
            args, kwargs = p_sum.call_args
            self.assertTrue(isinstance(args[0], ValidationSummary))
            self.assertTrue(isinstance(args[0].success, bool))

    def test_from_auth_file(self):
        args = [
            'validate', 'fromauthkey',
            '--auth-key', os.environ['APIMATIC_AUTH_KEY'],
            '--file', './tests/data/calculator.json'
        ]
        arguments = ArgumentParser.parse(args)
        with mock.patch('apimaticcli.api_validator.APIValidator.process_summary') as p_sum:
            APIValidator.from_user(arguments)
            args, kwargs = p_sum.call_args
            self.assertTrue(isinstance(args[0], ValidationSummary))
            self.assertEqual(args[0].success, True)
            self.assertEqual(len(args[0].errors), 0)

    def tearDown(self):
       time.sleep(2)
