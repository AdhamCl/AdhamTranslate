# Discord Translation Bot

## Description
This Discord bot translates messages in different languages based on user reactions. It utilizes the Google Translate API to perform translations.

## Features
- Translates messages in real-time based on reactions
- Supports a variety of languages using emoji reactions

## Setup
1. Install required Python packages:
    ```bash
    pip install discord googletrans
    ```

2. Create a Discord bot and obtain its token. You can follow the official Discord Developer documentation for guidance.

3. Create a `.env` file in the root directory of the project and add the following:
    ```
    TOKEN=your_discord_bot_token_here
    ```

## Usage
1. Run the bot using the following command:
    ```bash
    python main.py
    ```

2. Add reactions to the messages you want to translate using the supported emoji languages.

## Supported Languages
The bot supports translation to and from the following languages:
- Hindi (🇮🇳)
- Spanish (🇦🇷, 🇪🇸)
- English (🇦🇺, 🇨🇦, 🇬🇧, 🇺🇸)
- Bengali (🇧🇩)
- Portuguese (🇧🇷, 🇵🇹)
- Chinese (🇨🇳)
- Czech (🇨🇿)
- Croatian (
