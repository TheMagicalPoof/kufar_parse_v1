from aiogram.utils import executor
from create_bot import DP
from handlers import user


async def on_startup(_):
    print("Bot is online now!")


user.register_handlers_user(DP)

executor.start_polling(DP, skip_updates=True, on_startup=on_startup)
