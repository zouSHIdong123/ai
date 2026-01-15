# Moonshot AI Chatbot with Web Interface

A simple chatbot interface that uses the Moonshot AI API (Kimi model) for conversations, featuring both console and web interfaces.

## Features

- Interactive chat interface
- Conversation history tracking
- Web-based interface using Streamlit
- Ability to reset conversation
- Error handling
- Configurable parameters via web UI

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

### Console Interface

Run the chatbot in interactive mode:

```bash
python chatbot.py
```

In the chat interface:
- Type your message and press Enter to send
- Type `quit`, `exit`, or `退出` to exit the program
- Type `reset` to clear the conversation history

### Web Interface

Run the Streamlit web application:

```bash
streamlit run app.py
```

Or use the provided script:

```bash
./run_app.sh
```

Then open your browser and go to the URL displayed in the terminal (usually http://localhost:8501).

In the web interface:
- Enter your API key in the sidebar
- Select your preferred model and temperature settings
- Type your message in the chat input box
- Click the "Clear Chat" button to reset the conversation