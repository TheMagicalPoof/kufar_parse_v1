from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


def get_rkm(items: list):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in items:
        if isinstance(i, list):
            keyboard.row(*list(map(KeyboardButton, i)))
            continue
        keyboard.add(KeyboardButton(i))
    return keyboard


def get_ikm(items: list):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for item in items:
        if isinstance(item, list):
            pass
        if isinstance(item, dict):
            item.values()
            keyboard.add(InlineKeyboardButton(item.value()))



"""Main menu keyboard"""
kb_menu = get_rkm(["Отслеживать предмет",
                   "Изменить предмет",
                   "Удалить предмет",
                   "Вкл оповещение",
                   "Выкл оповещение",
                   "Обратная связь"])

"""Клавиатура редактирования предмета"""
kb_edit = get_rkm(["Название",
                   "Ассоциации",
                   'Цену "от"',
                   'Цену "до"',
                   "Область поиска",
                   "Назад"])

"""Клавиатура Цена от:"""
kb_from = get_rkm(["Даром"])

"""Клавиатура Цена до:"""
kb_to = get_rkm(["Бесконечно"])

"""Клавиатура отмены/подтвержения предмета"""
kb_confirm = get_rkm(["Редактировать",
                      "Подтвердить",
                      "Отменить"])

"""Клавиатура подтверждения удаления"""
kb_remove = get_rkm(["Удалить", "Не Удалять"])

"""Клавиатура региона"""
kb_reg = get_rkm(["Вся Беларусь", "Минск", "Минская обл.", "Брестская обл.", "Гомельская обл.", "Гродненская обл.", "Могилевская обл."])




"""Минск"""
kb_minsk_dis = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_minsk_dis_1 = KeyboardButton("Весь Минск")
kb_minsk_dis_2 = KeyboardButton("Центральный")
kb_minsk_dis_3 = KeyboardButton("Советский")
kb_minsk_dis_4 = KeyboardButton("Первомайский")
kb_minsk_dis_5 = KeyboardButton("Партизанский")
kb_minsk_dis_6 = KeyboardButton("Заводской")
kb_minsk_dis_7 = KeyboardButton("Ленинский")
kb_minsk_dis_8 = KeyboardButton("Октябрьский")
kb_minsk_dis_9 = KeyboardButton("Московский")
kb_minsk_dis.add(kb_minsk_dis_1)
kb_minsk_dis.row(kb_minsk_dis_2, kb_minsk_dis_3)
kb_minsk_dis.row(kb_minsk_dis_4, kb_minsk_dis_5)
kb_minsk_dis.row(kb_minsk_dis_6, kb_minsk_dis_7)
kb_minsk_dis.row(kb_minsk_dis_8, kb_minsk_dis_9)


"""Минская область"""
kb_minsk_reg = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_minsk_reg_1 = KeyboardButton("Любой")
kb_minsk_reg_2 = KeyboardButton("Березино")
kb_minsk_reg_3 = KeyboardButton("Борисов")
kb_minsk_reg_4 = KeyboardButton("Вилейка")
kb_minsk_reg_5 = KeyboardButton("Воложин")
kb_minsk_reg_6 = KeyboardButton("Дзержинск")
kb_minsk_reg_7 = KeyboardButton("Жодино")
kb_minsk_reg_8 = KeyboardButton("Заславль")
kb_minsk_reg_9 = KeyboardButton("Клецк")
kb_minsk_reg_10 = KeyboardButton("Копыль")
kb_minsk_reg_11 = KeyboardButton("Крупки")
kb_minsk_reg_12 = KeyboardButton("Логойск")
kb_minsk_reg_13 = KeyboardButton("Любань")
kb_minsk_reg_14 = KeyboardButton("Марьина Горка")
kb_minsk_reg_15 = KeyboardButton("Молодечно")
kb_minsk_reg_16 = KeyboardButton("Мядель")
kb_minsk_reg_17 = KeyboardButton("Несвиж")
kb_minsk_reg_18 = KeyboardButton("Руденск")
kb_minsk_reg_19 = KeyboardButton("Слуцк")
kb_minsk_reg_20 = KeyboardButton("Смолевичи")
kb_minsk_reg_21 = KeyboardButton("Солигорск")
kb_minsk_reg_22 = KeyboardButton("Старые Дороги")
kb_minsk_reg_23 = KeyboardButton("Столбцы")
kb_minsk_reg_24 = KeyboardButton("Узда")
kb_minsk_reg_25 = KeyboardButton("Фаниполь")
kb_minsk_reg_26 = KeyboardButton("Червень")
kb_minsk_reg_27 = KeyboardButton("Другие")
kb_minsk_reg.add(kb_minsk_reg_1)
kb_minsk_reg.row(kb_minsk_reg_2, kb_minsk_reg_3)
kb_minsk_reg.row(kb_minsk_reg_4, kb_minsk_reg_5)
kb_minsk_reg.row(kb_minsk_reg_6, kb_minsk_reg_7)
kb_minsk_reg.row(kb_minsk_reg_8, kb_minsk_reg_9)
kb_minsk_reg.row(kb_minsk_reg_10, kb_minsk_reg_11)
kb_minsk_reg.row(kb_minsk_reg_12, kb_minsk_reg_13)
kb_minsk_reg.row(kb_minsk_reg_14, kb_minsk_reg_15)
kb_minsk_reg.row(kb_minsk_reg_16, kb_minsk_reg_17)
kb_minsk_reg.row(kb_minsk_reg_18, kb_minsk_reg_19)
kb_minsk_reg.row(kb_minsk_reg_20, kb_minsk_reg_21)
kb_minsk_reg.row(kb_minsk_reg_22, kb_minsk_reg_23)
kb_minsk_reg.row(kb_minsk_reg_24, kb_minsk_reg_25)
kb_minsk_reg.row(kb_minsk_reg_26, kb_minsk_reg_27)


