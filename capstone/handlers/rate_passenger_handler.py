from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router, types
from services.rate_ride import rate
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

rate_passenger_router = Router()

class RateForm(StatesGroup):
    passenger_id = State()

@rate_passenger_router.message(Command("rate_passenger"))
async def signup_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer("Please enter passenger ID:")
    await state.set_state(RateForm.passenger_id)   

@rate_passenger_router.message(RateForm.passenger_id)
async def process_phone(message: types.Message, state: FSMContext) -> None:
    await state.update_data(passenger_id=message.text)
    user_data = await state.get_data()

    # Store user information in the database
    res = await rate(message.from_user.id, user_data['passenger_id'])

    await message.reply(res)
    await state.clear()

