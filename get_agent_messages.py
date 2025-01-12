import requests
import json

token = "<token>"
agent_id="Your_agent_id"
url = f"http://localhost:8283/v1/agents/{agent_id}/messages"
print(url)
headers = {
    "Authorization": f"Bearer {token}"
}
response = requests.get(url, headers=headers)
data = response.json()
# print(data)

def extract_conversation_messages(json_data):
    conversations = []
    
    for item in json_data:
        if item["message_type"] == "user_message":
            user_message = json.loads(item["message"])["message"]
            conversations.append({"type": "user", "message": user_message})
        elif item["message_type"] == "tool_call_message" and item.get("tool_call", {}).get("name") == "send_message":
            ai_message = json.loads(item["tool_call"]["arguments"])["message"]
            conversations.append({"type": "ai", "message": ai_message})
    
    return conversations

# Extracting and printing the conversation messages
conversation_messages = extract_conversation_messages(data)
for msg in conversation_messages:
    print(f"{msg['type'].capitalize()}: {msg['message']}")





