from codecs import make_encoding_map
from imghdr import tests

from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from aiogram.enums import ChatAction

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.keyboards import main_kb
from app.keyboards import main_inline_kb_callback

class Reg(StatesGroup):
    name = State()
    agreement = State()
    number = State()

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message, state : FSMContext):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await state.set_state(Reg.name)
    await message.answer('Привет! Введи свое имя')

@user_router.message(Reg.name)
async def reg_name(message: Message, state : FSMContext):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await state.update_data(name=message.text)
    await state.set_state(Reg.agreement)
    await message.answer('Согласен ли ты мне отправить свой номер?')

@user_router.message(Reg.agreement)
async def reg_agreement(message: Message, state : FSMContext):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await state.update_data(agreement=message.text) #Либо да либо нет
    print(Reg.agreement)
    if message.text == "Да":
        await state.set_state(Reg.number)
        await message.answer('Введи свой номер')
    else:
        await message.answer(text="Все, Спасибо")
        await state.clear()

@user_router.message(Reg.number)
async def reg_number(message: Message, state : FSMContext):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await state.update_data(number=message.text) #Либо да либо нет
    data = await state.get_data()
    await message.answer(f"{data['name'], data['agreement'], data['number']}")
    await state.clear()



@user_router.message(Command("help"))
async def cmd_help(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await message.answer('Помоги!', reply_markup=main_inline_kb_callback)

@user_router.callback_query(F.data == "korzina")
async def cmd_by(callback: CallbackQuery):
    await callback.answer('Вы выбрали корзину.')
    # await callback.answer('Вы выбрали корзину.', show_alert=True)
    # await callback.message.answer('Ваша корзина пуста.')

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



