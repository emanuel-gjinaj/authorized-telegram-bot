# Authorized Telegram Bot

## Project Overview

This project is a **Telegram Bot** created using Python and the `python-telegram-bot` library. The bot is designed with **user authorization** in mind, ensuring that only specific users can interact with it. Additionally, it features **custom message handling** and responds to both group chat mentions and direct messages, demonstrating various aspects of Telegram bot development.

## Features

- **User Authorization**: Only authorized users (based on their Telegram ID) can interact with the bot.
- **Custom Response Handling**: The bot responds to certain messages (e.g., replies to "hi" with "Hello!") and can identify unknown inputs.
- **Group Chat Support**: The bot listens for its username in group chats and responds accordingly.
- **Private Chat Support**: In private messages, the bot directly processes and replies to the user's message.
- **Retrieve User ID**: Users can use the `/getid` command to retrieve their Telegram ID.
- **Error Handling**: The bot includes error management to handle exceptions gracefully.