"""Брестская обл"""
kb_brest = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_brest_1 = KeyboardButton("Любой")
kb_brest_2 = KeyboardButton("Брест")
kb_brest_3 = KeyboardButton("Барановичи")
kb_brest_4 = KeyboardButton("Береза")
kb_brest_5 = KeyboardButton("Белоозерск")
kb_brest_6 = KeyboardButton("Ганцевичи")
kb_brest_7 = KeyboardButton("Дрогичин")
kb_brest_8 = KeyboardButton("Жабинка")
kb_brest_9 = KeyboardButton("Иваново")
kb_brest_10 = KeyboardButton("Ивацевичи")
kb_brest_11 = KeyboardButton("Каменец")
kb_brest_12 = KeyboardButton("Кобрин")
kb_brest_13 = KeyboardButton("Лунинец")
kb_brest_14 = KeyboardButton("Ляховичи")
kb_brest_15 = KeyboardButton("Малорита")
kb_brest_16 = KeyboardButton("Пинск")
kb_brest_17 = KeyboardButton("Пружаны")
kb_brest_18 = KeyboardButton("Столин")
kb_brest_19 = KeyboardButton("Другие")
kb_brest.add(kb_brest_1)
kb_brest.row(kb_brest_2, kb_brest_3)
kb_brest.row(kb_brest_4, kb_brest_5)
kb_brest.row(kb_brest_6, kb_brest_7)
kb_brest.row(kb_brest_8, kb_brest_9)
kb_brest.row(kb_brest_10, kb_brest_11)
kb_brest.row(kb_brest_12, kb_brest_13)
kb_brest.row(kb_brest_14, kb_brest_15)
kb_brest.row(kb_brest_16, kb_brest_17)
kb_brest.row(kb_brest_18, kb_brest_19)


