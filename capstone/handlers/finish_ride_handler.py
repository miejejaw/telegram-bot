from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router, types
from services.book_ride import finish_ride
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

finish_ride_router = Router()

@finish_ride_router.message(Command("finish_ride"))
async def signup_handler(message: types.Message, state: FSMContext) -> None:
    res = await finish_ride(message.from_user.id)
    await message.reply(res)


