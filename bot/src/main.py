from aiogram import executor
import asyncio
from bot_app import dp
from bot_app.commands import DELAY, repeat, remind


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.call_later(DELAY, repeat, remind, loop)
    executor.start_polling(dp, skip_updates=True)