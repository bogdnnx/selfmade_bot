from string import punctuation
from aiogram import F,types,Router
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group','supergroup']))

restricted_words = {"кабан", 'хомяк'}


def clean_text(text:str):
    return text.translate(str.maketrans('','',punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def start_cmd(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"Пользователь {message.from_user.first_name} соблюдайте порядок")
        await message.delete()