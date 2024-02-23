ССЫЛКА НА ТЕЛЕГРАММ БОТА : @csv_json_bot
К сожалению, не успела его захостить, поэтому надо будет вручную вставлять код в IDE

from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove,KeyboardButton
from aiogram import Bot, Dispatcher, types, executor
import logging


logging.basicConfig(level = logging.INFO)
bot = Bot(token= '7058282410:AAGMkIh2dt2Q5wyPsPIB5hRrXVr5fZR3msQ')
dp = Dispatcher(bot)

#Buttons
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.insert(KeyboardButton('/start')).insert(KeyboardButton('/description'))

kp = InlineKeyboardMarkup(row_width=True)
kp1 = InlineKeyboardButton(text='Код для конвертации в сsv📌', callback_data='to_convert')
kp2 = InlineKeyboardButton(text='Код для конвертации в json из csv📌', url = 'https://colab.research.google.com/drive/12j0nyV7n4fE0xcyq1aP4ufl6qzUDzPNs?usp=sharing#scrollTo=yQFhW_6uPKjt')
kp3 = InlineKeyboardButton(text='Сторонние ресурсы📌',url='https://csvjson.com/csv2json')
kp.insert(kp1)
kp.insert(kp2)
kp.insert(kp3)

NEW_TEXT = '''
/help - нажмите, чтобы начать работу
'''
NEW_TEXT2 ='''
Файл csv для пробной обработки находится вместе с почтовым сообщением.Вставьте его в гугл диск и она преобразует
в json код! '''

CODE_TO_CSV ='''
Скопируйте код ниже и воспользуйтесь ID, которая для вас удобнее всего и данный код конвертируется в csv.

import pandas as pd
data ={
     'Scool': ['Math' , 'Physics' , 'Information Technologies' , 'Russian language' , 'English language' , 'Biological', 'Physical Education'],
     'District':['Moskovsky','Frunzensky','Admiralteisky','Vasileostrovsky','Petrogradsky','Krasnoselsry','Kyrortny'],
     'Quality': ['Smart', 'Beautiful', 'Strange', 'Exciting','Wonderful','Auwful','Bad']
}

df = pd.DataFrame(data)
df.to_csv('new_csv', index = False)
'''

CODE_TO_JSON='''
#Данный код лучше всего реализывавается в google colab, потому что не требует стороннего подключения 
в библиотеки так как итак все встроено!
'''
async def on_startup(_):
    print('Ready!')
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = NEW_TEXT ,
                           reply_markup= kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = NEW_TEXT2 ,
                           reply_markup= kb)
@dp.message_handler(commands=['help'])
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id ,text='Добро пожаловать! Данный бот поможет вам конвертироать файл csv а json формат: ', reply_markup=kp)
    await message.delete()

@dp.callback_query_handler(text='to_convert')
async def cmd_convert(call:types.CallbackQuery):
    await bot.send_message(call.from_user.id,text=CODE_TO_CSV)

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply('Я не могу обработать данное сообщение!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)






