import unittest
import requests

SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:EXAMPLE:CHANGE_ME'

class TestUrls(unittest.TestCase):
  # test case function names must begin with "test" !

  def test_example_passing_test(self):
    response = requests.get("https://github.com/bdon")
    self.assertEqual(response.status_code,200)

  def test_example_failing_test(self):
    response = requests.get("https://github.com/bdon")
    self.assertEqual(response.status_code,404)
