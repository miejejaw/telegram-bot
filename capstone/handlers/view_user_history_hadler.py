from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router, types
from services.book_ride import get_user_history
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

view_user_history_router = Router()

@view_user_history_router.message(Command("view_history"))
async def signup_handler(message: types.Message) -> None:
    res = get_user_history(message.from_user.id)
    await message.reply(res)