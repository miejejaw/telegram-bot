from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router, types
from services.book_ride import cancel_ride
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

cancel_router = Router()

@cancel_router.message(Command("cancel_ride"))
async def signup_handler(message: types.Message, state: FSMContext) -> None:
    res = await cancel_ride(message.from_user.id)
    await message.reply(res)


