from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, Router, types
from database.user_db import update_user
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)


user_router = Router()

class UpdateForm(StatesGroup):
    name = State()
    phone = State()
    role = State()


@user_router.message(Command("update_name"))
async def update_name_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(UpdateForm.name)
    await message.answer("Please enter your new full name:")

@user_router.message(UpdateForm.name)
async def process_name_update(message: Message, state: FSMContext) -> None:
    new_name = message.text
    await state.update_data(name=new_name)
    await message.reply(f"Your name has been updated to: {new_name}")
    update_user(message.from_user.id, "name", new_name)
    await state.clear()



@user_router.message(Command("update_phone"))
async def update_phone_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(UpdateForm.phone)
    await message.answer("Please enter your new phone number:")

@user_router.message(UpdateForm.phone)
async def process_phone_update(message: Message, state: FSMContext) -> None:
    new_phone = message.text
    await state.update_data(phone=new_phone)
    await message.reply(f"Your phone number has been updated to: {new_phone}")
    update_user(message.from_user.id, "phone", new_phone)
    await state.clear()


@user_router.message(Command("update_role"))
async def update_role_handler(message: types.Message, state: FSMContext) -> None:
    await state.set_state(UpdateForm.role)
    await message.answer(f"Please select your new role: Driver or Passenger",)

@user_router.message(UpdateForm.role)
async def process_role_update(message: Message, state: FSMContext) -> None:
    new_role = message.text.casefold()

    if new_role not in ("driver", "passenger"):
        await message.reply("Invalid role. Please select 'Driver' or 'Passenger'.")
        return

    await state.update_data(role=new_role)
    await message.reply(f"Your role has been updated to: {new_role}")
    update_user(message.from_user.id, "role", new_role)
    await state.clear()
