from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router, types
from database.user_db import insert_user
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

register_router = Router()

class RegisterForm(StatesGroup):
    name = State()
    phone = State()
    role = State()
    
@register_router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Hi! Welcome to our chat bot.")
    await message.answer(
        '''
        You can control me by sending these commands:
        /signup - to create new account
        /login - to get services
        /delete_account - to delete your account

        Edit Account
        /edit_name - to change your name
        /edit_phone - to change your phone number
        /edit_role - to change your role
        
        booking
        /book_ride - to book ride
        /cancel_ride
        /accept_ride
        
        rating
        /rate_passenger
        /rate_driver
        
        /view_history
        '''
    )

@register_router.message(Command("signup"))
async def signup_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(RegisterForm.name)
    await message.answer("Please enter your full name:")

@register_router.message(RegisterForm.name)
async def process_name(message: Message, state: FSMContext) -> None:   
    await state.update_data(name=message.text)
    await message.reply(f"Nice to meet you, <b>{message.text}</b>! Please enter your phone number:")
    await state.set_state(RegisterForm.phone)
    

@register_router.message(RegisterForm.phone)
async def process_phone(message: types.Message, state: FSMContext) -> None:
    await state.update_data(phone=message.text)
    await state.set_state(RegisterForm.role)
    await message.answer(f"Please select your role <b>Driver</b> or <b>Passenger</b>",)


@register_router.message(RegisterForm.role)
async def process_role(message: types.Message, state: FSMContext) -> None:
    selected_role = message.text.casefold()

    if selected_role not in ("driver", "passenger"):
        await message.reply("Invalid role. Please select <b>Driver</b> or <b>Passenger</b>.")
        return

    await state.update_data(role=selected_role)
    user_data = await state.get_data()

    # Store user information in the database
    insert_user(message.from_user.id, user_data['name'], user_data['phone'], user_data['role'])

    await message.reply(f"<b>{message.from_user}</b> Your account has been successfully created. Please use /login to sign in.")
    await state.clear()
   
   
   
   
   
   
   
   
    

