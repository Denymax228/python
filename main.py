import telebot
import sqlite3
bot=telebot.TeleBot('6054946429:AAHTOi0Zngy0NIATANaOMK17IcLdmZSu5z8')
conn=sqlite3.connect('D:/python projects/bot_ampty/test', check_same_thread=False)
cursor=conn.cursor()
def dbtable(user_id: int,user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test1 (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()
@bot.message_handler(commands=['start'])
def main (message):
    if message.from_user.last_name==None:
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}')
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        dbtable(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    else:
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name} {message.from_user.last_name}' )
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        dbtable(user_id=us_id, user_name=us_name, user_lastname=us_sname, username=username)
bot.polling(none_stop=True)

