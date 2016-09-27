bundle:
	echo "Creating lambda bundle..."
	zip -r lambdamon.zip lambda_function.py checks.py check_url.py requests
