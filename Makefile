package:
	echo "Creating lambda function package..."
	zip -r function_package.zip lambda_function.py checks.py requests
