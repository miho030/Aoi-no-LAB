# _*_ coding:utf-8 _*_

"""
Major lib import
"""
import requests
from urllib import parse
import time
import random
from bs4 import BeautifulSoup

import pandas as pd

"""

===================================
        Main source code
===================================

"""

base_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'
# input_url = str(input(" inserct movie's name"))

comment_list = []

for page in range(1,101):
    url = base_url.format(page)
    # url = input_url.format(page)
    res=requests.get(url)
    if res.status_code == 200:
        soup= BeautifulSoup(res.text, 'lxml')
        tds = soup.select('table.list_netizen > tbody > tr > td.title')
        for td in tds:
            movie_title = td.select_one('a.movie').text.strip()
            link = td.select_one('a.movie').get('href')
            link = parse.urljoin(base_url, link)
            score = td.select_one('div.list_netizen_score > em').text.strip()
            comment = td.select_one('br').next_sibling.strip()
            comment_list.append((movie_title, link, score, comment))
        interval = round(random.uniform(0.2, 1.2), 2)
        time.sleep(interval)
    print('[+] ', page, ' page of crawling [Naver Movie] review done!')
    df = pd.DataFrame(comment_list,
                      columns=['name', 'link', 'rate', 'reviews'])
    df.to_csv('naver_comment.csv', encoding='utf-8', index=False)