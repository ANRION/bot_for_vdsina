import logging
import os
import telebot
from telebot import types

from excel.RW_Excel import Read_Excel
from source.config import TOKEN
from source.log import log
from source.variables import *



def initial_bot(use_logging=True, level_name='DEBUG'):
    bot = telebot.TeleBot(TOKEN)
    #bot = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
    logger = log('bot', 'bot.log', 'INFO')

    
    

    @bot.message_handler(commands=['start'])
    def start_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, start_mess)
        logger.info(f"It's start handler. Message from {message.from_user.id}")

    @bot.message_handler(commands=['help'])
    def help_handler(message: telebot.types.Message):
        bot.send_message(message.from_user.id, help_mess)
        logger.info(f"It's start handler. Message from {message.from_user.id}")


    @bot.message_handler(commands=['task'])
    def help_handler(message: telebot.types.Message):

       # a = os.getcwd()
       task =  Read_Excel(".\\excel\\task_c_level.xlsm", "t_task")

       if str(message.from_user.username) == "AndreySavinov":
            s = {}
            for KEY in task.keys():
                if task[KEY][1] == "Банк" and task[KEY][2] == "Проектная" and task[KEY][3] == "Васильев":
                    s.update({KEY: task[KEY]})
                    bot.send_message(message.from_user.id, task[KEY][4])
                    logger.info(f"Запросил задачу {message.from_user.id}")

    @bot.message_handler(content_types=['text'])
    def text_handler(message: telebot.types.Message):
        mmes = message.from_user
        if message.text == "Готово":
            bot.send_message(message.from_user.id, " Молодец " + str(message.from_user.first_name)+" ! "+message.from_user.username)

        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
        callback_button2 = types.InlineKeyboardButton(text="Не нажимай меня", callback_data="notest")
        keyboard.add(callback_button)
        keyboard.add(callback_button2)
        bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)




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
