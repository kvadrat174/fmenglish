#!/usr/bin/env python

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import os
import random
import datetime
import time
import configfm as cfg

from operations import *



bot = telebot.TeleBot('1029346409:AAHA8gU9En2RUUe0yAFpWUltG43dt6FWJ5E')

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
bt1 = telebot.types.KeyboardButton('Отметить посещение')
bt2 = telebot.types.KeyboardButton('Добавить оплату')
bt3 = telebot.types.KeyboardButton('Посмотреть баланс')
bt4 = telebot.types.KeyboardButton('Добавить ученика')
keyboard1.add(bt1, bt4)

keyboard9 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
bt11 = telebot.types.KeyboardButton('Да')
bt22 = telebot.types.KeyboardButton('Нет')
keyboard9.add(bt11,bt22)




@bot.message_handler(commands=['start'])
def start_message(message):
    nm = message.from_user.first_name


    id1 = message.from_user.id

    if UserList(id1,nm) == True:
        bot.send_message(message.chat.id, 'Здравствуйте, ' +str(nm)+ ' , что бы вы хотели сделать?', reply_markup=keyboard1);
    elif UserList(id1,nm) == False:
        bot.send_message(message.from_user.id, 'Вы добавлены', reply_markup=keyboard1)
    else:
        bot.send_message(message.from_user.id, 'Вы добавлены', reply_markup=keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):


    if message.text.lower() == 'добавить ученика':
        global id1
        id1 = message.from_user.id
        choose_group(message)

    elif message.text.lower() == 'отметить посещение':

        id1 = message.from_user.id
        mark_lesson(message)
    elif message.text.lower() == 'да':
        global gr
        gr = uchenik.vizit(res1)

        get_list(message)

    elif message.text.lower() == 'нет':

        gr = uchenik.nvizit(res1)
        get_list(message)







    elif message.text.lower() == 'посмотреть результаты':
        bot.send_message(message.from_user.id, 'В разработке))', reply_markup=keyboard1);







@bot.message_handler(content_types=['text'])
def choose_group(message):
    idi = message.from_user.id
    keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bt1 = telebot.types.KeyboardButton('пн-ср 10.00 4кл')
    bt2 = telebot.types.KeyboardButton('пн-ср 17.00 4кл')
    bt3 = telebot.types.KeyboardButton('пн-пт 18.00-17.00')
    bt4 = telebot.types.KeyboardButton('вт-чт 10.00 2-3 кл')
    bt5 = telebot.types.KeyboardButton('вт-чт 17.20 малыши')
    bt6 = telebot.types.KeyboardButton('вт-чт 11.30 взрослые')
    bt7 = telebot.types.KeyboardButton('вт-чт 18.40 3 класс')
    bt8 = telebot.types.KeyboardButton('вт-сб 19.30-14.30 6-7кл')
    bt9 = telebot.types.KeyboardButton('ср-пт 18-00 1кл')
    bt10 = telebot.types.KeyboardButton('вт-чт 18-30 1 класс')
    bt11 = telebot.types.KeyboardButton('Индивидуальные занятия')
    if id1 == cfg.anastasia_id:

        keyboard2.add(bt5, bt10)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup = keyboard2);
        bot.register_next_step_handler(message, get_group);

    elif id1 == cfg.olga_id:
        keyboard2.add(bt7, bt8)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=keyboard2);
        bot.register_next_step_handler(message, get_group);

    elif id1 == cfg.sofia_id:
        keyboard2.add(bt1, bt4, bt6, bt11)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=keyboard2);
        bot.register_next_step_handler(message, get_group);

    elif id1 == cfg.evgenya_id:
        keyboard2.add(bt2, bt3, bt9)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=keyboard2);
        bot.register_next_step_handler(message, get_group);

    else:

        keyboard2.add(bt1,bt2,bt3,bt4,bt5,bt6,bt7, bt8, bt9,bt10,bt11)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=keyboard2);
        bot.register_next_step_handler(message, get_group);



   


def get_group(message): #получаем фамилию
    global group;
    group = message.text;
    markup = telebot.types.ReplyKeyboardRemove(selective=False)

    bot.send_message(message.chat.id, 'Введите имя', reply_markup = markup);

    bot.register_next_step_handler(message, get_name);

