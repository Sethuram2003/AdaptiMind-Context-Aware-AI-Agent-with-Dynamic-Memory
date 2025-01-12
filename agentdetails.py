import requests
import json

token = "<token>"
agent_id="Your_agent_id"
url = f"http://localhost:8283/v1/agents/{agent_id}/context"
headers = {
    "Authorization": f"Bearer {token}"
}
response = requests.get(url, headers=headers)
data = response.json()
context_window_size_max = data.get("context_window_size_max", "N/A")
context_window_size_current = data.get("context_window_size_current", "N/A")
num_messages = data.get("num_messages", "N/A")
num_archival_memory = data.get("num_archival_memory", "N/A")
num_recall_memory = data.get("num_recall_memory", "N/A")
num_tokens_external_memory_summary = data.get("num_tokens_external_memory_summary", "N/A")
external_memory_summary = data.get("external_memory_summary", "N/A")
num_tokens_system = data.get("num_tokens_system", "N/A")
system_prompt = data.get("system_prompt", "N/A")
num_tokens_core_memory = data.get("num_tokens_core_memory", "N/A")
core_memory = data.get("core_memory", "N/A")
num_tokens_summary_memory = data.get("num_tokens_summary_memory", "N/A")
num_tokens_functions_definitions = data.get("num_tokens_functions_definitions", "N/A")
num_tokens_messages = data.get("num_tokens_messages", "N/A")

print(f"context_window_size_max: {context_window_size_max}")
print(f"context_window_size_current: {context_window_size_current}")
print(f"num_messages: {num_messages}")
print(f"num_archival_memory: {num_archival_memory}")
print(f"num_recall_memory: {num_recall_memory}")
print(f"num_tokens_external_memory_summary: {num_tokens_external_memory_summary}")
print(f"external_memory_summary: {external_memory_summary}")
print(f"num_tokens_system: {num_tokens_system}")
print(f"system_prompt: {system_prompt}")
print(f"num_tokens_core_memory: {num_tokens_core_memory}")
print(f"core_memory: {core_memory}")
print(f"num_tokens_summary_memory: {num_tokens_summary_memory}")
print(f"num_tokens_functions_definitions: {num_tokens_functions_definitions}")
print(f"num_tokens_messages: {num_tokens_messages}")


