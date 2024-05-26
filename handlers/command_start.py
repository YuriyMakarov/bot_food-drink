from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.reply_keyboard import main_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Выберите, что хотите заказать: "
             "блюда (/food) или напитки (/drink).",
        reply_markup=main_kb
    )

