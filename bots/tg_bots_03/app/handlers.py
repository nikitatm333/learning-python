from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from aiogram.enums import ChatAction


from app.keyboards import main_kb
from app.keyboards import main_inline_kb_callback

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await message.answer('Привет!',reply_markup=main_kb)

@user_router.message(Command("help"))
async def cmd_help(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await message.answer('Помоги!', reply_markup=main_inline_kb_callback)

@user_router.callback_query(F.data == "korzina")
async def cmd_by(callback: CallbackQuery):
    await callback.answer('Вы выбрали корзину.')
    # await callback.answer('Вы выбрали корзину.', show_alert=True)
    await callback.message.answer('Ваша корзина пуста.')

@user_router.message(F.photo)
async def get_photo(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await message.answer(f'ID фотографии: {message.photo[-1].file_id}')

@user_router.message()
async def echo(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                     action=ChatAction.TYPING)
    await message.answer(message.text)



