from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стартовое меню"),
            KeyboardButton(text="Способы оплаты"),
            
        ],
        [
            KeyboardButton(text="О репетиторе")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="anuka",
    
)
del_kbd = ReplyKeyboardRemove()


another_keyboard = ReplyKeyboardBuilder()
another_keyboard.add(
    KeyboardButton(text="Стартовое меню2"),
    KeyboardButton(text="Способы оплаты2"),
    KeyboardButton(text="О репетиторе2")
)
another_keyboard.adjust(2,1)
