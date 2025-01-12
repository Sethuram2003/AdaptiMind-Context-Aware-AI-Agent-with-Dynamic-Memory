# 🤖 LLM Memory Toolkit

A stateful AI agent built on the Letta platform using Llama 3.1, featuring dynamic memory management and custom tool integration for enhanced conversational experiences.

<div align="center">

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Llama](https://img.shields.io/badge/Llama_3.1-A100FF?style=for-the-badge&logo=llama&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-FF4B4B?style=for-the-badge&logo=ollama&logoColor=white)

</div>

## 📚 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example Conversations](#example-conversations)
- [Technical Details](#technical-details)
- [Contributing](#contributing)

## ✨ Features

- **Stateful Conversations**: Maintains context and memory across interactions
- **Local Model Hosting**: Uses Ollama for running Llama 3.1 locally
- **Custom Tool Integration**: Enhanced capabilities with specialized tools
- **Dynamic Learning**: Evolves through user interactions
- **Memory Management**: Sophisticated state handling and updates
- **Persona Customization**: Configurable agent personality and behavior

## 🗂️ Project Structure

```
llm-mem-toolkit/
├── LICENSE
├── Letta_system_persona     # System instructions and persona
├── agentdetails.py         # Agent configuration
├── chat_agent.py           # Core chat functionality
├── distance.py             # Distance calculation tool
├── get_agent_messages.py   # Message handling
├── location.py             # Location services
├── new_letta_listagents.py # Agent management
└── weather_tool.py         # Weather information
```

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/Sethuram2003/llm-mem-toolkit.git
cd llm-mem-toolkit
```

2. Install Ollama and Llama 3.1
```bash
# Install Ollama (instructions vary by OS)
ollama pull llama2:3.1
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Start the Letta server
2. Configure system persona:
   - Edit `Letta_system_persona` for custom behavior
   - Adjust memory parameters as needed

3. Set up custom tools:
   - Configure API keys if required
   - Modify tool parameters in respective files

## 📖 Usage

1. Initialize the agent:
```python
from chat_agent import ChatAgent

agent = ChatAgent()
agent.initialize()
```

2. Start conversation:
```python
response = agent.chat("Hello! Can you help me with the weather?")
```

## 💬 Example Conversations

Here are some example interactions with the agent:

### Weather Query
```
User: What's the weather like in New York?
Agent: Let me check that for you using my weather tool.
[Accessing weather data...]
The current temperature in New York is 72°F (22°C) with partly cloudy skies.
Humidity is at 65% with a light breeze from the northeast.

User: Should I bring an umbrella?
Agent: Based on the forecast, there's a 30% chance of rain later today.
I'd recommend bringing an umbrella just to be safe.
```

### Location Services
```
User: Find me cafes near Central Park
Agent: Using my location services tool to search...
[Accessing location data...]
I found several cafes within 0.5 miles of Central Park:
1. Park Café (0.1 miles) - ⭐4.5
2. The Morning Cup (0.3 miles) - ⭐4.3
3. Lakeside Coffee (0.4 miles) - ⭐4.7
Would you like details about any of these?
```

### Memory Demonstration
```
User: Remember my favorite color is blue
Agent: I've stored that information in my memory.
[Memory updated: user_preferences.favorite_color = "blue"]

User: What's my favorite color?
Agent: Based on our previous conversation, your favorite color is blue.
```

## 🔧 Technical Details

### Components

- **chat_agent.py**
  - Core conversation handling
  - Memory management
  - Tool integration

- **Custom Tools**
  - Weather: Real-time weather data
  - Location: Geolocation services
  - Distance: Geographic calculations

### Memory System
```python
{
    "user_preferences": {},
    "conversation_history": [],
    "learned_patterns": {},
    "tool_states": {}
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚠️ Requirements

- Python 3.6+
- Letta Platform
- Ollama
- Llama 3.1 model
- Internet connection for tools

## 📄 License

This project is licensed under the included LICENSE file.

---
<div align="center">

Created by **Sethuram2003**

</div>
