import sqlite3
import json

# SQLite 데이터베이스 연결
con = sqlite3.connect("C://Users//bitcamp//Desktop//history_network_graph//History")
cursor = con.cursor()

# 데이터베이스에서 URL 추출 및 처리
cursor.execute("""
               SELECT  id
                        , CASE \
                            WHEN url LIKE '%.com/%' THEN SUBSTR(url, 1, INSTR(url, '.com') + 3) \
                            WHEN url LIKE '%.kr/%' THEN SUBSTR(url, 1, INSTR(url, '.kr') + 3) \
                            WHEN url LIKE '%.io/%' THEN SUBSTR(url, 1, INSTR(url, '.io') + 2) \
                            WHEN url LIKE '%.net/%' THEN SUBSTR(url, 1, INSTR(url, '.net') + 3) \
                            ELSE url \
                         END AS url \
                FROM urls
                ORDER BY id;
               """)
rows = cursor.fetchall()

# 추출된 데이터를 딕셔너리로 변환
data = {}

for row in rows:
    data[row[0]] = row[1]

# JSON 파일로 저장
with open('urls.json', 'w') as f:
    json.dump(data, f, indent=4)
