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

rate_driver_router = Router()

class RateForm(StatesGroup):
    driver_id = State()

@rate_driver_router.message(Command("rate_driver"))
async def signup_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer("Please enter driver ID:")
    await state.set_state(RateForm.driver_id)   

@rate_driver_router.message(RateForm.driver_id)
async def process_phone(message: types.Message, state: FSMContext) -> None:
    await state.update_data(driver_id=message.text)
    user_data = await state.get_data()

    # Store user information in the database
    res = await rate(message.from_user.id, user_data['driver_id'])

    await message.reply(res)
    await state.clear()

