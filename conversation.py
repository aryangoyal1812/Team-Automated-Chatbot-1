# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 02:46:10 2021

@author: USER
"""
from test_intro import chatbot_response
from test_college import chatbot_response_college
from test_programming import chatbot_response_programming
from programming import TopResult
from Bonus import getWeather,getTime
import logging
from typing import Dict

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [
    ['Basic Interaction'],
    ['General Queries'],
    ['Programming doubts'],
    ['Weather','Time'],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def facts_to_str(user_data: Dict[str, str]) -> str:
    facts = list()

    for key, value in user_data.items():
        facts.append(f'{key} - {value}')

    return "\n".join(facts).join(['\n', '\n'])


def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Hi! My name is KamandListener. I am here to help you with your queries regarding IIT Mandi. "
        "I support following Commands(case sensitive):\n->Basic Interaction\n->General Queries\n->Programming doubts\n->Weather\n->Time",
        reply_markup=markup,
    )

    return CHOOSING


def regular_choice(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    context.user_data['choice'] = text
    if(text=="Basic Interaction"):
        update.message.reply_text("Let's have some chit-chat about myself")
    elif(text=="General Queries"):
        update.message.reply_text("Ask your General Query about college? I hope I will be able to answer them")
    elif(text=="Programming doubts"):
        update.message.reply_text("Here to help with programming issues")

    return TYPING_REPLY


def custom_choice(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'The supported functions are: \n->Basic Interaction\n->General Queries\n->Programming doubts\n->Weather\n->Time', reply_markup=markup,)

    return CHOOSING


def received_information(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    text = update.message.text
    category = user_data['choice']
    user_data[category] = text
    
    if(category=="Basic Interaction"):
        update.message.reply_text(
        chatbot_response(text),
        reply_markup=markup,)
    elif(category=="General Queries"):
        update.message.reply_text(
        chatbot_response_college(text),
        reply_markup=markup,)
    elif(category=="Programming doubts"):
        update.message.reply_text(
        chatbot_response_programming(text),
        reply_markup=markup,)
    del user_data['choice']
    
    return CHOOSING


def done(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']
    text = update.message.text
    if(text =="Weather"):
        update.message.reply_text(getWeather(),reply_markup=markup,)
    elif(text=="Time"):
        update.message.reply_text(getTime(),reply_markup=markup,)

    user_data.clear()
#    return ConversationHandler.END
    return CHOOSING

def main() -> None:
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1569656905:AAGp3i1-cp5qXnisNmnYOw76B4FjyFN-qDo", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(Basic Interaction|General Queries|Programming doubts)$'), regular_choice
                ),
                MessageHandler(Filters.text & ~(Filters.regex('^(Basic Interaction|General Queries|Programming doubts)$') | Filters.regex('^(Weather|Time)$')) , custom_choice),
            ],
            TYPING_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^(Weather|Time)$')), regular_choice
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^(Weather|Time)$')),
                    received_information,
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^(Weather|Time)$'), done)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()