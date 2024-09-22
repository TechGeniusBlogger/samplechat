import os
import openai
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# # Set up Azure credentials
# credential = DefaultAzureCredential()
# key_vault_name = "chattechgeniusblog "
# key_vault_uri = f"https://{key_vault_name}.vault.azure.net"
# secret_client = SecretClient(vault_url=key_vault_uri, credential=credential)

# # Retrieve OpenAI API key from Azure Key Vault
# openai_api_key = secret_client.get_secret("OpenAI-API-Key").value

# Set OpenAI API key
openai.api_key = f0b9cd46e2624e5aaa2cc0726c48bc3a

# Function to generate a response from OpenAI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1500
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    response = generate_response(user_prompt)
    print("Response from OpenAI:", response)

