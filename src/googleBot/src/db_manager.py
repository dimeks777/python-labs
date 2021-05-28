import aiomysql
from pymysql import connect
from src.config import DB_NAME, DB_USER, DB_HOST, DB_PASSWORD, DB_PORT


async def create_con(loop):
    con = await aiomysql.connect(host=DB_HOST, user=DB_USER, db=DB_NAME, password=DB_PASSWORD, port=DB_PORT, loop=loop)
    cur = await con.cursor()
    return con, cur


def create_sync_con():
    con = connect(host=DB_HOST, user=DB_USER, db=DB_NAME,
                  password=DB_PASSWORD, port=DB_PORT)
    cur = con.cursor()
    return con, cur


class UsersDbManager:

    @staticmethod
    async def get_count_all_users(loop):
        con, cur = await create_con(loop)
        await cur.execute('select count(tel_id) from bot.users')
        res = await cur.fetchone()
        return res[0]

    @staticmethod
    def sync_is_exist(tel_id):
        con, cur = create_sync_con()
        cur.execute('select count(*) from bot.users where tel_id = %s', tel_id)
        res = cur.fetchone()
        con.close()
        return res[0] > 0

    @staticmethod
    async def get_using_count(loop):
        con, cur = await create_con(loop)
        await cur.execute('select count(tel_id) from bot.users where is_using = 1')
        result = await cur.fetchone()
        return result[0]

    @staticmethod
    async def get_no_using_count(loop):
        con, cur = await create_con(loop)
        await cur.execute('select count(tel_id) from bot.users where is_using = 0')
        result = await cur.fetchone()
        return result[0]

    @staticmethod
    async def count_all_users(loop):
        con, cur = await create_con(loop)
        await cur.execute('select count(tel_id) from bot.users')
        result = await cur.fetchone()
        con.close()
        return result[0]

    @staticmethod
    async def is_using(tel_id, loop):
        con, cur = await create_con(loop)
        await cur.execute('select is_using from bot.users where tel_id = %s and is_using=1', tel_id)
        res = await cur.fetchone()

        if res is None:
            return False

        return res[0] > 0

    @staticmethod
    async def add_user(tel_id, username, loop):
        con, cur = await create_con(loop)
        await cur.execute('insert into bot.users(tel_id, username, registered) values (%s, %s, CURRENT_TIME())',
                          (tel_id, username))
        await con.commit()
        con.close()

    @staticmethod
    async def is_exist(tel_id, loop):
        con, cur = await create_con(loop)
        await cur.execute('select count(*) from bot.users where tel_id = %s', tel_id)
        res = await cur.fetchone()

        if res is None:
            return False

        return res[0] > 0

    @staticmethod
    async def update_username(tel_id, username, loop):
        con, cur = await create_con(loop)
        await cur.execute('update bot.users set username = %s where tel_id = %s', (username, tel_id))
        await con.commit()
        con.close()

    @staticmethod
    async def get_all_users(loop):
        con, cur = await create_con(loop)
        await cur.execute('select tel_id, is_using from bot.users where is_using = 1')
        res = await cur.fetchall()

        if res is None:
            return []

        result = []
        for r in res:
            result.append(r[0])

        return result

    @staticmethod
    async def update_is_using(tel_id, status, loop):
        con, cur = await create_con(loop)
        await cur.execute('update bot.users set is_using = %s where tel_id = %s', (status, tel_id))
        await con.commit()
        con.close()

    @staticmethod
    async def set_state(tel_id, state, loop):
        con, cur = await create_con(loop)
        await cur.execute('update bot.users set user_stat = %s where tel_id = %s', (state, tel_id))
        await con.commit()
        con.close()

    @staticmethod
    def get_state(tel_id):
        con, cur = create_sync_con()
        cur.execute('select user_stat from bot.users where tel_id = %s', tel_id)
        res = cur.fetchone()
        con.close()
        return res[0]


class VacanciesDBManager:
    @staticmethod
    async def create_vacancy_entry(user_id, username, telephone, vacancy, vacancy_description, loop):
        con, cur = await create_con(loop)
        await cur.execute(
            'insert into bot.vacancies(user_id,username,telephone,vacancy, vacancy_description, date_created) values '
            '(%s,%s,%s,%s,%s,CURRENT_TIME())', (user_id, username, telephone, vacancy, vacancy_description))
        await cur.execute(
            'insert into bot.actions(user_id,date_created) values '
            '(%s,CURRENT_TIME())', user_id)
        await con.commit()
        con.close()

    @staticmethod
    async def select_vacancies_by_keyword(loop, vacancy):
        con, cur = await create_con(loop)
        await cur.execute(
            "select vacancy,vacancy_description,username, telephone from bot.vacancies where vacancy LIKE '%%%s%%' " % vacancy)
        res = await cur.fetchall()

        if res is None:
            return []

        result = []
        for r in res:
            result.append(r)

        return result


class ActivityDBManager:
    @staticmethod
    async def get_usage_statistics(loop):
        con, cur = await create_con(loop)
        await cur.execute('select count(*) from bot.actions where date_created >= DATE_SUB(NOW(), INTERVAL 1 DAY)')
        last_day = await cur.fetchone()
        await cur.execute('select count(*) from bot.actions where date_created >= DATE_SUB(NOW(), INTERVAL 30 DAY)')
        last_month = await cur.fetchone()
        await cur.execute('select count(*) from bot.actions')
        all = await cur.fetchone()
        return last_day, last_month, all
