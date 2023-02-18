from aiogram import Bot, Dispatcher
from . local_settings import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


