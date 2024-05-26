import logging
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import command_start, ordering_food, ordering_drink, command_cancel


async def main():
    bot = Bot(token="7092282501:AAFKLxRszbTAgyXhfyvZy6Ls2EOZkZ2Pza8")
    dp = Dispatcher(storage=MemoryStorage())
    logging.basicConfig(level=logging.INFO)

    dp.include_router(command_start.router)
    dp.include_router(ordering_food.router)
    dp.include_router(ordering_drink.router)
    dp.include_router(command_cancel.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())