from aiogram.types import reply_keyboard, inline_keyboard

main_menu = reply_keyboard.ReplyKeyboardMarkup([["Создать вакансию", "Статистика пользования"], ["Поиск вакансий"]], resize_keyboard=True)
main_menu_user = reply_keyboard.ReplyKeyboardMarkup([["Создать вакансию", "Поиск вакансий"]], resize_keyboard=True)
