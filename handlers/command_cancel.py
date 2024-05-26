from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from keyboards.reply_keyboard import main_kb

router = Router()


@router.message(StateFilter(None), Command("cancel"))
@router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({})
    await message.answer(
        text="Нечего отменять",
        #reply_markup=ReplyKeyboardRemove()
        reply_markup=main_kb
    )


@router.message(Command("cancel"))
@router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        #reply_markup=ReplyKeyboardRemove()
        reply_markup=main_kb
    )