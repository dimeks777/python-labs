import asyncio
import logging
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import aioschedule as schedule
import json

from googleBot import bot, format_vacancy
from src.config import CHAT_ID
import src.db_manager as db

l = asyncio.get_event_loop()

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('broadcast')

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

client = gspread.authorize(creds)

sheet = client.open("BOT").sheet1


def get_last_row():
    row = sheet.get_all_values()
    return row[len(row) - 1]


def get_last_record():
    f = open('last_record.txt', 'r')
    return json.load(f)


def update_last_record(input_record):
    f = open('last_record.txt', 'w')
    json.dump(input_record, f)


async def ping_sheets():
    update_row = get_last_row()
    last_record = get_last_record()
    if update_row == last_record:
        print('Нет изменений')
    else:
        print('Получена новая строка!')
        update_last_record(update_row)
        try:
            await db.VacanciesDBManager.create_vacancy_entry(user_id=update_row[2], username=update_row[1],
                                                             telephone=update_row[3],
                                                             vacancy=update_row[4], vacancy_description=update_row[5],
                                                             loop=l)
        except Exception as e:
            log.warning(e)
        text = format_vacancy(update_row[4], update_row[5], update_row[1], update_row[3])
        await bot.send_message(CHAT_ID, text, parse_mode='HTML')
        await bot.send_message(update_row[2], "Ваша вакансия успешно размещена!")


schedule.every(5).seconds.do(ping_sheets)

loop = asyncio.get_event_loop()
while True:
    loop.run_until_complete(schedule.run_pending())
    time.sleep(1)
