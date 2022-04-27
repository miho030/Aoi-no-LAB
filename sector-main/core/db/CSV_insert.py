#_*_coding:utf-8 _*_

"""
이 파일은 DB와 파이썬이 연동되어, 모듈화된 크롤러의  csv 파일을
모두 찾아내어, 파일이름에 맞추어 DB로 자동 삽입(insert)하는 모듈임.
"""
# major Lib import
import pymysql.cursors
import threading

# find csv file and, To copy csv file for db insert
import os
from os import path
import shutil


def find_csv():
    src = "C:\\Users\\5008\\Desktop\\alpa\\modules\\Naver_Movie\\"
    dst = "C:\\Users\\5008\\Desktop\\alpa\\core\\db\\csv_files\\"

    files = os.listdir(src)
    print("[-] ", "DB에 넣을 csv 파일을 찾고 있습니다")
    print(files)

    files = [i for i in os.listdir(src) if i.endswith(".csv") and path.isfile(path.join(src, i))]
    for f in files:
        shutil.copy(path.join(src, f), dst)
        print("[+] 파일 [", f, "] 가 이동되었습니다.")
        print("")

def cAn():
    # connection 정보
    print("[+] ", "MYSQL DB와 연동을 시작합니다.")
    try:
        conn = pymysql.connect(
            host = '', # host name
            user = '', # user name
            password = '', # password
            db = '', # db name
            charset = 'utf8'
            )
    except ConnectionRefusedError:
        print("[!]", "대상 컴퓨터에서 연결을 거부하였습니다.")
    except UnboundLocalError:
        print("[!] ", "서버 연결 정보가 올바르지 않습니다.")
    except pymysql.err.OperationalError:
        print("[!] ","localhost를 찾지 못하였음.")


    curs = conn.cursor()
    # 실행할 sql 구문 입력
    sql = ""
    curs.execute(sql)
    conn.commit()
    threading.Timer(5, cAn).start()

find_csv()
cAn()


