from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Контакты")]
],
    resize_keyboard=True,
    input_field_placeholder="Выбери команду"
)