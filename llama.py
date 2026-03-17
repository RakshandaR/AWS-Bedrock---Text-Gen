import boto3
import json

prompt_data="""
Act as a Shakespeare and write a poem on Genertaive AI
"""

# connecting to the service 
bedrock=boto3.client(service_name="bedrock-runtime")


payload={
    "prompt":"[INST]"+ prompt_data +"[/INST]",         # [INST] - comes from the json format
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}
body=json.dumps(payload)
model_id="meta.llama3-8b-instruct-v1:0"

# inserted as per the API dcoumentation refernece 
response=bedrock.invoke_model(
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
    body=body
)

response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generation']
print(repsonse_text)