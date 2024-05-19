import logging
import asyncio
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import command_start_and_cancel, ordering_food, ordering_drink


async def main():
    bot = Bot(token="7101861490:AAED8DmT5NWqxsodKedIHvEEe4z3QFKqHD0")
    dp = Dispatcher(storage=MemoryStorage())
    logging.basicConfig(level=logging.INFO)

    dp.include_router(command_start_and_cancel.router)
    dp.include_router(ordering_food.router)
    dp.include_router(ordering_drink.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())