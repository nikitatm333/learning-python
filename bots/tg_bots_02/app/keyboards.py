from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Контакты")]
],
    resize_keyboard=True,
    input_field_placeholder="Выбери команду"
)

main_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Корзина", url="https://stackoverflow.com/")],
    [InlineKeyboardButton(text="Контакты", url="https://stackoverflow.com/")]
])