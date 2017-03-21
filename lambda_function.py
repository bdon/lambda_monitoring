import checks

import requests
import boto3
import unittest

client = boto3.client('sns',region_name='us-west-2')

def lambda_handler(event,context):
  loader = unittest.TestLoader()
  suite = loader.loadTestsFromModule(checks)
  result = unittest.TestResult()
  suite.run(result)
  print result
  messages = result.errors + result.failures

  if len(messages) > 0:
    client.publish(
        TopicArn=checks.SNS_TOPIC_ARN,
        Message="\n".join(map(lambda m:m[1],messages)),
        Subject='{0} tests failed'.format(len(messages))
    )

if __name__ == "__main__":
  lambda_handler({},{})
