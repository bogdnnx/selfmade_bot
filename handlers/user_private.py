from aiogram import Router,types,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from filters.chat_types import ChatTypeFilter



user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def greeting(message: Message):
    await message.answer("Бот для помощи в обучении")


@user_private_router.message(F.text.in_(["готово"]))
async def ready_for_work(message:Message):
    await message.reply("простое сообщение")


@user_private_router.message(Command("menu"))
@user_private_router.message(F.text.contains('меню'))

async def choise(message: Message):
    await message.answer('what do you want??')
    
    
@user_private_router.message(Command("about"))
async def telling_about(message:Message):
    await message.answer("Это бот репетитора Камилы Хакимовой")
    
    
@user_private_router.message(F.text.len()>5 | F.text.lower().contains("обезь "))
async def test(message:Message):
    await message.answer("сработал тестовый хэндлер")