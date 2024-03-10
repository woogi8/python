import openpyxl
import cx_Oracle

# Oracle DB 연결
connection = cx_Oracle.connect("<스키마>", "<비밀번호>", "<호스트명>/<SID/서비스명>")
print("데이터베이스 버전:", connection.version)

# 테이블 생성
create_table = """
CREATE TABLE test (
    col1 VARCHAR2(50) NOT NULL,
    col2 VARCHAR2(50) NOT NULL,
    col3 VARCHAR2(50) NOT NULL,
    col4 VARCHAR2(50) NOT NULL,
    col5 VARCHAR2(50) NOT NULL,
    col6 VARCHAR2(50) NOT NULL,
    col7 VARCHAR2(50) NOT NULL
)
"""
cursor = connection.cursor()
cursor.execute(create_table)

# 엑셀 파일 로드
wb = openpyxl.load_workbook('<파일명>', data_only=True)
ws = wb['Sheet1']

x = 1
m = 1

# 각 열마다 데이터 삽입
for j in range(2, ws.max_column + 1):
    ID = m
    col1 = ws.cell(row=x, column=j).value
    m += 1
    col2 = ws.cell(row=1, column=j).value
    col3 = ws.cell(row=2, column=j).value
    col4 = ws.cell(row=3, column=j).value
    col5 = ws.cell(row=4, column=j).value
    col6 = ws.cell(row=5, column=j).value
    col7 = ws.cell(row=6, column=j).value

    # 각 행마다 데이터 삽입
    for i in range(1, ws.max_row + 1):
        Cellval = ws.cell(row=i, column=j).value
        insert_table = f"""
        INSERT INTO test (col1, col2, col3, col4, col5, col6, col7)
        VALUES ('{col1}', '{col2}', '{col3}', '{col4}', '{col5}', '{col6}', '{col7}')
        """
        cursor.execute(insert_table)
        x += 1

# 연결 종료
connection.close()
