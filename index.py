from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
token = os.getenv('TOKEN')
bot_username = os.getenv('BOT_USERNAME')
authorized_user_id = int(os.getenv('USER_ID'))  # Ensure it's an integer

# Set bot token and bot username
BOT_TOKEN: Final = token
BOT_USERNAME: Final = bot_username

# List of authorized user IDs
authorized_user_ids = [authorized_user_id]  # Replace with actual user IDs


# Function to check if the user is authorized
def is_user_authorized(update: Update) -> bool:
    return update.effective_user.id in authorized_user_ids


# Function to process user messages and generate a response
def generate_response(user_message: str) -> str:
    processed_message: str = user_message.lower()
    if 'hi' in processed_message:
        return 'Hello!'
    return 'I do not understand what you wrote...'


# Handler for incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if user is authorized
    if not is_user_authorized(update):
        await update.message.reply_text("You are not authorized to use this bot.")
        return

    chat_type: str = update.message.chat.type
    user_message: str = update.message.text

    print(f'User ({update.message.chat.id}) in {chat_type}: "{user_message}"')

    # Handle group chat messages
    if chat_type == 'group':
        # Bot responds only if mentioned in a group chat
        if BOT_USERNAME in user_message:
            # Remove bot username from the message
            message_without_bot: str = user_message.replace(BOT_USERNAME, '').strip()
            response: str = generate_response(message_without_bot)
        else:
            return  # If bot is not mentioned, do nothing
    else:
        # For private chats, process the message directly
        response: str = generate_response(user_message)

    print('Bot:', response)
    await update.message.reply_text(response)


# Error handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Command to get the user's ID
async def get_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"Your user ID is: {user_id}")


if __name__ == '__main__':
    print('Starting bot...')

    # Create the application with the bot token
    app = Application.builder().token(BOT_TOKEN).build()

    # Add command handler for /getid
    app.add_handler(CommandHandler('getid', get_user_id))

    # Add message handler for text messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Add error handler
    app.add_error_handler(error_handler)

    print('Polling...')
    app.run_polling(poll_interval=1)
