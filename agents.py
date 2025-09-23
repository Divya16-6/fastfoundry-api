import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv
from azure.identity import InteractiveBrowserCredential

# Loading environment variables
load_dotenv()

foundry_endpoint = os.getenv("FOUNDRY_ENDPOINT") # Fetching the Foundry endpoint for the env file

def createAIClient():
    credential = InteractiveBrowserCredential() # Using InteractiveBrowserCredential, I'm providing the credential once the API is trigger in web
    client = AIProjectClient(
        credential=credential,
        endpoint=foundry_endpoint
    )   # creating the client using the foundry endpoint and the credential
    return client