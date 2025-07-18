import asyncio
import logging, sys
from aiogram import Bot, Dispatcher
from config import TOKEN
from start import chat_router
# from events import event

dp = Dispatcher()
async def main() -> None:
    dp.include_router(chat_router)
    # dp.include_router(event) #пока что данный импорт не необходим
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())