# PaLM Telegram Bot

This repository contains the source code for a simple Telegram bot that uses the PaLM API to generate text based on user-provided prompts. The bot is built using the [aiogram ↗](https://docs.aiogram.dev/en/latest/dispatcher.html) library for asynchronous handling of the Telegram bot API.

## Features

- Accepts text prompts and generates text using the PaLM API.
- Provides generated text as a response in Telegram.
- Supports the `/start` command for welcoming users and the `/bard` command for generating text.

## Requirements

- Python 3.6 or higher
- `aiogram` library
- `google.generativeai` library
- PaLM API access: Obtain an API key from [Google's GenerativeAI Developer Portal ↗](https://developers.generativeai.google/)

## Installation

1. Clone the repository:

   `````
   git clone https://github.com/yourusername/palm-telegram-bot.git
   ```

2. Change the current directory:

   ````
   cd palm-telegram-bot
   ````

3. Install the required Python packages:

   ````
   pip install aiogram google-generativeai
   ````

4. Replace the `API_KEY` and `TG_BOT_TOKEN` placeholders in the `bot.py` script with your PaLM API key and Telegram bot token, respectively.

5. Run the `bot.py` script:

   ````
   python bot.py
   ````

## Usage

1. Start a conversation with your bot on Telegram.
2. Send the `/start` command to receive a welcome message.
3. Send the `/bard` command followed by a text prompt, e.g., `/bard Once upon a time`.
4. The bot will generate text based on the prompt and send it back as a message.
