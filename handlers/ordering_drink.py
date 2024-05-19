from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.reply_keyboard import main_kb
from keyboards.simple_keyboard import make_row_keyboard


class OrderDrink(StatesGroup):
    drink_name = State()
    drink_size = State()


drink_names = ["Кола", "Фанта", "Спрайт"]
drink_sizes = ["0.3", "0.5", "0.7"]

router = Router()


@router.message(StateFilter(None), F.text == "Напитки")
@router.message(StateFilter(None), Command("drink"))
async def cmd_drink(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите напиток: ",
        reply_markup=make_row_keyboard(drink_names)
    )
    await state.set_state(OrderDrink.drink_name)


@router.message(OrderDrink.drink_name, F.text.in_(drink_names))
async def drink_chosen(message: Message, state: FSMContext):
    await state.update_data(food=message.text.lower())
    await message.answer(
        text="Напиток выбран, а что насчет объема? ",
        reply_markup=make_row_keyboard(drink_sizes)
    )
    await state.set_state(OrderDrink.drink_size)


@router.message(OrderDrink.drink_size, F.text.in_(drink_sizes))
async def drink_chosen(message: Message, state: FSMContext):
    await state.update_data(size=message.text.lower())

    order = await state.get_data()
    await message.answer(
        text=f"Вы выбрали {order['drink']} объем {order['size']} литра",
        #reply_markup=ReplyKeyboardRemove()
        reply_markup=main_kb
    )
    await state.clear()
