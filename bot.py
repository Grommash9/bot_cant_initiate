from asyncio import get_event_loop
from aiogram import Dispatcher, Bot
from aiogram.types import ChatJoinRequest
from aiogram import executor

loop = get_event_loop()
bot = Bot('5714203048:AAH1BDAlwsK-UdxVsmD4aQwV4z-9o76XU2g', parse_mode='HTML')
dp = Dispatcher(bot, loop)


@dp.chat_join_request_handler()
async def new_join_request_process(event: ChatJoinRequest):
    await bot.send_message(chat_id=event.from_user.id,
                           text='Поздравляем, Ваш запрос на добавление в канал был одобрен.')
    await event.approve()


if __name__ == '__main__':
    executor.start_polling(dp)
