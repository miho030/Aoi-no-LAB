"""
# _*_coding:utf-8 _*_

# major lib import
import cx_Oracle
import os

# 한글 지원 설정
os.putenv('NLS_LANG', 'UTF8')

# 연결에 필요한 정보 기입
conn = cx_Oracle.connect('root', '1234', 'localhost/orcl')



cursor = conn.cursor()

#DB에서 실행할  SQL문을 적는다...
# 일단은 가완성된 DB structure 이용한다...{아래 주석문에서 DB 구조 참고}

# Main(DB) -> sub(스키마) -> NM(테이블1), CP(테이블2)

cursor.execute(
    select comment
    from NM;
    where text = :texting,
    texting = "테스트"
               )

for name in cursor:
    print("Testing for DB comment import : ", comment)
"""