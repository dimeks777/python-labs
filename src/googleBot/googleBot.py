import asyncio
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram import types
from src.config import TOKEN, GOOGLE_FORM, MY_ID
import src.keyboard as kb
import src.db_manager as db

# Configure logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('broadcast')

# Initialize bot and dispatcher
loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def is_admin(tg_id: int):
    return tg_id == MY_ID


@dp.message_handler(lambda msg: db.UsersDbManager.sync_is_exist(msg.from_user.id) is False, commands=['start'])
async def start_message_handler(msg: types.Message):
    user_id = msg.from_user.id
    await db.UsersDbManager.add_user(user_id, msg.from_user.username, loop)
    if is_admin(user_id):
        await msg.answer("Вы зарегистрировались как админ", reply_markup=kb.main_menu)
    else:
        await msg.answer("Вы зарегистрировались как пользователь", reply_markup=kb.main_menu_user)


@dp.message_handler(lambda msg: is_admin(msg.from_user.id) is True, commands=['start'])
async def start_message_handler(msg: types.Message):
    await msg.answer("Вы уже зарегистрированы как админ!", reply_markup=kb.main_menu)


@dp.message_handler(commands=['start'])
async def start_message_handler(msg: types.Message):
    await msg.answer("Вы уже зарегистрированы как пользователь!", reply_markup=kb.main_menu_user)


@dp.message_handler(text='Создать вакансию')
async def post_message_handler(msg: types.Message):
    await msg.answer(GOOGLE_FORM.format(msg.from_user.id, "@" + msg.from_user.username))


@dp.message_handler(commands=['vacancy'])
async def post_message_handler(msg: types.Message):
    await msg.answer(GOOGLE_FORM.format(msg.from_user.id, "@" + msg.from_user.username))


@dp.message_handler(lambda msg: is_admin(msg.from_user.id) is True, text='Статистика пользования')
async def start_message_handler(msg: types.Message):
    result = await get_statistics(loop)
    await msg.answer(format_statistics(result[0], result[1], result[2], result[3], result[4], result[5]),
                     reply_markup=kb.main_menu,
                     parse_mode='HTML')


@dp.message_handler(lambda msg: is_admin(msg.from_user.id) is True, commands=['statistics'])
async def start_message_handler(msg: types.Message):
    result = await get_statistics(loop)
    await msg.answer(format_statistics(result[0], result[1], result[2], result[3], result[4], result[5]),
                     reply_markup=kb.main_menu,
                     parse_mode='HTML')


@dp.my_chat_member_handler()
async def bot_blocked_handler(msg: types.Message):
    is_using = await db.UsersDbManager.is_using(msg.from_user.id, loop)
    print(is_using)
    await db.UsersDbManager.update_is_using(msg.from_user.id, 0 if is_using else 1, loop)


@dp.message_handler(commands=['find'])
async def find_message_handler(msg: types.Message):
    await db.UsersDbManager.set_state(msg.chat.id, "WAIT_TEXT", loop)
    await bot.send_message(msg.chat.id, "Введите название вакансии")


@dp.message_handler(text='Поиск вакансий')
async def find_message_handler(msg: types.Message):
    await db.UsersDbManager.set_state(msg.chat.id, "WAIT_TEXT", loop)
    await bot.send_message(msg.chat.id, "Введите название вакансии")


@dp.message_handler(lambda msg: db.UsersDbManager.get_state(msg.chat.id) == "WAIT_TEXT")
async def find_message_handler(msg: types.Message):
    vacancies = await db.VacanciesDBManager.select_vacancies_by_keyword(loop, msg.text)
    text = ""
    for v in vacancies:
        text += format_vacancy(v[0], v[1], v[2], v[3]) + "\n\n---------------------------------------\n\n"
    if is_admin(msg.chat.id):
        await msg.answer(text, reply_markup=kb.main_menu, parse_mode='HTML')
    else:
        await msg.answer(text, reply_markup=kb.main_menu_user, parse_mode='HTML')


async def get_statistics(loop):
    result = await db.ActivityDBManager.get_usage_statistics(loop)
    users = await db.UsersDbManager.count_all_users(loop)
    active_users = await db.UsersDbManager.get_using_count(loop)
    non_active_users = await db.UsersDbManager.get_no_using_count(loop)
    return result[0], result[1], result[2], users, active_users, non_active_users


def format_statistics(last_day, last_month, all, users, active_users, non_active_users):
    return "<b>Статистика использования(отправлено вакансий)</b>: \n\n<b>За последний день: {0}</b>\n" \
           "<b>За последний месяц: {1}</b>\n" \
           "<b>За всё время: {2}</b>\n\n" \
           "<b>Всего пользователей: {3}</b>\n" \
           "<b>Активных пользователей {4}</b>\n" \
           "<b>Неактивных пользователй: {5}</b>".format(last_day[0], last_month[0], all[0], users, active_users,
                                                        non_active_users)


def format_vacancy(vacancy, description, username, telephone):
    return "<b>Вакансия</b>: {0}\n<b>Описание</b>: {1}\n\n<b>Контакт</b>:\nИмя пользователя: {2}\n" \
           "Телефон: {3}".format(vacancy, description, username, telephone)


if __name__ == '__main__':
    executor.start_polling(dp)
