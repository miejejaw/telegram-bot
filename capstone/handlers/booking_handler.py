from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router, types
from services.book_ride import booking_ride
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

booking_router = Router()

class BookingForm(StatesGroup):
    current_location = State()
    destination = State()

@booking_router.message(Command("book_ride"))
async def signup_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer("Please enter your current location:")
    await state.set_state(BookingForm.current_location)

@booking_router.message(BookingForm.current_location)
async def process_name(message: Message, state: FSMContext) -> None:   
    await state.update_data(current_location=message.text)
    await message.reply(f"Please enter your destination:")
    await state.set_state(BookingForm.destination)
    

@booking_router.message(BookingForm.destination)
async def process_phone(message: types.Message, state: FSMContext) -> None:
    await state.update_data(destination=message.text)
    user_data = await state.get_data()

    # Store user information in the database
    booking_id = await booking_ride(message.from_user.id, user_data['current_location'], user_data['destination'])

    await message.reply(f"successfully booked {booking_id}")
    await state.clear()
   
   
   
   
   
   
   
   
