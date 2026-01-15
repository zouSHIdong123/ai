# Moonshot AI Chatbot

A simple chatbot interface that uses the Moonshot AI API (Kimi model) for conversations.

## Features

- Interactive chat interface
- Conversation history tracking
- Ability to reset conversation
- Error handling

## Requirements

- Python 3.7+
- Moonshot API key

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Setup

1. Get your Moonshot API key from [Moonshot AI](https://www.moonshot.cn/)
2. Set the API key as an environment variable:

```bash
export MOONSHOT_API_KEY='your-api-key-here'
```

Or you can pass the API key directly to the constructor.

## Usage

Run the chatbot in interactive mode:

```bash
python chatbot.py
```

In the chat interface:
- Type your message and press Enter to send
- Type `quit`, `exit`, or `退出` to exit the program
- Type `reset` to clear the conversation history

## Example Code Usage

```python
from chatbot import MoonshotChatbot

# Initialize the chatbot
bot = MoonshotChatbot()

# Chat with the bot
response = bot.chat("Hello, how are you?")
print(response)

# Reset the conversation if needed
bot.reset_conversation()
```

## Notes

- The chatbot maintains conversation history for context
- Uses the `kimi-k2-turbo-preview` model by default
- Temperature is set to 0.6 for balanced creativity and coherence