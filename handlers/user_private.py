from aiogram import Router,types,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from filters.chat_types import ChatTypeFilter
from keyboard.reply import start_kb,another_keyboard,del_kbd
from aiogram.filters import or_f



user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(F.text == "Стартовое меню")
@user_private_router.message(CommandStart())
async def greeting(message: Message):
    await message.answer("Бот для помощи в обучении",reply_markup=another_keyboard.as_markup(resize_keyboard = True, input_field_placeholder = "anuka"))


# @user_private_router.message(F.text.in_(["готово"]))
# async def ready_for_work(message:Message):
#     await message.reply("простое сообщение")

@user_private_router.message(F.text == "Способы оплаты")
@user_private_router.message(Command("payment"))
async def choise(message: Message):
    await message.answer("Способы оплаты: ")



@user_private_router.message(or_f(Command("about"), (F.text =="О репетиторе"), (F.text =="О репетиторе2")))
async def telling_about(message:Message):
    await message.answer('О репетиторе: ', reply_markup=start_kb)
    await del_kbd
    
    
@user_private_router.message(F.text.len()>5)
async def test(message:Message):
    await message.answer("сработал тестовый хэндлер, длина сообщения больше 5")