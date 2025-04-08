import requests

def send_api_request(data):
    url = "https://webhook.site/578e3174-4e10-4ae4-a2ee-0aa1cec51950"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer test-token-xyz"
    }

    response = requests.post(url, json=data, headers=headers)
    return response
