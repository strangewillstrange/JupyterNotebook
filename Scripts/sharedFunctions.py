## Generate token
import requests
from requests.auth import HTTPBasicAuth
import json
import uuid
import configparser

header_correlation_id = 'x-correlation-id'
header_content_type = 'Content-Type'
header_client = 'x-client-id'
header_host = 'host'

def create_token (environment):
    token_url =  'https://wills-orchestrator.' + environment + '.private.strange.com:443'

    token_headers = {
        header_correlation_id: str( uuid.uuid4() ),
        header_content_type: 'application/json',
        header_host: 'https://wills-orchestrator.' + environment + '.private.strange.com'
    }

    # submit token request
    token_response = requests.get(token_url, header=token_headers, verify=False)

    # parse token
    payload = token_response.json()
    return "Bearer " + payload['token']