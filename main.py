from telebot import types
import telebot
token='6038737970:AAGbiidvvSQEktVMzjTmM-KziX1G4Xkp29A'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text = 'Yes')
    button2 = types.KeyboardButton(text = 'NO')
    keyboard.add(button1 , button2)
    bot.send_message(message.chat.id,'Hello, I can recomend you interesting movie, Would you like? ',  reply_markup=keyboard)


        
@bot.message_handler(commands=['movie'])
def movie_command (message):
    keyboard = types.ReplyKeyboardMarkup()
    but1 = types.KeyboardButton(text='Action',)
    but2 = types.KeyboardButton(text='Adventure')
    but3 = types.KeyboardButton(text='Comedy')
    but4 = types.KeyboardButton(text='Drama')
    but5 = types.KeyboardButton(text='Fantasy' )
    but6 = types.KeyboardButton(text='Thriller' )
    but7 = types.KeyboardButton(text='Documentary' )
    but8 = types.KeyboardButton(text='War' )
    keyboard.add(but1,but2,but3,but4,but5,but5,but6,but7,but8)
    bot.send_message(message.chat.id,'Choose the genre',  reply_markup=keyboard)

@bot.message_handler(commands=['serials'])
def serials_command (message):
    keyboard = types.InlineKeyboardMarkup()
    buts1 = types.InlineKeyboardButton(text="Click",url='https://kinobar.vip/17672-igra-prestolov-1-sezon-5-v7.html')
    keyboard.add(buts1)
    bot.send_photo(message.from_user.id,types.InputFile('600x900.webp'), caption='Game of Thrones', reply_markup=keyboard)
    bot.register_next_step_handler(message,serials_command)

@bot.message_handler(commands=['change'])
def change_command(message):
    msg = bot.send_message(message.chat.id, 'Enter something')
    bot.register_next_step_handler(msg, change_command2)

def change_command2(message):
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 1, text='You entered ' + message.text)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    if message.text == 'Yes':
        bot.send_message(message.chat.id, 'Cool\nEnter the command: /movie')
        bot.register_next_step_handler(message , start_command)
    elif message.text == 'NO':
        bot.send_message(message.chat.id, 'Okay in the next time:(\nBut I can recommend you the best serials of the world\n Enter the command: /serials')
        bot.register_next_step_handler(message , start_command)
    elif message.text == 'Action':
         bot.send_message(message.chat.id,'Police Story\nMad Max 2: The Road Warrior')
         bot.register_next_step_handler(message , movie_command)
    elif message.text == 'Adventure':
        bot.send_message(message.chat.id,'Life of Pi\nThe Lord of the Rings: The Fellowship of the Ring')
        bot.register_next_step_handler(message , movie_command)
    elif message.text == 'Comedy':
        bot.send_message(message.chat.id,'ACE VENTURA: PET DETECTIVE\nAirplane!')
        bot.register_next_step_handler(message , movie_command)
    elif message.text == 'Drama':
        bot.send_message(message.chat.id,'Opengeimer\nHunger!')
        bot.register_next_step_handler(message , movie_command)
    elif message.text == 'Fantasy':
        bot.send_message(message.chat.id,'Harry poter\nWitcher!')
        bot.register_next_step_handler(message , movie_command)
    elif message.text == 'Thriller':
        bot.send_message(message.chat.id,'Mr Harrigan\nBefore I Wake')
        bot.register_next_step_handler(message , movie_command)
    elif message.text == 'Documentary':
        bot.send_message(message.chat.id,'The Trial of Saddam Hussein\nNuclear Exodus')
        bot.register_next_step_handler(message , movie_command)
    elif message.text == 'War':
        bot.send_message(message.chat.id,'Braveheart\nGrave of the Fireflies')
        bot.register_next_step_handler(message , movie_command)
    
if __name__ == '__main__':
    bot.infinity_polling()