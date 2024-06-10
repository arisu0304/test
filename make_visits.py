import sqlite3
import json

# SQLite 데이터베이스 연결
con = sqlite3.connect("C://Users//bitcamp//Desktop//history_network_graph//History")
cursor = con.cursor()

# 데이터베이스에서 URL 추출 및 처리
cursor.execute("""
               SELECT   v.url 
                     , v.visit_duration
                     , vv.url 
                FROM visits v
                LEFT JOIN visits vv
                ON v.from_visit = vv.id
                ORDER BY v.url
               """)
rows = cursor.fetchall()

# 추출된 데이터를 딕셔너리로 변환
data = []
for row in rows:
    di = {}
    di["url"] = row[0]
    di["visit_duration"] = row[1]
    di["from_url"] = row[2]
    data.append(di)

# JSON 파일로 저장
with open('visits.json', 'w') as f:
    json.dump(data, f, indent=4)
