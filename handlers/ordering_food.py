from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.reply_keyboard import main_kb
from keyboards.simple_keyboard import make_row_keyboard


class OrderFood(StatesGroup):
    food_name = State()
    food_size = State()



food_names = ["Суши", "Спагетти", "Хачапури"]
food_sizes = ["Маленькую", "Среднюю", "Большую"]

router = Router()


@router.message(StateFilter(None), F.text == "Еда")
@router.message(StateFilter(None), Command("food"))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите блюдо: ",
        reply_markup=make_row_keyboard(food_names)
    )
    await state.set_state(OrderFood.food_name)


@router.message(OrderFood.food_name, F.text.in_(food_names))
async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(food=message.text.lower())
    await message.answer(
        text="Блюдо выбрано, а что насчет размера? ",
        reply_markup=make_row_keyboard(food_sizes)
    )
    await state.set_state(OrderFood.food_size)


@router.message(OrderFood.food_size, F.text.in_(food_sizes))
async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(size=message.text.lower())

    order = await state.get_data()
    await message.answer(
        text=f"Вы выбрали {order['food']} порцию {order['size']} ",
        #reply_markup=ReplyKeyboardRemove()
        reply_markup=main_kb
    )
    await state.clear()