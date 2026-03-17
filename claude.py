import boto3
import json

prompt_data = """
Act as Shakespeare and write a poem on Generative AI
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 512,
    "temperature": 0.8,
    "messages": [
        {
            "role": "user",
            "content": prompt_data
        }
    ]
}

body = json.dumps(payload)

model_id = "arn:aws:bedrock:us-east-1:251383864846:application-inference-profile/ge5jv8s01t6s"

response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response["body"].read())

response_text = response_body["content"][0]["text"]

print(response_text)