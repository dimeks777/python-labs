import argparse
import os
import time
from datetime import datetime, timedelta

import draw
import parse
from app_logger import get_logger


def add_args():
    print("adding args")
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--path", action="store", default='./results',
                        help='Path to a directory where results will be saved')
    parser.add_argument('-f', "--from_date", action="store", dest='from_date',
                        default=(datetime.today() - timedelta(30)).strftime('%Y-%m-%d'),
                        help='Start date of news. Enter in yyyy-MM-dd format ')
    parser.add_argument('-t', "--to_date", action="store", dest='to_date',
                        default=datetime.today().strftime('%Y-%m-%d'),
                        help='End date of news. Enter in yyyy-MM-dd format')
    parser.add_argument('-k', "--keyword", action="store", dest='keyword', default='bitcoin',
                        help='Keyword to find news')
    parser.add_argument('-s', '--sources', nargs='+', dest='sources', default=['techcrunch'])
    parser.add_argument('-c', '--companies', nargs='+', dest='companies', default=['AAPL', 'MSFT', 'NFLX', 'AMZN'])

    return parser.parse_args()


if __name__ == '__main__':
    logger = get_logger(__name__)
    logger.info("Script started")
    start_time = time.time()
    args = add_args()
    path = os.path.abspath(args.path)
    from_date = datetime.strptime(args.from_date, '%Y-%m-%d')
    to_date = datetime.strptime(args.to_date, '%Y-%m-%d')
    sources = ", ".join(args.sources)
    if not os.path.exists(path):
        os.makedirs(path)
    parse.do_task(path, from_date, to_date, args.keyword, sources, args.companies)
    draw.do_draw(os.path.join(path, 'finance'), path)
    logger.info("Script finished successfully in %.2f seconds" % (time.time() - start_time))