"""Гомельская обл"""
kb_gomel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_gomel_1 = KeyboardButton("Любой")
kb_gomel_2 = KeyboardButton("Гомель")
kb_gomel_3 = KeyboardButton("Брагин")
kb_gomel_4 = KeyboardButton("Буда-Кошелево")
kb_gomel_5 = KeyboardButton("Ветка")
kb_gomel_6 = KeyboardButton("Добруш")
kb_gomel_7 = KeyboardButton("Жидковичи")
kb_gomel_8 = KeyboardButton("Жлобин")
kb_gomel_9 = KeyboardButton("Калинковичи")
kb_gomel_10 = KeyboardButton("Корма")
kb_gomel_11 = KeyboardButton("Лельчицы")
kb_gomel_12 = KeyboardButton("Лоев")
kb_gomel_13 = KeyboardButton("Мозырь")
kb_gomel_14 = KeyboardButton("Октябрьский")
kb_gomel_15 = KeyboardButton("Наровля")
kb_gomel_16 = KeyboardButton("Петриков")
kb_gomel_17 = KeyboardButton("Речица")
kb_gomel_18 = KeyboardButton("Рогачев")
kb_gomel_19 = KeyboardButton("Светлогорск")
kb_gomel_20 = KeyboardButton("Хойники")
kb_gomel_21 = KeyboardButton("Чечерск")
kb_gomel_22 = KeyboardButton("Другие")
kb_gomel.row(kb_gomel_1, kb_gomel_2)
kb_gomel.row(kb_gomel_3, kb_gomel_4)
kb_gomel.row(kb_gomel_5, kb_gomel_6)
kb_gomel.row(kb_gomel_7, kb_gomel_8)
kb_gomel.row(kb_gomel_9, kb_gomel_10)
kb_gomel.row(kb_gomel_11, kb_gomel_12)
kb_gomel.row(kb_gomel_13, kb_gomel_14)
kb_gomel.row(kb_gomel_15, kb_gomel_16)
kb_gomel.row(kb_gomel_17, kb_gomel_18)
kb_gomel.row(kb_gomel_19, kb_gomel_20)
kb_gomel.row(kb_gomel_21, kb_gomel_22)


"""Гродненская область"""
kb_hrodno = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_hrodno_1 = KeyboardButton("Любой")
kb_hrodno_2 = KeyboardButton("Гродно")
kb_hrodno_3 = KeyboardButton("Березовка")
kb_hrodno_4 = KeyboardButton("Берестовица")
kb_hrodno_5 = KeyboardButton("Волковыск")
kb_hrodno_6 = KeyboardButton("Вороново")
kb_hrodno_7 = KeyboardButton("Дятлово")
kb_hrodno_8 = KeyboardButton("Зельва")
kb_hrodno_9 = KeyboardButton("Ивье")
kb_hrodno_10 = KeyboardButton("Кореличи")
kb_hrodno_11 = KeyboardButton("Лида")
kb_hrodno_12 = KeyboardButton("Мосты")
kb_hrodno_13 = KeyboardButton("Новогрудок")
kb_hrodno_14 = KeyboardButton("Островец")
kb_hrodno_15 = KeyboardButton("Ошмяны")
kb_hrodno_16 = KeyboardButton("Свислочь")
kb_hrodno_17 = KeyboardButton("Скидель")
kb_hrodno_18 = KeyboardButton("Слоним")
kb_hrodno_19 = KeyboardButton("Сморгонь")
kb_hrodno_20 = KeyboardButton("Щучин")
kb_hrodno_21 = KeyboardButton("Другие")
kb_hrodno.add(kb_hrodno_1)
kb_hrodno.row(kb_hrodno_2, kb_hrodno_3)
kb_hrodno.row(kb_hrodno_4, kb_hrodno_5)
kb_hrodno.row(kb_hrodno_6, kb_hrodno_7)
kb_hrodno.row(kb_hrodno_8, kb_hrodno_9)
kb_hrodno.row(kb_hrodno_10, kb_hrodno_11)
kb_hrodno.row(kb_hrodno_12, kb_hrodno_13)
kb_hrodno.row(kb_hrodno_14, kb_hrodno_15)
kb_hrodno.row(kb_hrodno_16, kb_hrodno_17)
kb_hrodno.row(kb_hrodno_18, kb_hrodno_19)
kb_hrodno.row(kb_hrodno_20, kb_hrodno_21)


