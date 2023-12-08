from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router, types
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

auth_router = Router()

class AuthForm(StatesGroup):
    login_phone = State()

@auth_router.message(Command("login"))
async def login_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(AuthForm.login_phone)
    await message.reply("Please enter your phone number:")


