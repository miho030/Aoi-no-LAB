# _*_ coding:utf-8 _*_

#---------------------------------------------------------------------------#
"""
Major lib import
"""
import requests
import time, random
from bs4 import BeautifulSoup
from pyfiglet import Figlet

# import urllib for HTTP error code
from urllib import parse
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

"""
CSV Creater Lib import
"""
import lxml # bs4에서 (rs.text, 'lxml') 기능 사용위함
# 긁어온 데이터를 딕셔너리 -> csv 파일로 변환하기 위한 라이브러리
import pandas as pd
# csv 파일 이름 저장을 위한 datetime Lib
from datetime import datetime



#---------------------------------------------------------------------------#



# 기본적인 인터페이스 출력
def interface():
    f = Figlet(font='slant')
    print(f.renderText('   Naver Movie\n          crawler'))
    print(" CopyRight all served By kbu")

# 크롤링 항목을 선택하는 창에서의 인터페이스 출력
def choice_function():
    print("[!] ", "어떤 홈페이지를 크롤링할지 선택해주세요! : ")
    print("")
    print("                    1) 네이버 영화 시청자리뷰   ")
    print("                    2) 제작중                ")


    print("")
#---------------------------------------------------------------------------#

"""
===================================
        URL checking code
===================================
"""
def check_url(input_url):
    # churl = input_url

    # 검증 절차 시작 안내 인터페이스
    print("")
    print("")
    print("#=======================================#")
    print("     [ ! ] URL이 유효한지 검증 중입니다.     ")
    print("#=======================================#")

    rs = requests.get(input_url)
    rs_code = rs.status_code
    if int(rs_code) == 200:
        print("요청한 서버 URL : ",input_url)
        print("요청한 서버 HTTP응답코드 : ",rs_code)
        print("[+] ", "URL이 유효하며 서버가 정상작동중입니다!")
    else:
        print(rs_code)
        print("[+] ", "URL이 유효하지 않습니다...")
        print("[-] ", "요청한 서버 HTTP응답코드 : ", rs_code)
#---------------------------------------------------------------------------#

"""
===================================
     Main source code
===================================
"""
def main():
    interface()
    choice_function()
    choice = input("[+] 선택한 항목의 번호를 적어주세요! (ex. 1 ) :  ")
    if int(choice) == 1:
        NM()
    if int(choice) == 2:
        input_url = input("[+]  url을 입력해 주세요 : ")
        check_url(input_url)
    else:
        print("[!] ", "잘못된 값이 입력되었어요ㅠㅠ")
        print("[-] ", "잠시후 다시 시도해주세요.")
        exit()
# ---------------------------------------------------------------------------#

"""
===================================
     Naver Movie source code
===================================
"""
def NM():

    # 이 부분은 네이버 영화 홈페이지에서 영화에 대한
    # 시청자의 리뷰를 정리한 모듈임.
    file_date = datetime.today().strftime("%Y%m%d%H%M%S")

    base_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'
    # input_url = str(input(" inserct movie's name"))

    comment_list = []

    for page in range(1, 101):
        # 네이버측에서 계속된 페이지 요청은 차단하기 때문에 랜덤함수 이용한다.
        url = base_url.format(page)
        # url = input_url.format(page)
        res = requests.get(url)
        if res.status_code == 200: # 만약 movie.naver.com과 정상연결이 확인되면
            soup = BeautifulSoup(res.text, 'lxml')
            tds = soup.select('table.list_netizen > tbody > tr > td.title')
            for td in tds:
                movie_title = td.select_one('a.movie').text.strip()
                score = td.select_one('div.list_netizen_score > em').text.strip()
                comment = td.select_one('br').next_sibling.strip()
                comment_list.append((movie_title, score, comment))
            interval = round(random.uniform(0.2, 1.2), 2)
            time.sleep(interval)


        # 크롤링한 랜덤 page 값을 CSV 제작 모듈에 넣어준다.
        # 파일을 DB에 입력하기 용이하도록, *.csv 파일로 저장한다.

        print('[+] ', page, ' page of crawling [Naver Movie] review done!')
        df = pd.DataFrame(comment_list,
                          columns=['name', 'rate', 'reviews'])
        df.to_csv(f'Naver_Movie{file_date}.csv', encoding='utf-8', index=False)

#---------------------------------------------------------------------------#


main()

