# API KEY 14c3fe61be5b4f5a87820c702eb67659
import concurrent.futures
import re
from datetime import datetime, timedelta
from itertools import cycle
from typing import List

import pandas as pd

from bs4 import BeautifulSoup
import requests as requests

api = '14c3fe61be5b4f5a87820c702eb67659'
data = ['Book Value Per Share', 'Gross Profit', 'Return on Assets']
read = False


class SearchParams:
    def __init__(self, keyword, sources, from_date, to_date, sort_by, page_size, page, api_key):
        self.keyword = keyword
        self.sources = sources
        self.from_date = from_date
        self.to_date = to_date
        self.sort_by = sort_by
        self.page_size = page_size
        self.page = page
        self.api_key = api_key


class NewsApiPayload:

    def __init__(self, title, description, published_at, url, author):
        self.title = title
        self.description = description
        self.published_at = published_at
        self.url = url
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Description: {self.description}\n" \
               f"Published at: {self.published_at}\n" \
               f"Url: {self.url}\n" \
               f"Author: {self.author}\n\n"

    def __repr__(self):
        return f"NewsApiPayload({self.title},{self.description},{self.published_at},{self.url}, {self.author})"

    def __ne__(self, other):
        return self.title is not other.title

    def __key(self):
        return self.title

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, NewsApiPayload):
            return self.__key() == other.__key()
        return NotImplemented


class FinanceYahooResponse:

    def __init__(self, company_name, book_value_per_share, gross_profit, return_on_assets):
        self.company_name = company_name
        self.book_value_per_share = book_value_per_share
        self.gross_profit = gross_profit
        self.return_on_assets = return_on_assets

    def __str__(self):
        return f'Company: {self.company_name}\n' \
               f'Book value per share: {self.book_value_per_share}\n' \
               f'Gross profit: {self.gross_profit}\n' \
               f'Return on assets: {self.return_on_assets}\n\n'


def get_payload(article):
    return NewsApiPayload(article['title'],
                          article['description'],
                          article['publishedAt'],
                          article['url'],
                          article['author'])


def get_proxies():
    response = requests.get("https://free-proxy-list.net").text

    soup = BeautifulSoup(response, 'html.parser')
    proxy_dict = {}
    proxy_list = list()
    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        try:
            proxy_dict['ip'] = cols[0].text
        except:
            proxy_dict['ip'] = None
        try:
            proxy_dict['port'] = cols[1].text
        except:
            proxy_dict['port'] = None
        try:
            proxy_dict['country'] = cols[3].text
        except:
            proxy_dict['country'] = None
        if proxy_dict['port'] is not None:
            proxy_list.append(proxy_dict)

        proxy_dict = {}
    return proxy_list


def build_news_url(search_params: SearchParams):
    return f'https://newsapi.org/v2/everything? q="{search_params.keyword}"&sources={search_params.sources}' \
           f'&from={search_params.from_date}&to={search_params.to_date}&sortBy={search_params.sort_by}' \
           f'&pageSize={search_params.page_size}&page={search_params.page}&apiKey={search_params.api_key} '


def get_news(search_params: SearchParams, proxies):
    r = get_request(f'https://newsapi.org/v2/everything?'
                    f'q="{search_params.keyword}"&sources={search_params.sources}&from={search_params.from_date}'
                    f'&to={search_params.to_date}'
                    f'&sortBy={search_params.sort_by}&pageSize={search_params.page_size}&page={search_params.page}'
                    f'&apiKey={search_params.api_key}', proxies)

    json_response = r.json()
    articles = {get_payload(x) for x in json_response['articles']}
    return sorted(list(articles), key=lambda x: datetime.fromisoformat(x.published_at[:-1]), reverse=True)


def get_request(url, proxies):
    proxy_pool = cycle(proxies)
    while True:
        proxy = next(proxy_pool)
        p = proxy['ip'] + ':' + proxy['port']
        pp = {
            'http': p,
            'https': p
        }
        print(pp)
        try:
            r = requests.get(url, proxies=pp)
            return r
        except Exception as e:
            print(f'{str(e)}Connect to {p} error. Skipping...')


def get_finance_data(company, proxies):
    r2 = get_request(f'https://finance.yahoo.com/quote/{company}/key-statistics', proxies)
    soup = BeautifulSoup(r2.text, 'html.parser')
    res_dict = {}

    for row in data:
        result = soup.find('span', text=re.compile(row))
        res_dict[row] = result.parent.parent.contents[1].text
    return FinanceYahooResponse(company, res_dict['Book Value Per Share'], res_dict['Gross Profit'],
                                res_dict['Return on Assets'])


def get_finance_data_async(companies, proxies):
    res_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Start the load operations and mark each future with its company
        future_to_company = {executor.submit(get_finance_data, company, proxies): company
                             for company in companies}
        for future in concurrent.futures.as_completed(future_to_company):
            url = future_to_company[future]
            try:
                res = future.result()
                print('Processing')
                res_list.append(res)
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
    return res_list


def write_news_to_csv(news: List[NewsApiPayload]):
    dict = {
        'Title': [x.title for x in news],
        'Description': [x.description for x in news],
        'Published at': [x.published_at for x in news],
        'Url': [x.url for x in news],
        'Author': [x.author for x in news]
    }
    df = pd.DataFrame(dict)
    df.to_csv('news.csv')


def write_finance_to_csv(finances: List[FinanceYahooResponse]):
    dict = {
        'Name': [x.company_name for x in finances],
        'Book Value Per Share': [x.book_value_per_share for x in finances],
        'Gross Profit': [x.gross_profit for x in finances],
        'Return on Assets': [x.return_on_assets for x in finances]
    }
    df = pd.DataFrame(dict)
    df.to_csv('finances.csv')


if __name__ == '__main__':
    from_date = datetime.today().strftime('%Y-%m-%d')
    to_date = (datetime.today() - timedelta(30)).strftime('%Y-%m-%d')
    proxies = get_proxies()
    params = SearchParams('bitcoin',
                          ", ".join(['techcrunch']),
                          from_date,
                          to_date,
                          'publishedAt',
                          '10',
                          1,
                          api)

    companies = ['AAPL', 'MSFT', 'NFLX', 'AMZN']

    results_dict = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = [executor.submit(get_news, params, proxies),
                         executor.submit(get_finance_data_async, companies, proxies)]
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                res = future.result()
                print('Added!')
                results_dict[type(res[0])] = res
            except Exception as exc:
                print('generated an exception: %s' % exc)

    try:
        write_news_to_csv(results_dict[NewsApiPayload])
        write_finance_to_csv(results_dict[FinanceYahooResponse])
    except Exception as e:
        print(f'Exception occurred: {str(e)}')
