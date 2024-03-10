import snowflake.connector
import pandas as pd
from sklearn.linear_model import LinearRegression

# Snowflake 연결 설정
conn = snowflake.connector.connect(
    user='<사용자명>',
    password='<비밀번호>',
    account='<계정명>.snowflakecomputing.com',
    warehouse='<웨어하우스명>',
    database='<데이터베이스명>',
    schema='<스키마명>'
)

# SQL 쿼리 실행하여 데이터 가져오기
query = 'SELECT * FROM my_table'
df = pd.read_sql(query, conn)

# 선형 회귀 모델 훈련
X = df[['feature1', 'feature2']]  # 입력 특성
y = df['target']  # 타겟 변수
model = LinearRegression()
model.fit(X, y)

# 새로운 데이터로 예측
new_data = pd.DataFrame({'feature1': [10], 'feature2': [20]})
predicted_value = model.predict(new_data)
print(f"Predicted value: {predicted_value[0]}")

# 연결 종료
conn.close()
