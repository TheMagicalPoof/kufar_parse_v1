from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import sys
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from peewee import SqliteDatabase


storage = MemoryStorage()

BOT = Bot(token="1516696135:AAEmy1ICA1OcTP3lanRfRJiW51oDvVPQOAU")
DP = Dispatcher(BOT, storage=storage)
DB = SqliteDatabase("db/test.db")