"""Могилевская обл"""
kb_mogilev = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_mogilev_1 = KeyboardButton("Любой")
kb_mogilev_2 = KeyboardButton("Могилев")
kb_mogilev_3 = KeyboardButton("Белыничи")
kb_mogilev_4 = KeyboardButton("Бобруйск")
kb_mogilev_5 = KeyboardButton("Быхов")
kb_mogilev_6 = KeyboardButton("Глуск")
kb_mogilev_7 = KeyboardButton("Горки")
kb_mogilev_8 = KeyboardButton("Дрибин")
kb_mogilev_9 = KeyboardButton("Кировск")
kb_mogilev_10 = KeyboardButton("Климовичи")
kb_mogilev_11 = KeyboardButton("Кличев")
kb_mogilev_12 = KeyboardButton("Краснополье")
kb_mogilev_13 = KeyboardButton("Круглое")
kb_mogilev_14 = KeyboardButton("Костюковичи")
kb_mogilev_15 = KeyboardButton("Кричев")
kb_mogilev_16 = KeyboardButton("Мстиславль")
kb_mogilev_17 = KeyboardButton("Осиповичи")
kb_mogilev_18 = KeyboardButton("Славгород")
kb_mogilev_19 = KeyboardButton("Чаусы")
kb_mogilev_20 = KeyboardButton("Чериков")
kb_mogilev_21 = KeyboardButton("Шклов")
kb_mogilev_22 = KeyboardButton("Хотимск")
kb_mogilev_23 = KeyboardButton("Другие")
kb_mogilev.add(kb_mogilev_1)
kb_mogilev.row(kb_mogilev_2, kb_mogilev_3)
kb_mogilev.row(kb_mogilev_4, kb_mogilev_5)
kb_mogilev.row(kb_mogilev_6, kb_mogilev_7)
kb_mogilev.row(kb_mogilev_8, kb_mogilev_9)
kb_mogilev.row(kb_mogilev_10, kb_mogilev_11)
kb_mogilev.row(kb_mogilev_12, kb_mogilev_13)
kb_mogilev.row(kb_mogilev_14, kb_mogilev_15)
kb_mogilev.row(kb_mogilev_16, kb_mogilev_17)
kb_mogilev.row(kb_mogilev_18, kb_mogilev_19)
kb_mogilev.row(kb_mogilev_20, kb_mogilev_21)
kb_mogilev.row(kb_mogilev_22, kb_mogilev_23)


"""Витебская обл"""
kb_vitebsk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_vitebsk_1 = KeyboardButton("Любой")
kb_vitebsk_2 = KeyboardButton("Витебск")
kb_vitebsk_3 = KeyboardButton("Бешенковичи")
kb_vitebsk_4 = KeyboardButton("Барань")
kb_vitebsk_5 = KeyboardButton("Браслав")
kb_vitebsk_6 = KeyboardButton("Верхнедвинск")
kb_vitebsk_7 = KeyboardButton("Глубокое")
kb_vitebsk_8 = KeyboardButton("Городок")
kb_vitebsk_9 = KeyboardButton("Докшицы")
kb_vitebsk_10 = KeyboardButton("Дубровно")
kb_vitebsk_11 = KeyboardButton("Лепель")
kb_vitebsk_12 = KeyboardButton("Лиозно")
kb_vitebsk_13 = KeyboardButton("Миоры")
kb_vitebsk_14 = KeyboardButton("Новолукомль")
kb_vitebsk_15 = KeyboardButton("Новополоцк")
kb_vitebsk_16 = KeyboardButton("Орша")
kb_vitebsk_17 = KeyboardButton("Полоцк")
kb_vitebsk_18 = KeyboardButton("Поставы")
kb_vitebsk_19 = KeyboardButton("Россоны")
kb_vitebsk_20 = KeyboardButton("Сенно")
kb_vitebsk_21 = KeyboardButton("Толочин")
kb_vitebsk_22 = KeyboardButton("Ушачи")
kb_vitebsk_23 = KeyboardButton("Чашники")
kb_vitebsk_24 = KeyboardButton("Шарковщина")
kb_vitebsk_25 = KeyboardButton("Шумилино")
kb_vitebsk_26 = KeyboardButton("Другие")
kb_vitebsk.row(kb_vitebsk_1, kb_vitebsk_2)
kb_vitebsk.row(kb_vitebsk_3, kb_vitebsk_4)
kb_vitebsk.row(kb_vitebsk_5, kb_vitebsk_6)
kb_vitebsk.row(kb_vitebsk_7, kb_vitebsk_8)
kb_vitebsk.row(kb_vitebsk_9, kb_vitebsk_10)
kb_vitebsk.row(kb_vitebsk_11, kb_vitebsk_12)
kb_vitebsk.row(kb_vitebsk_13, kb_vitebsk_14)
kb_vitebsk.row(kb_vitebsk_15, kb_vitebsk_16)
kb_vitebsk.row(kb_vitebsk_17, kb_vitebsk_18)
kb_vitebsk.row(kb_vitebsk_19, kb_vitebsk_20)
kb_vitebsk.row(kb_vitebsk_21, kb_vitebsk_22)
kb_vitebsk.row(kb_vitebsk_23, kb_vitebsk_24)
kb_vitebsk.row(kb_vitebsk_25, kb_vitebsk_26)