import telebot
import webbrowser
from telebot import types
import sqlite3



# Создаем переменную, чтобы обратиться к классу
bot = telebot.TeleBot('6794592744:AAG6TIGgCiPUFvUutLwlvhr6_okubmaPTw8')
name = None

# База Данных
@bot.message_handler(commands=['startneww'])
def start(message):
    conn = sqlite3.connect('../database.sql')
    cursor = conn.cursor()

    #Таблица
    cursor.execute('CREATE TABLE IF NOT EXISTS USERS (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cursor.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name # глобальная переменная которая существует внутри файла
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите ваш пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('../database.sql')
    cursor = conn.cursor()

    # Таблица
    cursor.execute("INSERT INTO users (name, pass) VALUES (?, ?)", (name, password))  # использование параметризованного запроса
    conn.commit()
    cursor.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()  # Создание экземпляра класса
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('../database.sql') # подключение к файлу
    cursor = conn.cursor() # создаем курсор

    # Таблица
    cursor.execute('SELECT * FROM users ')
    users = cursor.fetchall() # вернет все записи

    #Перебираем сипсок users
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'



    cursor.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


#Меню в начале диалога
@bot.message_handler(commands=['startnew'])
def start(message):
    # Кнопки
    markup = types.ReplyKeyboardMarkup()
    bottom_1 = types.KeyboardButton('Перейти на сайт')
    markup.row(bottom_1)
    bottom_2 = types.KeyboardButton('Удалить фото')
    bottom_3 = types.KeyboardButton('Изменить текст')
    markup.row(bottom_2, bottom_3)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Молодец :)')




# Создаем декоратор:
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://kndc.kz/')


# Обработчик команды /start
@bot.message_handler(commands=['startt'])
def handle_start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я бот, который может помочь вам с чувством одиночества :)')
    bot.send_message(message.chat.id, 'Пожалуйста, укажите ваш пол: мужской / женский')

# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    if message.text.lower() == 'мужской':
        bot.send_message(message.chat.id, f'Привет, Мой дорогой друг! {message.from_user.first_name}')
        bot.send_message(message.chat.id, 'Как дела?')
    elif message.text.lower() == 'женский':
        bot.send_message(message.chat.id, f'Привет, Моя дорогая подруга! {message.from_user.first_name}')
        bot.send_message(message.chat.id, 'Как дела?')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, Мой дорогой друг! {message.from_user.first_name}')
    elif message.text.lower() == 'как дела у тебя ?':
        bot.send_message(message.chat.id, 'У меня все в порядке, спасибо за ваш интерес!')
    elif message.text.lower() == 'все плохо':
        bot.send_message(message.chat.id, 'Не печалься, давай сыграем в игру :)')


# Фото
@bot.message_handler(content_types=['photo'])
def ge_photo(message):
    #Кнопки
    markup = types.InlineKeyboardMarkup()
    bottom_1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.youtube.com/watch?v=sgdaK1CoXyw&list=RDsgdaK1CoXyw&start_radio=1&ab_channel=STARMUSIC')
    markup.row(bottom_1)
    bottom_2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    bottom_3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(bottom_2, bottom_3)
    bot.reply_to(message, 'Какая красивая фотография :)', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1) # - 1 последнее сообщение
    elif callback.data == 'edit':
        bot.edit_message_text('Почему бы и нет', callback.message.chat.id, callback.message.message_id)

# Кнопки




# Обработчик команды /help
# @bot.message_handler(commands=['help'])
# def handle_help(message):
#     bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='HTML')

# Запуск бота
bot.polling(non_stop=True)

