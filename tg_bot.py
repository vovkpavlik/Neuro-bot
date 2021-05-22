import os
from functools import partial

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater

from detect_intents import detect_intents


def message_handler(project_id, update: Update, context: CallbackContext):
    users_message = update.effective_message.text
    chat_id = update.message.chat_id       
    response = detect_intents(project_id, chat_id, users_message, language_code="ru-ru")
    context.bot.send_message(chat_id, text=response.fulfillment_text)


def main():

    load_dotenv()

    tg_token = os.getenv("TG_TOKEN")
    project_id = os.getenv("GOOGLE_PROJECT_ID")

    updater = Updater(token=tg_token)
    dp = updater.dispatcher
        
    partial_message_handler = partial(message_handler, project_id)
    dp.add_handler(MessageHandler(Filters.text, partial_message_handler))
    
    updater.start_polling()


if __name__ == "__main__":
    main()
