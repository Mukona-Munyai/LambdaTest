import json
import boto3

client = boto3.client('lambda')

response = client.invoke(
    FunctionName='BasicCalc',
    Payload=json.dumps({"num1": 987, "num2": 243, "operation": "multiply"})
)

response_payload = response['Payload'].read()
print(response_payload)

