from aiogram import Bot, Dispatcher, F, types
import asyncio
import logging
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, BotCommandScopeAllPrivateChats
from dotenv import find_dotenv, load_dotenv
import os
from handlers import user_private,user_group
from common.bot_commads_list import private
load_dotenv(find_dotenv())

bot  = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

ALOLOWED_UPDATES = ["message, edited_message"]
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 


dp.include_routers(user_private.user_private_router, user_group.user_group_router)




    
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope =BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALOLOWED_UPDATES)
    
    
    
asyncio.run(main())

