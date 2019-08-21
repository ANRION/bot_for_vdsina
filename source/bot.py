import logging

import telebot
from telebot import types

from source.config import TOKEN
from source.log import log
from source.variables import *



def initial_bot(use_logging=True, level_name='DEBUG'):
    bot = telebot.TeleBot(TOKEN)
    #bot = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
    logger = log('bot', 'bot.log', 'INFO')
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('Готово', 'Не Готово')
    
    

    @bot.message_handler(commands=['start'])
    def start_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, start_mess)
        logger.info(f"It's start handler. Message from {message.from_user.id}")

    @bot.message_handler(commands=['help'])
    def help_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, help_mess)
        logger.info(f"It's start handler. Message from {message.from_user.id}")

    @bot.message_handler(content_types=['text'])
    def text_handler(message: telebot.types.Message):
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
        callback_button = types.InlineKeyboardButton(text="Не нажимай меня", callback_data="notest")
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)
             
       # bot.send_message(message.chat.id, 'Твоя задача готова?',reply_markup=keyboard1)
        logger.info(f"It's text handler. Message from {message.from_user.id}")
        
    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        # Если сообщение из чата с ботом
        if call.message:
            if call.data == "test":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
            if call.data == "notest":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="БАХ!!!")
    
    
    
    
    
    if use_logging:
        telebot.logger.setLevel(logging.getLevelName(level_name))

    return bot
