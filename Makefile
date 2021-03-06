generate: generate-spec generate-sdk

generate-spec:
	python generate_specification.py

generate-sdk:
	openapi-generator generate -i app/openapi.json -g typescript-angular -o front-end/openapi-sdk
