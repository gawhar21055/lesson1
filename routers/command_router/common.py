from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from keyboards import get_request_keyboard
from aiogram.fsm.state import StatesGroup, State

router = Router()


class Form(StatesGroup):
    name = State()
    surname = State()


@router.message(Command("state", prefix="/!"))
async def handle_state(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        text="Hi there! Whats your name?",
    )


@router.message(Form.name)
async def handle_form_name(message: types.Message, state: FSMContext):
    await state.set_state(Form.surname)
    await message.answer(
        text=f"Hi {message.text}. Enter ur surname, please.",
    )


@router.message(Form.surname)
async def handle_form_surname(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    data = await state.get_data()
    await message.answer(text=f"You name is {data["name"]} and ur surname is {data["surname"]}")
    await state.clear()


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text="Hi! I am test bot!")


@router.message(Command("help", prefix="/!"))
async def handle_help(message: types.Message):
    await message.answer(
        text="Help message",
        reply_markup=get_request_keyboard(),
    )


# @router.message(Command("info"))
# async def handle_info(message: types.Message):
#     await message.answer(
#         text="Info message",
#         reply_markup=get_info_keyboard(),
#     )
