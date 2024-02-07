import asyncio
from aiogram import Bot, Dispatcher
from handlers import message_handlers, command_handlers, callback_handlers
from config import TOKEN

import datetime
import sched
import time

async def main():
    print("""
⠀⠀⠀⠀⡠⠤⡀⠀⠀⢀⡴⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠁⠀⢳⢲⠖⡞⠀⠀⢳⡤⠤⢤⣶⡤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠤⢤⣀⠆⠀⡶⠀⢀⠀⠀⡶⠀⢀⣀⣀⡈⠿⠁⠻⠏⠉⠓⣄⠀⠀⠀⠀⠀⠀
⠰⠖⠒⡾⠀⠀⠀⠈⠉⠁⠀⠀⠀⠭⠭⢤⡄⠀⠀⠀⠀⠀⠀⠀⢣⠀⣠⡄⣀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠛⢣⣬⡄
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣳⠐⣾⣠⠃
⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠉⠉⠀⠀
⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠌⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⡄⡠⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⣴⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠀⠀⠀⠑⠔⠁⠉⠉⠉⠉⠹⠤⠏⠀⠈⠒⠃⠀
    """)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(command_handlers.router, callback_handlers.router, message_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
