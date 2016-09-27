Simple monitoring using requests and unittest on AWS Lambda

How to use:

1. Create a Simple Notification Service (SNS) topic with email recipients and set the ARN as SNS_TOPIC_ARN in checks.py
2. Copy checks_example.py to checks.py and customize with your test cases
3. Create an IAM role called `lambda_sns` with the following policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "sns:*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

4. Run `make package` to create function_package.zip, upload to Lambda
5. Configure Lambda:

Runtime: Python 2.7
Handler: lambda_function.lambda_handler
Role: lambda_sns

6. Configure trigger: 
CloudWatch Events - Schedule
Rule Name: (whatever you want)
Schedule expression: rate(5 minutes) or any interval you like
Enable Trigger checkbox

7. Run your lambda function with a failing test to make sure that SNS is configured correctly with the right permissions.

You can test your checks on your computer outside of Lambda by running 

```
python lambda_function.py
```

with the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID environment variables exported into your shell.


