import requests
import time
API_KEY = "TODO"
API_URL = "https://api.anthropic.com/v1/messages"

headers = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY,
    "anthropic-version": "2023-06-01"
}

def request_claude(prompt, max_tokens=1024, messages=None):
    if messages is not None:
        data = {
            "model": "claude-3-5-sonnet-20240620",
            "max_tokens": max_tokens,
            "messages": messages
        }
    else:
        data = {
            "model": "claude-3-5-sonnet-20240620",
            "max_tokens": max_tokens,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    response = requests.post(API_URL, json=data, headers=headers)
    time.sleep(4)
    if response.status_code == 200:
        result = response.json()
        return result['content'][0]['text']
    else:
        return f"Error: {response.status_code}, {response.text}"
