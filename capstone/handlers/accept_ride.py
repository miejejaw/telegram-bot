from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router, types
from services.book_ride import accept_ride
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

accept_router = Router()

class AcceptForm(StatesGroup):
    booking_id = State()

@accept_router.message(Command("accept_ride"))
async def signup_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer("Please enter Booking ID:")
    await state.set_state(AcceptForm.booking_id)   

@accept_router.message(AcceptForm.booking_id)
async def process_phone(message: types.Message, state: FSMContext) -> None:
    await state.update_data(booking_id=message.text)
    user_data = await state.get_data()

    # Store user information in the database
    res = await accept_ride(user_data['booking_id'], message.from_user.id)

    await message.reply(res)
    await state.clear()