def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.chat.id,'Введите фамилию');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Да', callback_data='yes_st'),
                 telebot.types.InlineKeyboardButton('Исправить', callback_data='no_st'))

    bot.send_message(message.chat.id,'Добавить '+str(name)+' '+str(surname)+' в группу '+str(group)+'? ',reply_markup = keyboard);

# ОТМЕЧАЕМ ПОСЕЩЕНИЕ ______________________________________________________
def mark_lesson(message):
    idi = message.from_user.id
    keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bt1 = telebot.types.KeyboardButton('пн-ср 10.00 4кл')
    bt2 = telebot.types.KeyboardButton('пн-ср 17.00 4кл')
    bt3 = telebot.types.KeyboardButton('пн-пт 18.00-17.00')
    bt4 = telebot.types.KeyboardButton('вт-чт 10.00 2-3 кл')
    bt5 = telebot.types.KeyboardButton('вт-чт 17.20 малыши')
    bt6 = telebot.types.KeyboardButton('вт-чт 11.30 взрослые')
    bt7 = telebot.types.KeyboardButton('вт-чт 18.40 3 класс')
    bt8 = telebot.types.KeyboardButton('вт-сб 19.30-14.30 6-7кл')
    bt9 = telebot.types.KeyboardButton('ср-пт 18-00 1кл')
    bt10 = telebot.types.KeyboardButton('вт-чт 18-30 1 класс')
    bt11 = telebot.types.KeyboardButton('Индивидуальные занятия')
    if id1 == cfg.anastasia_id:

        keyboard3.add(bt5, bt10)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=keyboard3);
        bot.register_next_step_handler(message, get_list);

    elif id1 == cfg.olga_id:
        keyboard3.add(bt7, bt8)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=keyboard3);
        bot.register_next_step_handler(message, get_list);

    elif id1 == cfg.evgenya_id:
        keyboard3.add(bt2, bt3, bt9)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=keyboard3);
        bot.register_next_step_handler(message, get_list);

    elif id1 == cfg.sofia_id:
        keyboard3.add(bt1, bt4, bt6, bt11)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=keyboard3);
        bot.register_next_step_handler(message, get_list);

    else:

        keyboard3.add(bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, bt10, bt11)
        bot.send_message(message.chat.id, "Выберите группу", reply_markup=keyboard3);
        bot.register_next_step_handler(message, get_list);


def get_list(message):  # получаем фамилию

    group = message.text


    global res
    res = uchenik.get_stlist(group)
    if res == None:
        res = uchenik.get_stlist(gr)
    print(res)
    try:
        res2 = res[0]
        print(res2)
        global res1
        res1 = res[1]


        #markup = telebot.types.ReplyKeyboardRemove(selective=False)

        #bot.send_message(message.chat.id, 'Отметьте по очереди присутствующих', reply_markup=markup);
        bot.send_message(message.chat.id, res2, reply_markup=keyboard9);






    except TypeError:
        bot.send_message(message.from_user.id,
                     'Вы отметили всех в этой группе \n Если кого то нехватает то необходимо добавить.',
                     reply_markup=keyboard1);






def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"), InlineKeyboardButton("No", callback_data="cb_no"))
    return markup




# Проверка колбэк условий
@bot.callback_query_handler(func=lambda call: True)
def callback_key(message):
    if message.data == 'yes_st':
        save_std(name, surname, group)
        bot.send_message(message.from_user.id, 'данные сохранены', reply_markup= keyboard1)

    elif message.data == 'no_st':
        bot.send_message(message.from_user.id, 'Давайте начнем с начала', reply_markup= keyboard1)

    """elif message.data == "cb_yes":
        bot.answer_callback_query(message.id, "Answer is Yes")
        uchenik.vizit(res1)
        bot.send_message(message.from_user.id, 'Посещение отмечено')
        try:
            get_list(message)
        except AttributeError:
            get_list()

    elif message.data == "cb_no":
        bot.answer_callback_query(message.id, "Answer is No")
        uchenik.nvizit(res1)
        get_list(message)"""




bot.polling(none_stop=True, interval=0)