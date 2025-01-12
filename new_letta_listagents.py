import requests
import json

token = "<token>"
url = "http://localhost:8283/v1/agents/"
headers = {
    "Authorization": f"Bearer {token}"
}
response = requests.get(url, headers=headers)
data = response.json()

for agent in data:
    print("-" * 55)  

    agent_id = agent.get("id", "N/A")  
    name = agent.get("name", "N/A")    
    model = agent.get("llm_config", {}).get("model", "N/A")  
    
    print(f"Agent ID: {agent_id}")
    print(f"Name: {name}")
    print(f"Model: {model}")
    print("-" * 55)  

