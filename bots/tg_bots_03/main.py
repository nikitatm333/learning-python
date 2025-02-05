import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import user_router


async def main():
    bot = Bot(token="7857738086:")
    dp = Dispatcher()
    dp.include_router(router=user_router)
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO) # Подключение логирования
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')