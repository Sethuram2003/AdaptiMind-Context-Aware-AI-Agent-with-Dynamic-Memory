import json
import requests

AGENT_ID = "agent-122c11da-8061-49ae-9edc-d121f6b18c5c"
url = f"http://localhost:8283/v1/agents/{AGENT_ID}/messages"

token = "<token>"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    messages = response.json()
    for message in messages:
        if not isinstance(message, dict):
            print(f"Unexpected message format: {message}")
            continue

        if message.get("message_type") == "user_message":
            try:
                message_content = json.loads(message["message"])
                user_message = message_content.get("message", "Unknown message")
                print(f"User: {user_message}")
            except json.JSONDecodeError:
                print(f"Failed to decode user message: {message['message']}")
                user_message = "Unknown message"
        
        elif (
            message.get("message_type") == "tool_call_message" and 
            message.get("tool_call", {}).get("name") == "send_message"
        ):
            try:
                tool_call_args = json.loads(message["tool_call"]["arguments"])
                ai_message = tool_call_args.get("message", "Unknown AI message")
                print(f"AI: {ai_message}")
            except json.JSONDecodeError:
                print(f"Failed to decode AI message: {message['tool_call']['arguments']}")
                ai_message = "Unknown AI message"
else:
    print(f"Failed to get the reply. Status code: {response.status_code}, Response: {response.text}")
