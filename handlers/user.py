from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from keyboards import kb_menu, kb_from, kb_to, kb_reg, kb_confirm
from keyboards import kb_minsk_reg, kb_minsk_dis, kb_brest, kb_gomel, kb_hrodno, kb_mogilev, kb_vitebsk
from aiogram.types import ReplyKeyboardRemove
from keyboards import get_rkm
from db import Region, District

from create_bot import DP, BOT


class StatesUser(StatesGroup):
    main = State()
    add_item = State()
    edit_item = State()
    rem_item = State()
    feedback = State()


class StatesUserAddItem(StatesGroup):
    name = State()
    price_from = State()
    price_to = State()
    region = State()
    district = State()
    confirm = State()


async def cm_start(message: types.Message):
    await BOT.send_message(message.chat.id, "Этот бот создан для парсинга куфара /menu что бы начать")


async def cm_menu(message: types.Message):
    await StatesUser.main.set()
    await BOT.send_message(message.chat.id, text="Главное меню:", reply_markup=kb_menu)


async def menu_cb(message: types.Message):
    if message.text == "Отслеживать предмет":
        await StatesUser.next()
        await StatesUserAddItem.name.set()
        await BOT.send_message(message.chat.id, text="Напишите название предмета:", reply_markup=ReplyKeyboardRemove())


async def name_cb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await StatesUserAddItem.next()
    await BOT.send_message(message.chat.id,
                           text='Укажите цену "от":', reply_markup=kb_from)


async def price_from_cb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.isdigit():
            data["price_from"] = int(message.text)
        elif message.text == "Даром":
            data["price_from"] = 0
        else:
            await BOT.send_message(message.chat.id,
                                   text='Укажите цену "от":', reply_markup=kb_from)
            return

    await StatesUserAddItem.next()
    await BOT.send_message(message.chat.id, text='Укажите цену "до":', reply_markup=kb_to)


async def price_to_cb(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        if message.text == "Бесконечно":
            data["price_to"] = 0
        elif message.text.isdigit():
            if int(message.text) == 0:
                await BOT.send_message(message.chat.id, text=f'Цена "до" не может быть равна 0! Укажите корректно:', reply_markup=kb_to)
                return
            if data.get("price_from") > int(message.text):
                await BOT.send_message(message.chat.id, text=f'Цена "до" не может быть меньше {data.get("price_from")} р. Укажите корректно:', reply_markup=kb_to)
                return
            data["price_to"] = int(message.text)
        else:
            await BOT.send_message(message.chat.id,
                                   text=f'Укажите цену "до" корректно:',
                                   reply_markup=kb_to)
            return
        await StatesUserAddItem.next()

        await BOT.send_message(message.chat.id,
                               text='Укажите область поиска:',
                               reply_markup=get_rkm([item.name for item in Region.select()]))


async def reg_cb(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        await BOT.send_message(message.chat.id, text=f'Укажите район:', reply_markup=get_rkm([item.district_name for item in District.select().where()]))
        if message.text == "Вся Беларусь":
            await StatesUserAddItem.confirm.set()
            data["reg"] = message.text
            await BOT.send_message(message.chat.id,
                                   text=f'Перепроверте, всё ли верно?\nПредмет #{data.get("name")}\nЦена: от {data.get("price_from")} до {data.get("price_to")}\nОбласть поиска: {data.get("reg")}',
                                   reply_markup=kb_confirm)
            return

        if message.text == "Минск":
            await BOT.send_message(message.chat.id, text=f'Укажите район:', reply_markup=kb_minsk_reg)
        elif message.text == "Минская обл.":
            await BOT.send_message(message.chat.id, text=f'Укажите район:', reply_markup=kb_minsk_dis)
        elif message.text == "Брестская обл.":
            await BOT.send_message(message.chat.id, text=f'Укажите район:', reply_markup=kb_brest)
        elif message.text == "Гомельская обл.":
            await BOT.send_message(message.chat.id, text=f'Укажите район:', reply_markup=kb_gomel)
        elif message.text == "Гродненская обл.":
            await BOT.send_message(message.chat.id, text=f'Укажите район:', reply_markup=kb_hrodno)
        elif message.text == "Могилевская обл.":
            await BOT.send_message(message.chat.id, text=f'Укажите район:', reply_markup=kb_mogilev)
        else:
            await BOT.send_message(message.chat.id,
                                   text='Укажите корректную область поиска:',
                                   reply_markup=kb_reg)
            return

        data["reg"] = message.text
        await StatesUserAddItem.next()


async def dis_cb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass


async def confirm_cb(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        async with state.proxy() as data:
            print(str(data))
            await BOT.send_message(message.chat.id,
                                   text=f'Отлично, бот вас уведомит как только на площадке появится #{data.get("name")}',
                                   reply_markup=ReplyKeyboardRemove())
            await state.finish()
    if message.text == "Отменить":
        await BOT.send_message(message.chat.id,
                               text='Вы всё отменили операцию.',
                               reply_markup=ReplyKeyboardRemove())
        await state.finish()


def register_handlers_user(dp: Dispatcher):

    """commands handlers"""
    dp.register_message_handler(cm_start, commands=["start", "help"])
    dp.register_message_handler(cm_menu, commands="menu")

    """MainMenu handler"""
    dp.register_message_handler(menu_cb, state=StatesUser.main)

    """AddItem handlers"""
    dp.register_message_handler(name_cb, state=[StatesUser.add_item, StatesUserAddItem.name])
    dp.register_message_handler(price_from_cb, state=[StatesUser.add_item, StatesUserAddItem.price_from])
    dp.register_message_handler(price_to_cb, state=[StatesUser.add_item, StatesUserAddItem.price_to])
    dp.register_message_handler(reg_cb, state=[StatesUser.add_item, StatesUserAddItem.region])
    # dp.register_message_handler(reg_cb, state=[StatesUser.add_item, StatesUserAddItem.district])
    dp.register_message_handler(confirm_cb, state=[StatesUser.add_item, StatesUserAddItem.confirm])



