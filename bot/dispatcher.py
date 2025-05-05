from aiogram import Dispatcher

from bot.handlers.main_handler import main_router
from bot.handlers.user import user_router
from env_data.utils import Env

TOKEN = Env().bot.TOKEN


dp = Dispatcher()

dp.include_routers(*[main_router, user_router])