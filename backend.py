import boto3

client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")

KNOWLEDGE_BASE_ID = "P1O1GQ9CUT"
MODEL_ARN = "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-lite-v1:0"

def get_answer(query):
    try:
        response = client.retrieve_and_generate(
            input={"text": query},
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                    "modelArn": MODEL_ARN
                }
            }
        )

        
        answer = response["output"]["text"]

        
        if "Response:" in answer:
            answer = answer.split("Response:")[-1].strip()

        if "Action:" in answer:
            answer = answer.split("Action:")[0].strip()

        
        source_uris = []
        citations = response.get("citations", [])

        for citation in citations:
            refs = citation.get("retrievedReferences", [])
            for ref in refs:
                location = ref.get("location", {})
                s3_location = location.get("s3Location", {})
                uri = s3_location.get("uri")
                if uri and uri not in source_uris:
                    source_uris.append(uri)

        return answer, source_uris

    except Exception as e:
        return f"Error: {str(e)}", []
