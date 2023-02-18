from aiogram import types
import asyncio
from datetime import datetime
from . app import bot
from . app import dp

DELAY = 3600

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello")

async def remind():
    cur_time = datetime.now().strftime("%H")
    time = '17'
    print(time, cur_time)
    if cur_time == time:
        print(cur_time, time)
        await bot.send_message(chat_id=924278497, text='Составь список продуктов')


def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)